import dearpygui.dearpygui as dpg

def w_sin_conexion():
    with dpg.window(no_resize=True, no_collapse=True, no_title_bar=True, modal=True, no_move=True,
                    tag="w_sin_conexion",no_background=True):
        dpg.add_text("No tienes acceso a internet, Reinicia el programa.")