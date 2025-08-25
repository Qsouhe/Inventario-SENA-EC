from events import window_change
from utils import loader, themes, widgets_pos_size, force_layout
import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg
from events import users_events
from ui.floating_windows import log_out

loader_styleqs = False

def user_window():
    with dpg.window(tag="ventana_user", show=False):
        with dpg.child_window(tag="opciones_user", border=False):
            dpg.add_image_button(   texture_tag=loader.iconuser_active, 
                                    width=45, height=45, 
                                    tag="btn_usuarios_user",
                                    callback=users_events.load)
            dpg.add_image_button(   texture_tag=loader.icondashboard, 
                                    width=45, height=45,
                                    tag="btn_dashboard_user",
                                    callback= lambda: window_change.window_change("ventana_user", "dashboard"))
            dpg.add_image_button(   texture_tag=loader.iconinventory, 
                                    width=45, height=45,
                                    tag="btn_inventario_user",
                                    callback= lambda: window_change.window_change("ventana_user", "inventory"))
            dpg.add_image_button(   texture_tag=loader.iconexit, 
                                    width=45, height=45,
                                    tag="btn_exit_user",
                                    callback= lambda: log_out.log_out("ventana_user"))

        with dpg.child_window(tag="user", border=False):
            with dpg.child_window(tag="data_user", width=400, border=False):
                dpg.add_text("Datos del Usuario", tag="txt_window_user")
                dpg_sqs.add_image(route="recursos/imagenes/image_user_xbrrar.png", width=200, height=200, tag="img_user")
                dpg.add_text("Alias:")
                dpg.add_button(label="", tag="btn_alias")
                dpg.add_text("Nombre y apellido:")
                dpg.add_button(label="", tag="btn_nombre_apellido")
                dpg.add_text("Numero telefonico:")
                dpg.add_button(label="", tag="btn_numero_telefonico")
                dpg.add_text("Correo institucional:")
                dpg.add_button(label="", tag="btn_correo_institucional")

            with dpg.child_window(tag="user_changes", border=False):
                dpg.add_text("Mas usuarios", tag="txt_cambios_user")
                with dpg.child_window(border=False):
                    with dpg.table( resizable=False, 
                                    borders_innerH=False, 
                                    borders_innerV=False, 
                                    borders_outerV=False, 
                                    borders_outerH=False,
                                    row_background=True,
                                    pad_outerX=True,
                                    header_row=False,
                                    policy=dpg.mvTable_SizingFixedFit,
                                    tag="table_users",
                                    ):
                        dpg.add_table_column()
                        dpg.add_table_column(label="Imagen", width_fixed=False)
                        dpg.add_table_column(label="Contenedor", width_stretch=True)
                        dpg.add_table_column()

    dpg.bind_item_font("txt_window_user", loader.fuente_titulo)
    dpg.bind_item_font("txt_cambios_user", loader.fuente_titulo)

    dpg.bind_item_theme("ventana_user", themes.themes["fondo_home"])
    dpg.bind_item_theme("btn_usuarios_user", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_dashboard_user", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_inventario_user", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_exit_user", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("user", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("opciones_user", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("data_user", themes.themes["fondo_contenedores"])
    dpg.bind_item_theme("user_changes", themes.themes["fondo_contenedores"])
    dpg.bind_item_theme("btn_alias", themes.themes["btn_gris"])
    dpg.bind_item_theme("btn_nombre_apellido", themes.themes["btn_gris"])
    dpg.bind_item_theme("btn_numero_telefonico", themes.themes["btn_gris"])
    dpg.bind_item_theme("btn_correo_institucional", themes.themes["btn_gris"])
    dpg.bind_item_theme("table_users", themes.themes["tema_tabla_alt_gris"])

def execute_styleqs():
    dpg.configure_item("ventana_carga", show=True)

    users_events.show_data()
    users_events.load()

    with dpg_sqs.WindowLayout("ventana_user"):
        with dpg_sqs.FlexLayoutBuilder( tag="opciones_user",
                                        padding=10,
                                        gap=10,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width=60
                                        ) as opciones_user:
            opciones_user.add_widget(tag="btn_exit_user", position=dpg_sqs.AbsolutePosition("bottom"))

        with dpg_sqs.FlexLayoutBuilder( tag="ventana_user",
                                        gap=15,
                                        padding=10,
                                        horizontal=True,
                                        alling_widgets="alling_center",
                                        height="default"
                                        ) as ventana_user:
            ventana_user.add_widget(tag="user", height=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="user",
                                        gap=15,
                                        horizontal=True,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width="default"
                                        ) as user:
            user.add_widget(tag="data_user", height=dpg_sqs.PercentageSize(100))
            user.add_widget(tag="user_changes", height=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="data_user",
                                        gap=10,
                                        padding=20,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width="default"
                                        ) as dt_user:
            dt_user.add_widget(tag="btn_alias", width=dpg_sqs.PercentageSize(100))
            dt_user.add_widget(tag="btn_nombre_apellido", width=dpg_sqs.PercentageSize(100))
            dt_user.add_widget(tag="btn_numero_telefonico", width=dpg_sqs.PercentageSize(100))
            dt_user.add_widget(tag="btn_correo_institucional", width=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="user_changes",
                                        gap=5,
                                        padding=10,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width="default"
                                        ):
            pass

    dpg_sqs.bind_widget_theme("opciones_user", themes.themes["fondo_gradiant_contenedores"])

    dpg_sqs.execute_after(lambda: widgets_pos_size.posicionamiento_exit("btn_exit_user"))
    dpg_sqs.execute_after(lambda: dpg.configure_item("ventana_carga", show=False))
    dpg_sqs.execute_styleqs()