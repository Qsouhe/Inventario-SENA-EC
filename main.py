from ui import login, dashboard, user, inventory
import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg
from utils import loader, themes
import dearpygui.demo as demo
from backend import backend
from ui.floating_windows import append

def main():
    dpg.create_context()
    dpg.create_viewport()
    dpg.set_viewport_resizable(False)
    dpg_sqs.clear_data()

    #Ejecuta la validacion del backend
    backend.get_drive_service()

    #Carga las imagenes, las fuentes y los temas
    loader.load()
    themes.load_themes()

    #Agrega una fuente por defecto para todos
    dpg.bind_font(loader.fuente_personalizada)

    #Ejecuta la ventana de login
    login.login_window()
    login.execute_styleqs()

    #Ejecuta de manera interna la estructura de todo lo demas
    user.user_window()

    dashboard.dashboard_window()
    inventory.inventory_window()

    dpg.bind_theme(themes.themes["global_tema"])

    """
    dpg.show_style_editor()
    demo.show_demo()
    dpg.show_item_registry()
    dpg.show_metrics()
    dpg.show_documentation()
    dpg.show_debug()
    dpg.show_about()
    dpg.show_font_manager()
    """

    dpg.set_viewport_title("Inventario Economia Circulas - SENA Centro de gestion industrial")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()