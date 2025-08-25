import dearpygui.dearpygui as dpg
from utils import themes, loader
from events import inventory_events
from ui.floating_windows import verify

def delete(ids):
    if ids:
        size_p_window = dpg.get_item_rect_size("ventana_inventory")
        width = 600
        height = 80

        pos = ((size_p_window[0] / 2) - (width / 2), (size_p_window[1] / 2) - (height / 2))

        with dpg.window(no_resize=True, no_collapse=True, no_title_bar=True, modal=True, no_move=True,
                        tag="window_delete", width=width, height=height, label="Eliminar", pos=pos):
            dpg.add_spacer(height=20)
            dpg.add_text(f"Seguro que quieres eliminar los elementos identificados con el id: {ids}", indent=20)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=180)
                dpg.add_button(label="Confirmar", tag="btn_confirmar_delte", callback=inventory_events.delete_elements)
                dpg.add_button(label="Cancelar", callback=lambda: dpg.delete_item("window_delete"))
        
        dpg.bind_item_theme("window_delete", themes.themes["ventana_delete"])
        dpg.bind_item_theme("btn_confirmar_delte", themes.themes["btn_rojo"])
    else:
        verify.verify("ventana_inventory", "No has selecionado elementos a eliminar", "red")