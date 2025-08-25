import dearpygui.dearpygui as dpg
import dpg_styleqs.dpg_styleqs as dpg_sqs
from utils import themes, loader
from events import inventory_events

def w_append():
    size_p_window = dpg.get_item_rect_size("ventana_inventory")
    width = 1000
    height = 680

    pos = ((size_p_window[0] / 2) - (width / 2), (size_p_window[1] / 2) - (height / 2))

    with dpg.window(no_resize=True, no_collapse=True, no_title_bar=True, modal=True, no_move=True,
                    tag="window_append", width=width, height=height, label="Agregar", pos=pos):

        with dpg.child_window(border=False, auto_resize_y=True):
            dpg.add_text("Agregar:", tag="txt_agregar")
            with dpg.group(horizontal=True):
                with dpg.child_window(auto_resize_x=True, auto_resize_y=True, border=False):
                    dpg_sqs.add_image(route="recursos/imagenes/upload_element.png", width=285, height=285, tag="img_element")
                    dpg.add_button(label="Agregar imagen", width=285, tag="btn_upload_img_element", callback=inventory_events.select_img)

                dpg.add_spacer(width=5)
                with dpg.child_window(auto_resize_y=True, border=False):
                    dpg.add_text("Nombre:")
                    dpg.add_input_text(hint="Ejem: Portatil", tag="nombre_elemento", callback=inventory_events.propagate_name_change)
                    dpg.add_text("Descripcion:")
                    dpg.add_input_text( hint="Ejem: Se encuentra en buen estado(Opcional)", tag="descripcion_elemento",
                                        callback=inventory_events.propagate_main_change, user_data="descripcion")
                    dpg.add_text("Ubicacion:")
                    dpg.add_input_text( hint="Ejem: Economia Circular", tag="ubicacion_elemento",
                                        callback=inventory_events.propagate_main_change, user_data="ubicacion")
                    dpg.add_text("Estado:")
                    dpg.add_combo(  items=["Buen estado", "Mantenimiento", "Dado de baja"],
                                    default_value="Buen estado", tag="estado_elemento",
                                    callback=inventory_events.propagate_main_change, user_data="estado")
                    dpg.add_text("Cantidad:")
                    dpg.add_drag_int(   speed=0.5, callback=inventory_events.append_component, tag="cantidad",
                                        min_value=1, default_value=1)

        with dpg.child_window(border=False, tag="contenedor_elementos", height=255):
            pass

        with dpg.child_window(border=False, auto_resize_y=True):
            with dpg.group(horizontal=True):
                dpg.add_button(label="Agregar", tag="btn_agregar", callback=inventory_events.on_add_clicked)
                dpg.add_button(label="Cancelar", tag="btn_cancelar", callback=inventory_events.delete_window)

    dpg.bind_item_font("txt_agregar", loader.fuente_titulo)

    dpg.bind_item_theme("window_append", themes.themes["ventana_append"])
    dpg.bind_item_theme("btn_agregar", themes.themes["btn_verde"])
    dpg.bind_item_theme("btn_cancelar", themes.themes["btn_gris_activo"])

    inventory_events.append_component()