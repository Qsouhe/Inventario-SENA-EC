import dearpygui.dearpygui as dpg
from backend import backend
from utils import loader
from ui.floating_windows import verify
import data

def show_data():
    img = None
    content = backend.obtener_usuario()
    data_imgs = data.user_data.get_imgs()
    for c in content:
        if data.user_data.get_id() == c["ID"]:
            img = c["IMAGEN"]
            dpg.configure_item("btn_alias", label=c["ALIAS"])
            dpg.configure_item("btn_nombre_apellido", label=c["NOMBRES Y APELLIDOS"])
            dpg.configure_item("btn_numero_telefonico", label=c["NUMERO TELEFONICO"])
            dpg.configure_item("btn_correo_institucional", label=c["CORREO INSTITUCIONAL"])
    
    if img in data_imgs:
        pass
    else:
        data_register_img = backend.download_img_drive(img)
        img_dpg = loader.load_img_byte(data_register_img)

        data.user_data.add_imgs(img, img_dpg)

        dpg.configure_item("img_user", texture_tag=img_dpg)

def load():
    content = backend.obtener_usuario()
    children = dpg.get_item_children("table_users", 1)

    if children:
        for row in children:
            dpg.delete_item(row)

    for c in reversed(content):
        data_imgs = data.user_data.get_imgs()
        img = c["IMAGEN"]
        img_dpg = None

        if img in data_imgs:
            img_dpg = data_imgs[img]
        else:
            data_register_img = backend.download_img_drive(c["IMAGEN"])
            img_dpg = loader.load_img_byte(data_register_img)
            data.user_data.add_imgs(img, img_dpg)

        if not data.user_data.get_id() == c["ID"]:
            with dpg.table_row(parent="table_users"):
                dpg.add_spacer(width=5)
                dpg.add_image(img_dpg, width=125, height=125)
                with dpg.table_cell():
                    dpg.add_text(c["ALIAS"])
                    dpg.add_text(c["NOMBRES Y APELLIDOS"])
                    dpg.add_text(c["NUMERO TELEFONICO"])
                    dpg.add_text(c["CORREO INSTITUCIONAL"])
                dpg.add_spacer(width=5)