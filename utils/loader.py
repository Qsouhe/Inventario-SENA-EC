import dearpygui.dearpygui as dpg

#Valor inicial de las variables de imagenes sin cargar
iconConfi = None
iconFlechaIz = None
icondashboard = None
icondashboard_active = None
iconinventory = None
iconinventory_active = None
iconusers = None
iconusers_active = None
iconchange = None
iconchange_active = None
iconuser = None
iconuser_active = None
iconexit = None
iconcheck = None
iconx = None
iconupload = None
iconload = None

#Valor inicial de las Fuentes de imagenes sin cargar
fuente_personalizada = None
fuente_boton = None
fuente_titulo = None
fuente_subtitulo_1 = None
fuente_subtitulo_2 = None

#Funcion que carga todas las imagenes y fuentes
def load():
    #Convierte las variables en global para asi poder cambiar las variables con valor inicial de None
    global iconConfi, iconFlechaIz, icondashboard, icondashboard_active, iconinventory, iconinventory_active 
    global iconusers, iconusers_active, iconchange, iconchange_active , iconexit, iconuser, iconuser_active
    global iconcheck, iconx, iconupload, iconload
    global fuente_personalizada, fuente_boton, fuente_titulo, fuente_subtitulo_1, fuente_subtitulo_2

    #--------------- toma los datos de cada imagen con su ruta ---------------
    width_iconConfi, height_iconConfi, _, data_iconConfi = dpg.load_image("recursos/imagenes/iconos/Configuracion.png")
    width_iconFlechaIz, height_iconFlechaIz, _, data_iconFlechaIz = dpg.load_image("recursos/imagenes/iconos/FlechaIzquierda.png")

    width_icondashboard, height_icondashboard, _, data_icondashboard = dpg.load_image("recursos/imagenes/iconos/dashboard.png")
    width_icondashboard_active, height_icondashboard_active, _, data_icondashboard_active = dpg.load_image("recursos/imagenes/iconos/dashboard_active.png")

    width_iconinventory, height_iconinventory, _, data_iconinventory = dpg.load_image("recursos/imagenes/iconos/inventory.png")
    width_iconinventory_active, height_iconinventory_active, _, data_iconinventory_active = dpg.load_image("recursos/imagenes/iconos/inventory_active.png")

    width_iconusers, height_iconusers, _, data_iconusers = dpg.load_image("recursos/imagenes/iconos/users.png")
    width_iconusers_active, height_iconusers_active, _, data_iconusers_active = dpg.load_image("recursos/imagenes/iconos/users_active.png")

    width_iconchange, height_iconchange, _, data_iconchange = dpg.load_image("recursos/imagenes/iconos/change.png")
    width_iconchange_active, height_iconchange_active, _, data_iconchange_active = dpg.load_image("recursos/imagenes/iconos/change_active.png")

    width_iconuser, height_iconuser, _, data_iconuser = dpg.load_image("recursos/imagenes/iconos/user.png")
    width_iconuser_active, height_iconuser_active, _, data_iconuser_active = dpg.load_image("recursos/imagenes/iconos/user_active.png")

    width_iconexit, height_iconexit, _, data_iconexit = dpg.load_image("recursos/imagenes/iconos/exit.png")

    width_iconcheck, height_iconcheck, _, data_iconcheck = dpg.load_image("recursos/imagenes/iconos/check.png")
    width_iconx, height_iconx, _, data_iconx = dpg.load_image("recursos/imagenes/iconos/x.png")

    width_iconupload, height_iconupload, _, data_iconupload = dpg.load_image("recursos/imagenes/upload.png")
    width_iconload, height_iconload, _, data_iconload = dpg.load_image("recursos/imagenes/iconos/load.png")

    #--------------- Se registra las imagenes en dearpygui ---------------
    with dpg.texture_registry(tag="registro_imagenes_inventory_EC"):
        #Cada variable cambia su valor inicial (None) por la imagen registrada
        iconConfi = dpg.add_static_texture(width_iconConfi, height_iconConfi, data_iconConfi)
        iconFlechaIz = dpg.add_static_texture(width_iconFlechaIz, height_iconFlechaIz, data_iconFlechaIz)

        icondashboard = dpg.add_static_texture(width_icondashboard, height_icondashboard, data_icondashboard)
        icondashboard_active = dpg.add_static_texture(width_icondashboard_active, height_icondashboard_active, data_icondashboard_active)

        iconinventory = dpg.add_static_texture(width_iconinventory, height_iconinventory, data_iconinventory)
        iconinventory_active = dpg.add_static_texture(width_iconinventory_active, height_iconinventory_active, data_iconinventory_active)

        iconusers = dpg.add_static_texture(width_iconusers, height_iconusers, data_iconusers)
        iconusers_active = dpg.add_static_texture(width_iconusers_active, height_iconusers_active, data_iconusers_active)

        iconchange = dpg.add_static_texture(width_iconchange, height_iconchange, data_iconchange)
        iconchange_active = dpg.add_static_texture(width_iconchange_active, height_iconchange_active, data_iconchange_active)

        iconuser = dpg.add_static_texture(width_iconuser, height_iconuser, data_iconuser)
        iconuser_active = dpg.add_static_texture(width_iconuser_active, height_iconuser_active, data_iconuser_active)

        iconexit = dpg.add_static_texture(width_iconexit, height_iconexit, data_iconexit)

        iconcheck = dpg.add_static_texture(width_iconcheck, height_iconcheck, data_iconcheck)
        iconx = dpg.add_static_texture(width_iconx, height_iconx, data_iconx)

        iconupload = dpg.add_static_texture(width_iconupload, height_iconupload, data_iconupload)
        iconload = dpg.add_static_texture(width_iconload, height_iconload, data_iconload)
    
    #--------------- Se registra las fuentes en dearpygui ---------------
    with dpg.font_registry(tag="registro_fuentes"):
        #Cada variable cambia su valor inicial (None) por la fuente registrada con su tamaño
        fuente_personalizada = dpg.add_font("recursos/fuentes/OpenSans-Regular.ttf", 20)
        fuente_titulo = dpg.add_font("recursos/fuentes/Oswald-Bold.ttf", 40)
        fuente_subtitulo_1 = dpg.add_font("recursos/fuentes/Oswald-Bold.ttf", 30)
        fuente_subtitulo_2 = dpg.add_font("recursos/fuentes/Oswald-Bold.ttf", 20)

def load_img_byte(data_register_img):
    with dpg.texture_registry():
        img = dpg.add_static_texture(data_register_img[0], data_register_img[1], data_register_img[2])
        return img