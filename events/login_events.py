import dpg_styleqs.internal.image as sqs_image
from ui.floating_windows import verify
from tkinter import Tk, filedialog
import dearpygui.dearpygui as dpg
from utils import loader, themes
from events import window_change
from backend import backend
from PIL import Image
import bcrypt
import data

#Funcion que registra el usuario
def register(callback_finish):
    content = backend.obtener_usuario()
    icorrect_inputs = False

    def set_false():
        nonlocal icorrect_inputs
        if icorrect_inputs == False:
            icorrect_inputs = True

    try:
        imagen = dpg.get_item_user_data("btn_upload_img_user")["img_pillow"]
    except:
        imagen = None

    alias = dpg.get_value("input_aliasin")
    nombres_apellidos = dpg.get_value("input_nombre_apellido")
    numero_telefonico = dpg.get_value("input_numero")
    correo_institucional = dpg.get_value("input_correoin")
    contraseña = dpg.get_value("input_contraseña_rg")
    confirmar_contraseña = dpg.get_value("input_confirmar_contraseña_rg")

    if alias:
        for c in content:
            if alias == c["ALIAS"]:
                dpg.bind_item_theme("input_aliasin", themes.themes["incorrect_input"])
                set_false()
                verify.verify(f"ventana_validacion", "Ya existe el alias: {alias}, intenta con otro", "red")
                return
        dpg.bind_item_theme("input_nombre_apellido", themes.themes["neutral_input"])
    else:
        dpg.bind_item_theme("input_aliasin", themes.themes["incorrect_input"])
        verify.verify("ventana_validacion", "El campo 'alias' es obligatorio", "red")
        set_false()

    if not nombres_apellidos:
        dpg.bind_item_theme("input_nombre_apellido", themes.themes["incorrect_input"])
        verify.verify("ventana_validacion", "El campo 'nombre y apellido' es obligatorio", "red")
        set_false()
    else:
        dpg.bind_item_theme("input_nombre_apellido", themes.themes["neutral_input"])
    
    if not contraseña:
        dpg.bind_item_theme("input_contraseña_rg", themes.themes["incorrect_input"])
        verify.verify("ventana_validacion", "El campo 'Contraseña' es obligatorio", "red")
        set_false()
    else:
        dpg.bind_item_theme("input_contraseña_rg", themes.themes["neutral_input"])
    
    if confirmar_contraseña != contraseña:
        dpg.bind_item_theme("input_confirmar_contraseña_rg", themes.themes["incorrect_input"])
        verify.verify("ventana_validacion", "La 'Contraseña' y la 'Confirmar contraseña' no coinciden", "red")
        set_false()
    else:
        dpg.bind_item_theme("input_confirmar_contraseña_rg", themes.themes["neutral_input"])
    
    if icorrect_inputs == True:
        return
    else:
        if imagen:
            with dpg.window(modal=True,
                    no_resize=True,
                    no_collapse=True, 
                    no_title_bar=True, 
                    no_move=True,
                    no_scrollbar=True,
                    no_background=True,
                    tag="subiendo_datos"):

                dpg.add_text("Subiendo datos...")

            img_subida = backend.subir_img_users(imagen, alias)
            id_usuario = 0
            
            if content:
                for c in content:
                    id_usuario = max(id_usuario, c["ID"])
                id_usuario += 1

            contraseña = contraseña.encode("utf-8")
            hash_contraseña = bcrypt.hashpw(contraseña, bcrypt.gensalt())
            hash_contraseña = hash_contraseña.decode("utf-8")

            estructura = [[id_usuario, alias, img_subida["id"], nombres_apellidos, numero_telefonico, correo_institucional, hash_contraseña]]
            backend.agregar_usuario(estructura)

            callback_finish()

            dpg.set_value("input_aliasin", "")
            dpg.set_value("input_nombre_apellido", "")
            dpg.set_value("input_numero", "")
            dpg.set_value("input_correoin", "")
            dpg.set_value("input_contraseña_rg", "")
            dpg.set_value("input_confirmar_contraseña_rg", "")
            dpg.configure_item("upload_img", texture_tag=loader.iconupload)

            verify.verify("ventana_validacion", "Registro exitoso", "green")
        else:
            verify.verify("ventana_validacion", "El parametro de imagen es obligatorio", "red")
    
    dpg.delete_item("subiendo_datos")

