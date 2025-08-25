import dpg_styleqs.internal.image as sqs_image
from ui.floating_windows import verify
from tkinter import Tk, filedialog
import dearpygui.dearpygui as dpg
from utils import themes, loader
from backend import backend
from datetime import date
from PIL import Image
import traceback
import data

#+----------------------------------------------------------------+
#|                            INVENTORY                           |
#+----------------------------------------------------------------+

seleccion = []
data_rows = []

def checkbox(sender, app_data, user_data):
    if app_data:
        seleccion.append(user_data)
    else:
        seleccion.remove(user_data)

def filter_rows(sender, app_data, user_data):
    if app_data:
        for d in data_rows:
            if app_data in d[1]:
                dpg.configure_item(d[0], show=True)
            else:
                dpg.configure_item(d[0], show=False)
    else:
        for d in data_rows:
            dpg.configure_item(d[0], show=True)

def load():
    content = backend.obtener_inventario()
    children = dpg.get_item_children("table_inventory", 1)

    if children:
        for row in children:
            dpg.delete_item(row)

    for c in content:
        data_imgs = data.user_data.get_imgs()
        img = c["IMAGEN"]
        img_dpg = None
        tag = dpg.generate_uuid()

        if img in data_imgs:
            img_dpg = data_imgs[img]
        else:
            data_register_img = backend.download_img_drive(c["IMAGEN"])
            img_dpg = loader.load_img_byte(data_register_img)
            data.user_data.add_imgs(img, img_dpg)

        filtro_texto = f"{c['FECHA']} {c['NOMBRE']} {c['DESCRIPCION']} {c['SERIAL']} {c['UBICACION']} {c['ESTADO']}"
        data_rows.append([tag, filtro_texto])

        with dpg.table_row(parent="table_inventory", label=filtro_texto, tag=tag):
            dpg.add_checkbox(user_data=c["ID"], callback=checkbox)
            dpg.add_text(c["FECHA"])
            dpg.add_image(img_dpg, width=30, height=30)
            dpg.add_text(c["NOMBRE"])
            dpg.add_text(c["DESCRIPCION"])
            dpg.add_text(c["SERIAL"])
            dpg.add_text(c["UBICACION"])
            dpg.add_text(c["ESTADO"])

#+----------------------------------------------------------------+
#|                          WINDOW DELETE                         |
#+----------------------------------------------------------------+

def delete_elements():
    content = backend.obtener_inventario()
    filas_borrar = []

    for index, c in enumerate(content, start=2):
        if c["ID"] in seleccion:
            filas_borrar.append(index)
    
    for f in sorted(filas_borrar, reverse=True):
        backend.eliminar_fila_inventario(f)

    dpg.delete_item("window_delete")
    load()

#+----------------------------------------------------------------+
#|                          WINDOW APPEND                         |
#+----------------------------------------------------------------+

# Estado global
componentes_creados = []
_next_comp_uid = 0


def select_img():
    # Tk para filedialog
    root = Tk(); root.withdraw()
    ruta = filedialog.askopenfilename(  title="Selecciona una imagen",
                                        filetypes=[("Imagenes", "*.png *.jpg *.jpeg *.bmp *.tga")])
    root.destroy()

    if not ruta:
        pass
    try:
        img_pillow = Image.open(ruta).convert("RGBA")
    except Exception as e:
        print("Error abriendo la imagen:", e)
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
        img_pillow = sqs_image.ImageStyleQs.EffectsImage(img_pillow).rounded_corners(radius=int(min_side/10)).image_return()
    except Exception as e:
        print("Advertencia: fallo aplicando efectos:", e)

    if img_pillow.mode != "RGBA":
        img_pillow = img_pillow.convert("RGBA")

    # Normalizar bytes (DearPyGui espera floats 0..1)
    data = [c / 255.0 for c in img_pillow.tobytes()]  # len == min_side*min_side*4

    texture_tag = "upload_texture_tag_inventory"  # tag fijo para reutilizar

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

        dpg.configure_item("img_element", texture_tag=texture_tag)
        dpg.set_item_user_data("btn_upload_img_element", {"img_pillow": img_pillow})

# Genera un id Unico para cada componente
def _new_uid():
    global _next_comp_uid
    _next_comp_uid += 1
    return f"comp_{_next_comp_uid}"

# Marca campo como bloqueado para que no le afecte la propagacion de los demas campos
def comp_field_changed(sender, app_data, user_data):
    uid, field = user_data
    for c in componentes_creados:
        if c["uid"] == uid:
            c["locked"][field] = True
            break

# Propaga cambios hechos en el formulario principal para todos los componentes
def propagate_main_change(sender, app_data, user_data):
    field = user_data  
    new_value = app_data
    key_map = {"descripcion": "desc", "ubicacion": "ubic", "estado": "estado"}
    for c in componentes_creados:
        if not c["locked"][field]:
            dpg.set_value(c[key_map[field]], new_value)

# Propaga cambios hechos en el nombre del formulario principal para todos los componentes
def propagate_name_change(sender, app_data, user_data):
    new_name = app_data or ""
    for idx, c in enumerate(componentes_creados):
        dpg.set_value(c["text"], f"{new_name} {idx}")

