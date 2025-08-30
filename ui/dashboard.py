import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg
from events import window_change
from utils import loader, themes, widgets_pos_size, force_layout
from events import dashboard_events
from ui.floating_windows import log_out
import threading
import os
import sys

loader_styleqs = False

def dashboard_window():
    with dpg.window(tag="ventana_dashboard", show=False):
        with dpg.child_window(tag="opciones", border=False):
            dpg.add_image_button(   texture_tag=loader.iconuser, 
                                    width=45, height=45, 
                                    tag="btn_usuarios_dashboard",
                                    callback= lambda: window_change.window_change("ventana_dashboard", "user"))
            dpg.add_image_button(   texture_tag=loader.icondashboard_active, 
                                    width=45, height=45,
                                    tag="btn_dashboard_dashboard",
                                    callback=dashboard_events.load)
            dpg.add_image_button(   texture_tag=loader.iconinventory, 
                                    width=45, height=45,
                                    tag="btn_inventario_dashboard",
                                    callback= lambda: window_change.window_change("ventana_dashboard", "inventory"))
            dpg.add_image_button(   texture_tag=loader.iconexit, 
                                    width=45, height=45,
                                    tag="btn_exit_dashboard",
                                    callback= lambda: log_out.log_out("ventana_dashboard"))

        with dpg.child_window(tag="dashboard", border=False):
            dpg.add_input_text(hint="Buscar", tag="buscador_dashboard", callback=dashboard_events.filter_rows)
            dpg.add_combo(items=["Nombre" ,"Serial", "Categoria"], default_value="Nombre", tag="filtrado")

            with dpg.child_window(tag="equipos_recientes", border=False):
                dpg.add_text("Mas Recientes:", tag="txt_MasR")
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
                                    tag="table_dashboard",
                                    ):
                        dpg.add_table_column()
                        dpg.add_table_column(label="Imagen", width_fixed=False)
                        dpg.add_table_column(label="Contenedor", width_stretch=True)
                        dpg.add_table_column(label="Estado", width_fixed=False)
                        dpg.add_table_column()

            with dpg.child_window(border=False, tag="graficas_equipos"):
                with dpg.child_window(tag="grafica", border=False):
                    dpg.add_text("Grafica de categorias:", tag="txt_GraficasC")
                    #Grafica
                    with dpg.child_window(width=250, height=150, border=False, tag="grafica_childwindow"):
                        pass

                    dpg.add_button(label="Buen Estado", tag="txt_estado_bueno")
                    dpg.add_text("cantidad: nose", tag="txt_ctd_buen_estado")
                    dpg.add_button(label="Mantenimiento", tag="txt_estado_mantenimiento")
                    dpg.add_text("cantidad: nose", tag="txt_ctd_mantenimiento")
                    dpg.add_button(label="Dado de baja", tag="txt_estado_baja")
                    dpg.add_text("cantidad: nose", tag="txt_ctd_dado_baja")
    
                with dpg.child_window(tag="lista_equipos", border=False):
                    with dpg.child_window(tag="container_lista_equipos", border=False):
                        with dpg.table( resizable=False, 
                                        borders_innerV=False, 
                                        borders_outerV=False, 
                                        borders_outerH=False,
                                        row_background=True,
                                        pad_outerX=True,
                                        header_row=False,
                                        policy=dpg.mvTable_SizingFixedFit,
                                        tag="table_cantidad_elements",
                                        ):
                            dpg.add_table_column()
                            dpg.add_table_column(label="Imagen", width_fixed=False)
                            dpg.add_table_column(label="Contenedor", width_stretch=True)

    dpg.bind_item_font("txt_MasR", loader.fuente_subtitulo_1)
    dpg.bind_item_font("txt_GraficasC", loader.fuente_subtitulo_1)

    dpg.bind_item_theme("ventana_dashboard", themes.themes["fondo_home"])
    dpg.bind_item_theme("btn_usuarios_dashboard", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_dashboard_dashboard", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_inventario_dashboard", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_exit_dashboard", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("buscador_dashboard", themes.themes["buscador"])
    dpg.bind_item_theme("filtrado", themes.themes["combo"])
    dpg.bind_item_theme("opciones", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("dashboard", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("lista_equipos", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("container_lista_equipos", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("equipos_recientes", themes.themes["fondo_contenedores"])
    dpg.bind_item_theme("grafica", themes.themes["fondo_contenedores"])
    dpg.bind_item_theme("txt_estado_bueno", themes.themes["estado_verde"])
    dpg.bind_item_theme("txt_estado_mantenimiento", themes.themes["estado_azul"])
    dpg.bind_item_theme("txt_estado_baja", themes.themes["estado_rojo"])
    dpg.bind_item_theme("table_dashboard", themes.themes["tema_tabla_alt_gris"])
    dpg.bind_item_theme("table_cantidad_elements", themes.themes["tema_tabla_claro"])

def execute_styleqs():
    valid_reset = True

    def stop_reset():
        valid_reset = False

    def reset():
        if valid_reset == True:
            python = sys.executable
            os.execl(python, python, *sys.argv)

    start_reset = threading.Timer(10.0, reset)

    dpg.configure_item("ventana_carga", show=True)

    dashboard_events.load()

    with dpg_sqs.WindowLayout("ventana_dashboard"):
        with dpg_sqs.FlexLayoutBuilder( tag="opciones",
                                        padding=10,
                                        gap=10,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width=60
                                        ) as opciones:
            opciones.add_widget(tag="btn_exit_dashboard", position=dpg_sqs.AbsolutePosition("bottom"))

        with dpg_sqs.FlexLayoutBuilder( tag="ventana_dashboard",
                                        gap=15,
                                        padding=10,
                                        horizontal=True,
                                        alling_widgets="alling_center",
                                        height="default"
                                        ) as ventana_dashboard:
            ventana_dashboard.add_widget(tag="opciones", height=dpg_sqs.PercentageSize(100))
            ventana_dashboard.add_widget(tag="dashboard", height=dpg_sqs.PercentageSize(100))

        with dpg_sqs.GridLayoutBuilder( tag="dashboard", 
                                        rows=2, 
                                        columns=2, 
                                        gap=15
                                        ) as grid_usuarios:
            grid_usuarios.define(dpg_sqs.DefineColumn(column=2, width=dpg_sqs.FixedSize(300)))
            grid_usuarios.define(dpg_sqs.DefineRow(row=1, height=dpg_sqs.FixedSize(36)))

        with dpg_sqs.FlexLayoutBuilder( tag="grafica",
                                        width="default",
                                        padding=20,
                                        gap=5
                                        ) as grafica:
            grafica.add_widget(tag="txt_GraficasC", position=dpg_sqs.StaticPosition("center"))
            grafica.add_widget(tag="grafica_childwindow", position=dpg_sqs.StaticPosition("center"))

        with dpg_sqs.FlexLayoutBuilder( tag="graficas_equipos",
                                        gap=15,
                                        width="default",
                                        height="default",
                                        alling_widgets="alling_center"
                                        ) as graficas_equipos:
            graficas_equipos.add_widget(tag="grafica", width=dpg_sqs.PercentageSize(100))
            graficas_equipos.add_widget(tag="lista_equipos", width=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="equipos_recientes",
                                        alling_widgets="alling_center",
                                        gap=5,
                                        padding=10,
                                        width="default",
                                        height="default"):
            pass

    dpg_sqs.bind_widget_theme("opciones", themes.themes["fondo_gradiant_contenedores"])
    dpg_sqs.bind_widget_theme("lista_equipos", themes.themes["fondo_gradiant_contenedores"])

    dpg_sqs.execute_after(lambda: widgets_pos_size.posicionamiento_exit("btn_exit_dashboard"))
    dpg_sqs.execute_after(lambda: dpg.configure_item("ventana_carga", show=False))
    dpg_sqs.execute_after(stop_reset)
    dpg_sqs.execute_after(force_layout.layout_dashboard)
    dpg_sqs.execute_styleqs()

    start_reset.start