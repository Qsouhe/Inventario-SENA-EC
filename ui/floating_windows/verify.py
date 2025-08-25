import dearpygui.dearpygui as dpg
from typing import Literal

active_verify_tags = set()  # Para rastrear widgets existentes

def animar_opacidad(item, color, start_alpha, end_alpha, duration=1.0, steps=60, on_finish=None):
    delay_frames = int(duration * 60 / steps)
    delta_alpha = (end_alpha - start_alpha) / steps

    r, g, b = (0, 0, 0)
    r_t, g_t, b_t = (255, 255, 255)

    if color == "red":
        r, g, b = (255, 61, 113)
    elif color == "green":
        r, g, b = (115, 228, 120)
    elif color == "white":
        r, g, b = (255, 255, 255)
        r_t, g_t, b_t = (0, 0, 0)

    def step_anim(step=0):
        if not dpg.does_item_exist(item):
            return

        if step > steps:
            if on_finish:
                on_finish()
            return

        alpha = max(0, min(1, start_alpha + delta_alpha * step))

        # Limpiar temas anteriores para evitar acumulación
        current_theme = dpg.get_item_theme(item)
        if current_theme:
            dpg.delete_item(current_theme, children_only=True)

        with dpg.theme() as temp_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (r, g, b, int(255 * alpha)))
                dpg.add_theme_color(dpg.mvThemeCol_Text, (r_t, g_t, b_t, int(255 * alpha)))
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 8)
                dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

        dpg.bind_item_theme(item, temp_theme)

        dpg.set_frame_callback( dpg.get_frame_count() + delay_frames,
                                lambda: step_anim(step + 1))

    step_anim()


def verify(tag_window, label: str, color: Literal["red", "green", "white"]):
    # Eliminar widgets antiguos
    for t in list(active_verify_tags):
        if dpg.does_item_exist(t):
            dpg.delete_item(t)
        active_verify_tags.discard(t)

    tag = dpg.generate_uuid()
    active_verify_tags.add(tag)

    with dpg.child_window(auto_resize_x=True, auto_resize_y=True, tag=tag, pos=(10, 10), parent=tag_window):
        with dpg.group(horizontal=True):
            dpg.add_text(label, indent=20)
            dpg.add_spacer(width=15)

    # Fade in -> espera -> fade out -> eliminar
    animar_opacidad(tag, color, 0, 1, duration=1.0, steps=60,
        on_finish=lambda: dpg.set_frame_callback(
            dpg.get_frame_count() + int(2 * 60),
            lambda: animar_opacidad(tag, color, 1, 0, duration=1.0, steps=60,
                                    on_finish=lambda: [dpg.delete_item(tag), active_verify_tags.discard(tag)])
        )
    )
