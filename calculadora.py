from consolemenu import *
from consolemenu.items import *
from consolemenu import PromptUtils
from mock import Mock
from decimal import *

def main():
    # Create the menu
    menu = ConsoleMenu("Menú de calculo", "Selecciona la figura")

    #Creamos el menú de elipticas
    submenu_internal_elipses = ConsoleMenu("Formas elipsicas", "Selecciona una forma")

    semi_elipse_item = FunctionItem("Semi-elipse", input_handler)
    quarter_elipse_item = FunctionItem("Cuarto de elipse", input_handler)
    parable_item = FunctionItem("Parabola", input_handler)
    ejuta_item = FunctionItem("Ejuta", input_handler)

    submenu_internal_elipses.append_item(semi_elipse_item)
    submenu_internal_elipses.append_item(quarter_elipse_item)
    submenu_internal_elipses.append_item(parable_item)
    submenu_internal_elipses.append_item(ejuta_item)

    #Ya creado el menú hacemos una instancia de la que ira al menú principal
    submenu_principal_elipses = SubmenuItem("Formas circulares", submenu=submenu_internal_elipses)

    #Agregamos al menú principal los menús creados
    menu.append_item(submenu_principal_elipses)


    # Mostramos el menú
    menu.show()

def eliptical_forms(x: Decimal, y: Decimal, area: Decimal):
    pass

def input_handler():
    pu = PromptUtils(Screen())
    result = pu.input("Ingresa los valores (y)")
    pu.println("Pusiste esto ei: ",result,"Ei: es de tipo ",type(result))
    pu.enter_to_continue()


if __name__ == "__main__":
    main()