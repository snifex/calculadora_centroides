from consolemenu import *
from consolemenu.items import *
from consolemenu import PromptUtils
from decimal import *
from Figura import *
from TipoFigura import *

figuras_array: list[Figura] = []

def main():
    global figuras_array

    # Create the menu
    menu = ConsoleMenu("Menú de calculo", "Selecciona la figura", exit_option_text="Salir del programa")

    #Creamos el menú de elipticas
    submenu_add_figures = ConsoleMenu("Agrega una forma", "Selecciona el tipo de forma")

    rectangle_item = FunctionItem("Rectangulo",input_handler, [TipoFigura.RECTANGULO.value])
    triangle_item = FunctionItem("Triangulo",input_handler, [TipoFigura.TRIANGULO.value])
    semi_circle_item = FunctionItem("Semi-circulo",input_handler, [TipoFigura.SEMI_CIRCUNFERENCIA.value])
    quarter_circle_item = FunctionItem("Cuarto de circunferencia", input_handler,[TipoFigura.CUARTO_CIRCUNFERENCIA.value])
    semi_elipse_item = FunctionItem("Semi-elipse", input_handler, [TipoFigura.SEMI_ELIPSE.value])
    quarter_elipse_item = FunctionItem("Cuarto de elipse",  input_handler, [TipoFigura.CUARTO_ELIPSE.value])
    parable_item = FunctionItem("Parabola", input_handler, [TipoFigura.PARABOLA.value])
    ejuta_item = FunctionItem("Ejuta", input_handler, [TipoFigura.EJUTA.value])

    #Agregamos las opciones al submenu
    submenu_add_figures.append_item(rectangle_item)
    submenu_add_figures.append_item(triangle_item)
    submenu_add_figures.append_item(semi_circle_item)
    submenu_add_figures.append_item(quarter_circle_item)
    submenu_add_figures.append_item(semi_elipse_item)
    submenu_add_figures.append_item(quarter_elipse_item)
    submenu_add_figures.append_item(parable_item)
    submenu_add_figures.append_item(ejuta_item)

    #Ya creado el menú hacemos una instancia de la que ira al menú principal
    item_menu_add_figure = SubmenuItem("Agrega una figura", submenu=submenu_add_figures)


    #Hacemos una lista de subemenu de cada opción
    submenu_perks_figures = [SelectionMenu([f"Base: {i.x_lado}", f"Altura: {i.y_lado}", i.tipo_figura, f"{i.get_area()}"], exit_option_text="Regresar a ver las figuras", title=i.tipo_figura) for i in figuras_array]

    submenu_figures_actual = [SubmenuItem(figure.tipo_figura,submenu = submenu_perks_figures[index]) for index,figure in enumerate(figuras_array)]
    #Creamos un menú con las formas que hay
    submenu_figures = ConsoleMenu("Figuras actuales")

    for i in submenu_figures_actual:
        submenu_figures.append_item(i)


    #Hacemos una opción donde nos muestre las figuras actuales
    actual_figures = SubmenuItem("Ver las figuras actuales", submenu=submenu_figures)

    #Agregamos al menú principal los menús creados
    menu.append_item(item_menu_add_figure)
    menu.append_item(actual_figures)
    # Mostramos el menú
    menu.show()

#TODO: Tratar de mostrar las figuras

def remove_epilogue_figures(menu):
    menu.epilogue_text = None

def add_epilogue_figures(menu):
    menu.epilogue_text = "No hay figuras aún"

def input_handler(tipo_figura: int):
    global figuras_array

    pu = PromptUtils(Screen())
    result_x = pu.input("Ingresa el valor de la base: ")
    result_y = pu.input("Ingresa el valor de la altura: ")
    
    #Obtenemos los valores
    result_input_x = float(result_x.input_string)
    result_input_y = float(result_y.input_string)

    #Creamos una instancia de Figura
    figura_temp = Figura(result_input_x, result_input_y, tipo_figura)
    figuras_array.append(figura_temp)

    pu.enter_to_continue()


if __name__ == "__main__":
    main()




# Primero metes una figura x
# Seleccionas que tipo de figura 
# Haces los calculos de los centroides
# Calculas los 