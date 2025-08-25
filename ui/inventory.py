from events import window_change
from utils import loader, themes, widgets_pos_size
import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg
from ui.floating_windows import append, delete
from events import inventory_events
from ui.floating_windows import log_out

loader_styleqs = False

def inventory_window():
    with dpg.window(tag="ventana_inventory", show=False):
        with dpg.child_window(tag="opciones_inventory", border=False):
            dpg.add_image_button(   texture_tag=loader.iconuser, 
                                    width=45, height=45, 
                                    tag="btn_usuarios_inventory",
                                    callback= lambda: window_change.window_change("ventana_inventory", "user"))
            dpg.add_image_button(   texture_tag=loader.icondashboard, 
                                    width=45, height=45,
                                    tag="btn_dashboard_inventory",
                                    callback= lambda: window_change.window_change("ventana_inventory", "dashboard"))
            dpg.add_image_button(   texture_tag=loader.iconinventory_active, 
                                    width=45, height=45,
                                    tag="btn_inventario_inventory",
                                    callback=inventory_events.load)
            dpg.add_image_button(   texture_tag=loader.iconexit, 
                                    width=45, height=45,
                                    tag="btn_exit_inventory",
                                    callback= lambda: log_out.log_out("ventana_inventory"))

        with dpg.child_window(tag="inventory", border=False):
            with dpg.child_window(tag="opciones_inventory_edits", border=False):
                dpg.add_image_button(   loader.iconload, 
                                        tag="btn_load_inventory", 
                                        width=41, 
                                        height=41,
                                        callback=inventory_events.load)
                dpg.add_button(label="Agregar", tag="btn_agregar_inventory", callback=append.w_append)
                dpg.add_button(label="Eliminar", tag="btn_eliminar_inventory", callback=lambda: delete.delete(inventory_events.seleccion))
                dpg.add_input_text(tag="buscador_inventario", hint="Buscar...", callback=inventory_events.filter_rows)

            with dpg.child_window(border=False, tag="container_table"):
                with dpg.filter_set(tag="filtro_inventario"):
                    with dpg.table( resizable=False, 
                                    borders_innerH=False, 
                                    borders_innerV=False, 
                                    borders_outerV=False, 
                                    borders_outerH=False,
                                    row_background=True,
                                    pad_outerX=True,
                                    policy=dpg.mvTable_SizingFixedFit,
                                    tag="table_inventory",
                                    ):
                        dpg.add_table_column()
                        dpg.add_table_column(label="Fecha", width_fixed=False)
                        dpg.add_table_column(label="Imagen", width_fixed=False)
                        dpg.add_table_column(label="Nombre", width_fixed=False)
                        dpg.add_table_column(label="Descripcion", width_stretch=True)
                        dpg.add_table_column(label="Serial", width_fixed=False)
                        dpg.add_table_column(label="Ubicacion", width_fixed=False)
                        dpg.add_table_column(label="Estado", width_fixed=False)

    dpg.bind_item_theme("ventana_inventory", themes.themes["fondo_home"])
    dpg.bind_item_theme("btn_usuarios_inventory", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_dashboard_inventory", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_inventario_inventory", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_exit_inventory", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("btn_load_inventory", themes.themes["boton_img_sin_fondo"])
    dpg.bind_item_theme("opciones_inventory", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("inventory", themes.themes["childwindow_no_background"])
    dpg.bind_item_theme("buscador_inventario", themes.themes["buscador"])
    dpg.bind_item_theme("btn_agregar_inventory", themes.themes["btn_verde"])
    dpg.bind_item_theme("btn_eliminar_inventory", themes.themes["btn_rojo"])
    dpg.bind_item_theme("table_inventory", themes.themes["tema_tabla_inventory"])
    dpg.bind_item_theme("container_table", themes.themes["fondo_contenedor_inventory"])

def execute_styleqs():
    dpg.configure_item("ventana_carga", show=True)

    inventory_events.load()

    with dpg_sqs.WindowLayout("ventana_inventory"):
        with dpg_sqs.FlexLayoutBuilder( tag="opciones_inventory",
                                        padding=10,
                                        gap=10,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width=60
                                        ) as opciones_inventory:
            opciones_inventory.add_widget(tag="btn_exit_inventory", position=dpg_sqs.AbsolutePosition("bottom"))

        with dpg_sqs.FlexLayoutBuilder( tag="ventana_inventory",
                                        gap=15,
                                        padding=10,
                                        horizontal=True,
                                        alling_widgets="alling_center",
                                        height="default"
                                        ) as ventana_user:
            ventana_user.add_widget(tag="inventory", height=dpg_sqs.PercentageSize(100))

        with dpg_sqs.FlexLayoutBuilder( tag="opciones_inventory_edits",
                                        gap=15,
                                        horizontal=True):
            pass

        with dpg_sqs.FlexLayoutBuilder( tag="inventory",
                                        gap=15,
                                        alling_widgets="alling_center",
                                        height="default",
                                        width="default"
                                        ) as inventory:
            inventory.add_widget(tag="opciones_inventory_edits", width=dpg_sqs.PercentageSize(100))

    dpg_sqs.bind_widget_theme("opciones_inventory", themes.themes["fondo_gradiant_contenedores"])
    dpg_sqs.execute_after(lambda: widgets_pos_size.posicionamiento_exit("btn_exit_inventory"))
    dpg_sqs.execute_after(lambda: widgets_pos_size.size_input_automatic_right("buscador_inventario", "opciones_inventory_edits"))
    dpg_sqs.execute_after(lambda: dpg.configure_item("ventana_carga", show=False))
    dpg_sqs.execute_styleqs()