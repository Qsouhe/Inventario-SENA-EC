from events import inventory_events, users_events, dashboard_events
from ui import dashboard, login, user, inventory
import dearpygui.dearpygui as dpg
from typing import Literal

#--------------- Funcion que cambia las ventanas ---------------
def window_change(tag_primary: str, ventana: Literal["login", "user", "dashboard", "inventory"]):
    """
    ================== EXPLICACION ==================
    se ejecuta al llamar la dependiendo de la opcion de ventana
    def ventana():
        dpg.hide_item(tag_primary)  <-------------------- Oculta la ventana actual
        dpg.show_item("ventana_0")  <-------------------- Muestra la ventana_0 es decir cualquiera que se eliga
        dpg.set_primary_window("ventana_0", True)   <---- Convierte la ventana_0 a primary window, para que cubra toda la pantalla
    """
    #--------------- ventana login (principal) ---------------
    def login_window():
        dpg.hide_item(tag_primary)
        dpg.show_item("ventana_validacion")
        dpg.set_primary_window("ventana_validacion", True)

    #--------------- ventana user ---------------
    def user_window():
        print("cambiando a ventana user")
        dpg.hide_item(tag_primary)
        dpg.show_item("ventana_user")
        dpg.set_primary_window("ventana_user", True)

        if user.loader_styleqs == False:
            user.loader_styleqs = True
            user.execute_styleqs()
        else:
            users_events.load()

    #--------------- ventana dashboard ---------------
    def dashboard_window():
        print("cambiando a ventana dashboard")
        dpg.hide_item(tag_primary)
        dpg.show_item("ventana_dashboard")
        dpg.set_primary_window("ventana_dashboard", True)

        if dashboard.loader_styleqs == False:
            dashboard.loader_styleqs = True
            dashboard.execute_styleqs()
        else:
            dashboard_events.load()
    
    #--------------- ventana inventory ---------------
    def inventory_window():
        print("cambiando a ventana inventory")
        dpg.hide_item(tag_primary)
        dpg.show_item("ventana_inventory")
        dpg.set_primary_window("ventana_inventory", True)

        if inventory.loader_styleqs == False:
            inventory.loader_styleqs = True
            inventory.execute_styleqs()
        else:
            inventory_events.load()

    #Elige cual funcion ejecutar dependiendo del valor de ventana
    match ventana:
        case "login":
            login_window()
        case "user":
            user_window()
        case "dashboard":
            dashboard_window()
        case "inventory":
            inventory_window()