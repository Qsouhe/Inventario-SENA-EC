import dpg_styleqs.dpg_styleqs as dpg_sqs
import dearpygui.dearpygui as dpg

#Diccionario que alamacena cada tema
themes = {}

def load_themes():
    with dpg.theme() as global_tema:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0)

    themes["global_tema"] = global_tema

    #--------------- Tema de los formularios de login ---------------
    with dpg.theme() as formularios:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 0))

        with dpg.theme_component(dpg.mvText):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))

        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)


        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 75, 105, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["formularios"] = formularios

    #--------------- Tema de los inputs incorrectos ---------------
    with dpg.theme() as incorrect_input:
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)

    themes["incorrect_input"] = incorrect_input

    with dpg.theme() as neutral_input:
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)

    themes["neutral_input"] = neutral_input

    #--------------- Tema de los formularios de login utilizando dpg_styleqs ---------------
    with dpg_sqs.ThemeWidgets("mvChildWindow") as formulario_styleqs:
        formulario_styleqs.add_background_color(color=(255, 255, 255), 
                                                rounded_corners=12)
        formulario_styleqs.add_shadow(pos=(0,8), opacity=0.25)

    themes["formulario_styleqs"] = formulario_styleqs.tag

    #--------------- Tema de fondo gradiante sin redondear esquinas ---------------
    with dpg_sqs.ThemeWidgets("mvChildWindow") as fondo_gradiant:
        fondo_gradiant.add_background_gradiant( gradiant_type="Lineal_vertical",
                                                    start_color=(115, 255, 120),
                                                    end_color=(45, 75, 125))

    themes["fondo_gradiant"] = fondo_gradiant.tag

    #--------------- Tema de fondo gradiante redondeando esquinas (se utiliza en algunos contenedores) ---------------
    with dpg_sqs.ThemeWidgets("mvChildWindow") as fondo_gradiant_contenedores:
        fondo_gradiant_contenedores.add_background_gradiant( gradiant_type="Lineal_vertical",
                                                    start_color=(115, 255, 120),
                                                    end_color=(45, 75, 125),
                                                    rounded_corners=12)

    themes["fondo_gradiant_contenedores"] = fondo_gradiant_contenedores.tag

    #--------------- Tema gris para las ventanas ---------------
    with dpg.theme() as fondo_home:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (230, 230, 230, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
    
    themes["fondo_home"] = fondo_home

    #--------------- Tema claro para los contenedores ---------------
    with dpg.theme() as fondo_contenedores:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)

    themes["fondo_contenedores"] = fondo_contenedores

    #--------------- Tema que quita el fondo a los contenedores(childWindow) ---------------
    with dpg.theme() as childwindow_no_background:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0)
    
    themes["childwindow_no_background"] = childwindow_no_background

    #--------------- Tema de los image button ---------------
    with dpg.theme() as boton_img_sin_fondo:
        with dpg.theme_component(dpg.mvImageButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))
    
    themes["boton_img_sin_fondo"] = boton_img_sin_fondo

    #--------------- Tema de los inputs de busqueda ---------------
    with dpg.theme() as buscador:
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
    
    themes["buscador"] = buscador

    #--------------- Tema de los combo ---------------
    with dpg.theme() as combo:
        with dpg.theme_component(dpg.mvCombo):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (245, 245, 245, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)

            dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (245, 245, 245, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (245, 245, 245, 255))

            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 1)

            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (245, 245, 245, 255))

    themes["combo"] = combo

    #--------------- Sombreado para los widgets de imagenes ---------------
    with dpg_sqs.ThemeWidgets("mvImage") as imagen_sombreado:
        imagen_sombreado.add_shadow(pos=(0,8), opacity=0.25)

    themes["imagen_sombreado"] = imagen_sombreado.tag

    #--------------- texto con fondo verde (realmente es un boton disfrazado) ---------------
    with dpg.theme() as estado_verde:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5)
    
    themes["estado_verde"] = estado_verde
