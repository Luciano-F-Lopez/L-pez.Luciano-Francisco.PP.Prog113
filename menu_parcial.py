from os import system
def pausar():
    system("pause")

def pantalla_limpia():
    system("cls")


def menu_01()->str:
    pantalla_limpia()
    print(" Menu de Opciones")
    print("1- Cargar archivo")
    print("2- imprimir lista")
    print("3- asignar estadisticas")
    print("4- filtrar por mejores posts ")
    print("5- filtrar por haters")
    print("6- informar promedio de followers")
    print("7- ordenar los datos ppor nombre de user ascendente")
    print("8- Mostrar mas popular")
    print("9- salir")
    opcion = input("Ingrese opcion: ")
    return opcion



#---------------------------------------------------

