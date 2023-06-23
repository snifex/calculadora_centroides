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
    submenu_add_figures = ConsoleMenu("Agrega una forma", "Selecciona el tipo de forma", exit_option_text="Regresar al menú principal")

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

    #Hacemos una opción donde nos muestre las figuras actuales
    actual_figures = FunctionItem("Ver las figuras actuales", print_actual_figures)

    #Agregamos al menú principal los menús creados
    menu.append_item(item_menu_add_figure)
    menu.append_item(actual_figures)

    # Mostramos el menú
    menu.show()

def print_actual_figures() -> None:
    global figuras_array

    pu = PromptUtils(Screen())

    if len(figuras_array) == 0:
        pu.println("No hay figuras aún")
    else:
        for i in figuras_array:
            pu.println(f"Tipo de figura: {i.tipo_figura}\n  Base: {i.x_lado}\n  Altura: {i.y_lado}\n  Area={i.get_area()}\n  Centroide= {i.get_centroide()}\n")

    pu.enter_to_continue()

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
