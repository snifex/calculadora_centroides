from consolemenu import *
from consolemenu.items import *
from consolemenu import PromptUtils
from mock import Mock
from decimal import *

def main():
    # Create the menu
    menu = ConsoleMenu("Menu de calculo", "Selecciona la figura")

    #Creamos los items del menú
    circular_forms_items = SelectionMenu(["Semi-elipse","Cuarto de elipse", "Parabola", "Ejuta/Acartelamiento"])
    
    semi_elipse_item = FunctionItem("Ingresa los datos por orden (eje y, lado a, lado): ", eliptical_forms, ["prompt.input"])

    circular_menu = SubmenuItem("Formas circulares",circular_forms_items, menu)

    prueba_item  = FunctionItem("Prueba texto", input_handler)

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command",  "dir")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu}
    menu.append_item(circular_menu)
    menu.append_item(prueba_item)
    menu.append_item(semi_elipse_item)


    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

def eliptical_forms(x: Decimal, y: Decimal, area: Decimal):
    pass    

def input_handler():
    pu = PromptUtils(Screen())
    result = pu.input("Ingresa los siguientes valores: 1,2,3")
    pu.println("Pusiste esto ei: ",result,"Ei: es de tipo ",type(result))
    pu.enter_to_continue()


if __name__ == "__main__":
    main()