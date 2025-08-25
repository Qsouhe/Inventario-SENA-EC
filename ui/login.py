import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg
from utils import loader, themes
from events import login_events
from ui.warnings import no_conexion
from backend import backend

def valid():
    valid = backend.init_sheets()
    if not valid:
        no_conexion.w_sin_conexion()

#Cambia la sesion de inicio de sesion por la de registro de usuario y viceversa
def mostrar():
            if dpg.is_item_shown("childwindow_registro"):
                dpg.configure_item("childwindow_inicio_sesion", show=True)
                dpg.configure_item("childwindow_registro", show=False)
            else:
                dpg.configure_item("childwindow_inicio_sesion", show=False)
                dpg.configure_item("childwindow_registro", show=True)

def login_window():
    with dpg.window(tag="ventana_validacion"):
        #------------------------------ SESION DE INICIO DE SESION ------------------------------
        with dpg.child_window(  border=False, 
                                tag="childwindow_inicio_sesion"):
            dpg_sqs.add_image(  route="recursos/imagenes/logoSENA.png", 
                                width=175, 
                                height=150,
                                tag="logoSENA")
            dpg.add_text("ECONOMIA CIRCULAR", 
                        tag="txt_EC")

            with dpg.child_window(  tag="formulario_inicio_sesion", 
                                    border=False):
                dpg.add_input_text( hint="Alias", 
                                    tag="input_alias_lg", 
                                    callback=lambda: dpg.focus_item("input_contraseña_lg"), 
                                    on_enter=True)
                dpg.add_input_text( hint="Contraseña", 
                                    password=True, 
                                    tag="input_contraseña_lg",
                                    callback=login_events.validation,
                                    on_enter=True)
                dpg.add_button( label="Inicio de sesion",
                                tag="btn_inicio_sesion",
                                callback= login_events.validation)

            dpg.add_button( label="Aun no te has registrado? Registrate!", 
                            tag="btn_register_ventana",
                            callback=mostrar)

        #------------------------------ SESION DE REGISTRO DE USUARIO ------------------------------
        with dpg.child_window(  border=False, 
                                tag="childwindow_registro"):
            with dpg.child_window(  tag="formulario_registro", 
                                    border=False):
                dpg.add_image(  loader.iconupload, 
                                width=125, 
                                height=125, 
                                tag="upload_img")
                dpg.add_button( label="Subir Imagen", 
                                tag="btn_upload_img_user", 
                                callback=login_events.select_img)
                dpg.add_input_text( hint="Alias", 
                                    tag="input_aliasin",
                                    callback=lambda: dpg.focus_item("input_nombre_apellido"),
                                    on_enter=True)
                dpg.add_input_text( hint="Nombre y apellido", 
                                    tag="input_nombre_apellido",
                                    callback=lambda: dpg.focus_item("input_numero"),
                                    on_enter=True)
                dpg.add_input_text( hint="Numero telefonico (Opcional)", 
                                    tag="input_numero", 
                                    default_value="",
                                    callback=lambda: dpg.focus_item("input_correoin"),
                                    on_enter=True)
                dpg.add_input_text( hint="Correo Institucional (Opcional)", 
                                    tag="input_correoin", 
                                    default_value="",
                                    callback=lambda: dpg.focus_item("input_contraseña_rg"),
                                    on_enter=True)
                dpg.add_input_text( hint="Contraseña", 
                                    tag="input_contraseña_rg",
                                    password=True,
                                    callback=lambda: dpg.focus_item("input_confirmar_contraseña_rg"),
                                    on_enter=True)
                dpg.add_input_text( hint="Confirmar contraseña", 
                                    tag="input_confirmar_contraseña_rg",
                                    password=True,
                                    callback=lambda: login_events.register(mostrar),
                                    on_enter=True)
                dpg.add_button( label="Registrate", 
                                tag="btn_registrate", 
                                callback= lambda: login_events.register(mostrar))

            dpg.add_button( label="Ya estas registrado? Inicia Sesion!", 
                            tag="btn_inicio_sesion_ventana", 
                            callback=mostrar)

    #------------------------------ APLICA LAS FUENTES ------------------------------
    dpg.bind_item_font("txt_EC", loader.fuente_titulo)

    #------------------------------- APLICA LOS TEMAS -------------------------------
    dpg.bind_item_theme("btn_register_ventana", themes.themes["btn_transparente_claro"])
    dpg.bind_item_theme("btn_inicio_sesion_ventana", themes.themes["btn_transparente_claro"])
    dpg.bind_item_theme("formulario_inicio_sesion", themes.themes["formularios"])
    dpg.bind_item_theme("formulario_registro", themes.themes["formularios"])
    dpg.bind_item_theme("childwindow_inicio_sesion", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("childwindow_registro", themes.themes["childwindow_no_background"])

    # Definimos login como ventana principal inicial
    dpg.set_primary_window("ventana_validacion", True)

#Ejecuta las funciones del modulo dpg_styleqs
def execute_styleqs():
    #Crea ventana de carga
    dpg_sqs.window_loader("ventana_carga", "ventana_validacion", (115, 255, 120), (45, 75, 255), 1.5)

    #------------------------------- Ejecuta el tipo de diseño(organizacion de los widgets) -------------------------------
    with dpg_sqs.WindowLayout("ventana_validacion"):
        with dpg_sqs.FlexLayoutBuilder( tag="formulario_inicio_sesion", 
                                        width=400, 
                                        gap=10,
                                        padding=20,
                                        alling_widgets="alling_center"
                                        ) as forl_inicio_sesion:
            forl_inicio_sesion.add_widget(  tag="input_alias_lg", 
                                            width=dpg_sqs.PercentageSize(100))
            forl_inicio_sesion.add_widget(  tag="input_contraseña_lg", 
                                            width=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="childwindow_inicio_sesion",
                                        alling_widgets="alling_center",
                                        width=600,
                                        gap=10
                                        ):
            pass
        
        with dpg_sqs.FlexLayoutBuilder( tag="formulario_registro",
                                        width=500,
                                        gap=10,
                                        padding=20,
                                        alling_widgets="alling_center"
                                        ) as forl_conectate_basedatos:
            forl_conectate_basedatos.add_widget(tag="input_aliasin", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_nombre_apellido", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_apellidos", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_numero", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_correoin", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_correo", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_contraseña_rg", 
                                                width=dpg_sqs.PercentageSize(100))
            forl_conectate_basedatos.add_widget(tag="input_confirmar_contraseña_rg", 
                                                width=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="childwindow_registro",
                                        alling_widgets="alling_center",
                                        width=600,
                                        gap=10,
                                        padding=20
                                        ):
            pass

        with dpg_sqs.FlexLayoutBuilder( tag="ventana_validacion",
                                        width="default",
                                        height="default",
                                        padding=20
                                        ) as apartado_validadion:
            apartado_validadion.add_widget( tag="childwindow_inicio_sesion", 
                                            position=dpg_sqs.AbsolutePosition("center"))
            apartado_validadion.add_widget( tag="childwindow_registro", 
                                            position=dpg_sqs.AbsolutePosition("center"))

    #------------------------------- APLICA LOS TEMAS DE DEARPYGUI -------------------------------
    dpg_sqs.bind_widget_theme("ventana_validacion", themes.themes["fondo_gradiant"])
    dpg_sqs.bind_widget_theme("logoSENA", themes.themes["imagen_sombreado"])
    dpg_sqs.bind_widget_theme("formulario_inicio_sesion", themes.themes["formulario_styleqs"])
    dpg_sqs.bind_widget_theme("formulario_registro", themes.themes["formulario_styleqs"])

    #------------------------------- FUNCIONES QUE SE EJECUTAN AL FINAL -------------------------------
    #Pone a la sesion de inicio de sesion como predeterminado
    dpg_sqs.execute_after(mostrar)
    #Oculta la ventana de carga
    dpg_sqs.execute_after(lambda: dpg.configure_item("ventana_carga", show=False))
    #Verifica la conexion a internet
    dpg_sqs.execute_after(valid)
    #Ejecuta todas las ordenes
    dpg_sqs.execute_styleqs()