def validation():
    content = backend.obtener_usuario()

    nombre_apellido = dpg.get_value("input_alias_lg")
    contraseña = dpg.get_value("input_contraseña_lg")

    for c in content:
        if nombre_apellido == c["ALIAS"]:
            if bcrypt.checkpw(contraseña.encode("utf-8"), c["CONTRASEÑA"].encode("utf-8")):
                window_change.window_change("ventana_validacion", "dashboard")
                dpg.bind_item_theme("input_alias_lg", themes.themes["neutral_input"])
                data.user_data.add_id(c["ID"])

                dpg.set_value("input_alias_lg", "")
                dpg.set_value("input_contraseña_lg", "")
                return
            else:
                verify.verify("ventana_validacion", "La contraseña no coincide", "red")
                dpg.bind_item_theme("input_contraseña_lg", themes.themes["incorrect_input"])
                return

    verify.verify("ventana_validacion", "No se encontro el usuario", "red")
    dpg.bind_item_theme("input_alias_lg", themes.themes["incorrect_input"])

def select_img():
    with dpg.window(modal=True,
                    no_resize=True,
                    no_collapse=True, 
                    no_title_bar=True, 
                    no_move=True,
                    no_scrollbar=True,
                    no_background=True,
                    tag="seleccion_imagen"
                    ):
        pass

    # Tk para filedialog
    root = Tk(); root.withdraw()
    ruta = filedialog.askopenfilename(  title="Selecciona una imagen",
                                        filetypes=[("Imagenes", "*.png *.jpg *.jpeg *.bmp *.tga")])
    root.destroy()
    if not ruta:
        dpg.delete_item("seleccion_imagen")
    try:
        img_pillow = Image.open(ruta).convert("RGBA")
    except Exception as e:
        print("Error abriendo la imagen:", e)
        dpg.delete_item("seleccion_imagen")
        return

    verify.verify("ventana_validacion", "Cargando imagen", "green")

    width, height = img_pillow.size
    min_side = min(width, height)
    left = (width - min_side) // 2
    top = (height - min_side) // 2
    img_pillow = img_pillow.crop((left, top, left + min_side, top + min_side))

    # limitar tamaño para seguridad (opcional)
    MAX_SIDE = 1024
    if min_side > MAX_SIDE:
            img_pillow = img_pillow.resize((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            min_side = MAX_SIDE

    # aplicar efectos si quieres (manejo de excepciones)
    try:
        img_pillow = sqs_image.ImageStyleQs.EffectsImage(img_pillow).rounded_corners(radius=int(min_side/2)).image_return()
    except Exception as e:
        print("Advertencia: fallo aplicando efectos:", e)

    if img_pillow.mode != "RGBA":
        img_pillow = img_pillow.convert("RGBA")

    # Normalizar bytes (DearPyGui espera floats 0..1)
    data = [c / 255.0 for c in img_pillow.tobytes()]  # len == min_side*min_side*4

    texture_tag = "upload_texture_tag"  # tag fijo para reutilizar

    # Si ya existe la textura, intentamos solo actualizar los datos
    if dpg.does_item_exist(texture_tag):
        try:
            dpg.set_value(texture_tag, data)   # actualizar datos de la textura dinámica
        except Exception as e:
            # si actualizar falla (por ejemplo tamaño distinto), borramos y recreamos
            try:
                dpg.delete_item(texture_tag)
            except Exception:
                pass
            with dpg.texture_registry():
                dpg.add_dynamic_texture(min_side, min_side, data, tag=texture_tag)
    else:
        # crear textura dinámica por primera vez
        with dpg.texture_registry():
            dpg.add_dynamic_texture(min_side, min_side, data, tag=texture_tag)

        dpg.configure_item("upload_img", texture_tag=texture_tag)
        dpg.set_item_user_data("btn_upload_img_user", {"img_pillow": img_pillow})
    
    dpg.delete_item("seleccion_imagen")