import dearpygui.dearpygui as dpg

def layout_dashboard():
    size_options = dpg.get_item_rect_size("opciones")
    size_btn_exit = dpg.get_item_rect_size("btn_exit_dashboard")
    pos_btn_exit = dpg.get_item_pos("btn_exit_dashboard")

    if size_options[1] <= size_btn_exit[1] + pos_btn_exit[1]:
        dpg.set_item_pos("btn_exit_dashboard", (pos_btn_exit[0], (size_options[1] - size_btn_exit[1]) - 10))