#home
    #--------------- texto con fondo azul (realmente es un boton disfrazado) ---------------
    with dpg.theme() as estado_azul:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 129, 202, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (45, 129, 202, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (45, 129, 202, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5)

    themes["estado_azul"] = estado_azul

    #--------------- texto con fondo rojo (realmente es un boton disfrazado) ---------------
    with dpg.theme() as estado_rojo:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (229, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (229, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (229, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5)
    
    themes["estado_rojo"] = estado_rojo

    #--------------- Tema para los inputs en general ---------------
    with dpg.theme() as inputs:
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)
    
    themes["inputs"] = inputs

    #--------------- Tema de boton verde ---------------
    with dpg.theme() as btn_verde:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["btn_verde"] = btn_verde

    #--------------- Tema de boton azul ---------------
    with dpg.theme() as btn_azul:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 75, 125, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["btn_azul"] = btn_azul

    #--------------- Tema de boton rojo ---------------
    with dpg.theme() as btn_rojo:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["btn_rojo"] = btn_rojo

    #--------------- Tema de boton gris ---------------
    with dpg.theme() as btn_gris_activo:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (225, 225, 225, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
    
    themes["btn_gris_activo"] = btn_gris_activo

    #--------------- Tema de boton gris ---------------
    with dpg.theme() as btn_gris:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (225, 225, 225, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (225, 225, 225, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (225, 225, 225, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
    
    themes["btn_gris"] = btn_gris

    #--------------- Tema de boton transparente claro ---------------
    with dpg.theme() as btn_transparente_claro:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (255, 255, 255, 25))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 255, 255, 25))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15 , 5)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
    
    themes["btn_transparente_claro"] = btn_transparente_claro

    #--------------- Tema claro para los contenedores ---------------
    with dpg.theme() as fondo_contenedor_inventory:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)

    themes["fondo_contenedor_inventory"] = fondo_contenedor_inventory

    #--------------- Tema Tabla Inventario ---------------
    with dpg.theme() as tema_tabla_inventory:
        with dpg.theme_component(dpg.mvTable):
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (227, 250, 230, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 15, 8)

        with dpg.theme_component(dpg.mvTableColumn, enabled_state=True):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))

        with dpg.theme_component(dpg.mvCheckbox):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (45, 75, 125, 255))
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255, 255))

    themes["tema_tabla_inventory"] = tema_tabla_inventory

    #--------------- Tema Tabla Inventario ---------------
    with dpg.theme() as tema_tabla_claro:
        with dpg.theme_component(dpg.mvTable):
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (255, 255, 255, 50))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (255, 255, 255, 25))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 15, 8)

        with dpg.theme_component(dpg.mvTableColumn, enabled_state=True):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))

        with dpg.theme_component(dpg.mvText):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))

    themes["tema_tabla_claro"] = tema_tabla_claro

    with dpg.theme() as tema_tabla_alt_gris:
        with dpg.theme_component(dpg.mvTable):
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (245, 245, 245, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 15, 8)

        with dpg.theme_component(dpg.mvTableColumn, enabled_state=True):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))

        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8 ,2)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["tema_tabla_alt_gris"] = tema_tabla_alt_gris

    #--------------- Tema ventana verify ---------------
    with dpg.theme() as ventana_verify_good:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (115, 228, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 1)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)

    themes["ventana_verify_good"] = ventana_verify_good
    with dpg.theme() as ventana_verify_bad:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255, 61, 113, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 1)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)

    themes["ventana_verify_bad"] = ventana_verify_bad

    with dpg.theme() as ventana_append:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (255,255,255,255))

        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)
        
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 75, 125, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)

        with dpg.theme_component(dpg.mvCombo):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (230, 230, 230, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (245, 245, 245, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)

            dpg.add_theme_color(dpg.mvThemeCol_Button, (230, 230, 230, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (245, 245, 245, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (245, 245, 245, 255))

            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 1)

            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (245, 245, 245, 255))
        
        with dpg.theme_component(dpg.mvDragInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (230, 230, 230, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["ventana_append"] = ventana_append

    with dpg.theme() as ventana_delete:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (255,255,255,255))
        
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (225, 225, 225, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 25 ,10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    themes["ventana_delete"] = ventana_delete

    with dpg.theme() as fondo_gris_childwindow:
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (230, 230, 230, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10)
    
    themes["fondo_gris_childwindow"] = fondo_gris_childwindow