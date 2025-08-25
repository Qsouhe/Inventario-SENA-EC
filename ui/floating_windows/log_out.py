import dearpygui.dearpygui as dpg
from utils import themes, loader
from events import inventory_events
from ui.floating_windows import verify
from events import window_change
import data

def log_out(tag_primary):
    def bye():
        window_change.window_change(tag_primary, "login")
        data.user_data.add_id(None)
        dpg.delete_item("window_log_out")
    
    size_p_window = dpg.get_item_rect_size(tag_primary)
    width = 300
    height = 80

    pos = ((size_p_window[0] / 2) - (width / 2), (size_p_window[1] / 2) - (height / 2))

    with dpg.window(no_resize=True, no_collapse=True, no_title_bar=True, modal=True, no_move=True,
                    tag="window_log_out", width=width, height=height, label="Eliminar", pos=pos):
        dpg.add_spacer(height=20)
        dpg.add_text("Seguro que quieres cerrar Sesion?", indent=20)
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=20)
            dpg.add_button(label="Confirmar", tag="btn_confirmar_log_out", callback=bye)
            dpg.add_button(label="Cancelar", callback=lambda: dpg.delete_item("window_log_out"))
        
    dpg.bind_item_theme("window_log_out", themes.themes["ventana_delete"])
    dpg.bind_item_theme("btn_confirmar_log_out", themes.themes["btn_rojo"])