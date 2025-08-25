from ui.floating_windows import verify
import dearpygui.dearpygui as dpg
from backend import backend
from utils import loader
import data

data_rows = []

def filter_rows(sender, app_data, user_data):
    if app_data:
        for d in data_rows:
            if app_data in d[1]:
                dpg.configure_item(d[0], show=True)
            else:
                dpg.configure_item(d[0], show=False)
    else:
        for d in data_rows:
            dpg.configure_item(d[0], show=True)

# Funcion que carga el contenido de la base de datos
def load():
    # Contiene la base de datos
    content = backend.obtener_inventario()
    # Obtiene el registro de imagenes
    data_imgs = data.user_data.get_imgs()
    # Variables que guardan la cantidad de estado
    buen_estado = 0
    mantenimiento = 0
    dado_baja = 0
    # Variable guarda la cantidad de elementos
    elements = {}

    # Funcion que elimina a los hijos de un contenedor
    def delete_children(parent_tag):
        children = dpg.get_item_children(parent_tag, 1)

        if children:
            for row in children:
                dpg.delete_item(row)

    # Se ejecuta la funcion en los diferentes contenedores para carga los datos
    delete_children("table_dashboard")
    delete_children("grafica_childwindow")
    delete_children("table_cantidad_elements")
    
    # Funcion que registra imagenes en dearpygui
    def image_register(id_image):
        img_dpg = None
        # Si La imagen ya esta registrada la toma de data.py, si no la registra y la guarda en data.py
        if id_image in data_imgs:
            img_dpg = data_imgs[id_image]
        else:
            data_register_img = backend.download_img_drive(c["IMAGEN"])
            img_dpg = loader.load_img_byte(data_register_img)
            data.user_data.add_imgs(id_image, img_dpg)

        return img_dpg

    # Bucle que recorre la base de datos
    for c in reversed(content):
        # Tag unico
        tag = dpg.generate_uuid()
        # Imagen registrada en dearpygui
        img_dpg = image_register(c["IMAGEN"])

        # Guarda registro de de las tablas de dashboard
        filtro_texto = f"{c['FECHA']} {c['NOMBRE']} {c['DESCRIPCION']} {c['SERIAL']} {c['UBICACION']} {c['ESTADO']}"
        data_rows.append([tag, filtro_texto])

        #Crea la tabla dashboard
        with dpg.table_row(parent="table_dashboard", label=filtro_texto, tag=tag):
            dpg.add_spacer(width=5)
            dpg.add_image(img_dpg, width=125, height=125)
            with dpg.table_cell():
                dpg.add_text(c["FECHA"])
                dpg.add_text(c["NOMBRE"])
                dpg.add_text(c["DESCRIPCION"])
                dpg.add_text(c["SERIAL"])
                dpg.add_text(c["UBICACION"])
            dpg.add_button(label=c["ESTADO"])

        # Guarda la cantidad de estados
        if "Buen estado" == c["ESTADO"]:
            buen_estado += 1
        elif "Mantenimiento" == c["ESTADO"]:
            mantenimiento += 1
        elif "Dado de baja" == c["ESTADO"]:
            dado_baja += 1

        # Guarda un diccionario con la cantidad de elementos existentes
        if c["NOMBRE"] in elements:
            elements[c["NOMBRE"]]["CANTIDAD"] += 1
        else:
            elements[c["NOMBRE"]] = {"IMAGEN": c["IMAGEN"], "CANTIDAD" : 1}
    
    # Genera la fila de cantidad de elementos
    for e in elements:
        img_dpg = image_register(elements[e]["IMAGEN"])

        with dpg.table_row(parent="table_cantidad_elements"):
                dpg.add_image(img_dpg, width=75, height=75)
                with dpg.table_cell():
                    dpg.add_spacer(height=10)
                    dpg.add_text(e)
                    dpg.add_text(f"Cantidad: {elements[e]["CANTIDAD"]}")

    with dpg.drawlist(width=250, height=150, parent="grafica_childwindow"):
        # Datos para la grafica
        valores = [buen_estado, mantenimiento, dado_baja]
        etiquetas = [str(v) for v in valores]
        colores = [(115, 228, 120, 255), (45, 129, 202, 255), (229, 61, 113, 255)]

        #Area disponible para las barras
        area = [(30,0),(220, 125)]
        #Ancho por barra
        ancho_barra = 30
        #Toma el valor maximo de la lista valores
        max_valor = max(valores)
        #Decide altura maxima
        altura_maxima = 125

        #Posicion x de las barras
        x_pos = area[0][0]
        #Se calcula el espacio entre todas las barras para asi centrarlas
        space = ((area[1][0] - area[0][0]) - (ancho_barra * len(valores))) / (len(valores) - 1)

        #Bucle que recorre las 3 listas y dibujas las barras
        for v, c, e in zip(valores, colores, etiquetas):
            #Toma el alto dependiendo de la altura_maxima
            altura = (v / max_valor) * altura_maxima

            #Posiciones para dibujar las barras
            x2_pos = x_pos + ancho_barra
            y1_pos = area[1][1] - altura
            y2_pos = area[1][1]

            #Dibuja la barra
            dpg.draw_rectangle((x_pos, y1_pos), (x2_pos, y2_pos),
                                                fill=c,
                                                color=(0, 0, 0, 0),
                                                rounding=8)

            #Agrega el texto de la cantidad
            dpg.draw_text((x_pos + 5, y2_pos + 8), e,
                                                size=20, color=(200, 200, 200, 255))

            #Calcula la proxima posicion
            x_pos = x2_pos + space

        #Línea base de la grafica
        dpg.draw_rectangle((10, 112), (240, 130), color=(0, 0, 0, 0), fill=(200, 200, 200, 255), rounding=8)

    dpg.set_value("txt_ctd_buen_estado", f"Cantidad: {buen_estado}")
    dpg.set_value("txt_ctd_mantenimiento", f"Cantidad: {mantenimiento}")
    dpg.set_value("txt_ctd_dado_baja", f"Cantidad: {dado_baja}")