import dearpygui.dearpygui as dpg

#--------------- Funcion de posicionamiento para el boton exit ---------------
def posicionamiento_exit(tag_button):
        posicion = dpg.get_item_pos(tag_button)
        x = posicion[0]
        y = posicion[1] - 10
        dpg.set_item_pos(tag_button, pos=(x, y))

def size_input_automatic_right(tag_input, tag_container):
        pos_input = dpg.get_item_pos(tag_input)
        width_container, _ = dpg.get_item_rect_size(tag_container)

        width_enable = width_container - pos_input[0]
        dpg.set_item_width(tag_input, width=width_enable)