# Crea los componentes de la ventana append
def component(nombre_display, index, initial_values):
    uid = _new_uid()
    ce_tag = f"ce_{uid}"
    text_tag = f"text_{uid}"
    serial_tag = f"serial_{uid}"
    desc_tag = f"desc_{uid}"
    ubic_tag = f"ubic_{uid}"
    estado_tag = f"estado_{uid}"

    with dpg.child_window(auto_resize_y=True, border=False, parent="contenedor_elementos", tag=ce_tag):
        dpg.add_text(nombre_display, tag=text_tag)
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint="Serial", width=231, tag=serial_tag)
            dpg.add_input_text(
                hint="Descripcion", width=231,
                tag=desc_tag,
                default_value=initial_values.get("descripcion", ""),
                callback=comp_field_changed,
                user_data=(uid, "descripcion")
            )
            dpg.add_input_text(
                hint="Ubicacion", width=231,
                tag=ubic_tag,
                default_value=initial_values.get("ubicacion", ""),
                callback=comp_field_changed,
                user_data=(uid, "ubicacion")
            )
            dpg.add_combo(
                items=["Buen estado", "Mantenimiento", "Dado de baja"],
                default_value=initial_values.get("estado", "Buen estado"),
                width=231,
                tag=estado_tag,
                callback=comp_field_changed,
                user_data=(uid, "estado")
            )

    return {
        "uid": uid,
        "ce": ce_tag,
        "text": text_tag,
        "serial": serial_tag,
        "desc": desc_tag,
        "ubic": ubic_tag,
        "estado": estado_tag,
        "locked": {"descripcion": False, "ubicacion": False, "estado": False}
    }

#Controla el numero de componentes que debe de haber
def append_component():
    if not dpg.does_item_exist("cantidad"):
        return
    value = dpg.get_value("cantidad") or 1
    if value < 1:
        dpg.set_value("cantidad", 1)
        value = 1

    nombre = dpg.get_value("nombre_elemento") if dpg.does_item_exist("nombre_elemento") else ""
    actuales = len(componentes_creados)

    initial_values = {
        "descripcion": dpg.get_value("descripcion_elemento") if dpg.does_item_exist("descripcion_elemento") else "",
        "ubicacion": dpg.get_value("ubicacion_elemento") if dpg.does_item_exist("ubicacion_elemento") else "",
        "estado": dpg.get_value("estado_elemento") if dpg.does_item_exist("estado_elemento") else "Buen estado",
    }

    if value > actuales:
        for v in range(actuales, value):
            comp = component(f"{nombre} {v}", v, initial_values)
            componentes_creados.append(comp)
    elif value < actuales:
        for _ in range(actuales - value):
            comp = componentes_creados.pop()
            dpg.delete_item(comp["ce"])

    # actualizar nombres
    current_name = dpg.get_value("nombre_elemento") if dpg.does_item_exist("nombre_elemento") else ""
    for idx, c in enumerate(componentes_creados):
        dpg.set_value(c["text"], f"{current_name} {idx}:")

# Recorre todos los componentes y verifica que cada uno tenga un serial
def on_add_clicked(_, __, ___):
    content = backend.obtener_inventario()

    try:
        imagen = dpg.get_item_user_data("btn_upload_img_element")["img_pillow"]
    except:
        imagen = None

    nombre = dpg.get_value("nombre_elemento")
    ubicacion = dpg.get_value("ubicacion_elemento")

    if not nombre:
        dpg.bind_item_theme("nombre_elemento", themes.themes["incorrect_input"])
        verify.verify("ventana_inventory", "El campo 'nombre' es obligatorio", "red")
        return
    else:
        dpg.bind_item_theme("nombre_elemento", themes.themes["neutral_input"])

    if not ubicacion:
        dpg.bind_item_theme("ubicacion_elemento", themes.themes["incorrect_input"])
        verify.verify("ventana_inventory", "El campo 'Ubicacion' es obligatorio", "red")
        return
    else:
        dpg.bind_item_theme("ubicacion_elemento", themes.themes["neutral_input"])

    nombre_base = dpg.get_value("nombre_elemento") if dpg.does_item_exist("nombre_elemento") else ""
    faltantes = False

    for idx, comp in enumerate(componentes_creados):
        serial = dpg.get_value(comp["serial"])
        if not serial or str(serial).strip() == "":
            faltantes = True

    if faltantes:
        verify.verify("ventana_inventory", f"El campo 'Serial' es obligatorio en cada {nombre}", "red")
        return

    if imagen:
        img_subida = backend.subir_img_inventory(imagen, nombre)
        id_elemento = 0

        if content:
            for c in content:
                id_elemento = max(id_elemento, c["ID"])
            id_elemento += 1

        for idx, comp in enumerate(componentes_creados):
            backend.agregar_inventario([[
                id_elemento,
                str(date.today()),
                img_subida["id"],
                nombre,
                dpg.get_value(comp["desc"]),
                dpg.get_value(comp["serial"]),
                dpg.get_value(comp["ubic"]),
                dpg.get_value(comp["estado"]),
            ]])
            id_elemento += 1
        
        for cc in componentes_creados:
            dpg.delete_item(cc["uid"])
        dpg.delete_item("window_append")
        load()
    else:
        verify.verify("ventana_inventory", "El parametro de imagen es obligatorio", "red")

def delete_window():
    for cc in componentes_creados:
        dpg.delete_item(cc["uid"])
        dpg.delete_item(cc["ce"])
    componentes_creados.clear()
    dpg.delete_item("window_append")