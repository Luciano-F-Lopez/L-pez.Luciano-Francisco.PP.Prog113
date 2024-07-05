from os import system
def pausar():
    system("pause")

def pantalla_limpia():
    system("cls")

def menu_00()->str:
    pantalla_limpia()
    print(" Menu de Opciones")
    print("1- Obtener nombre de cada Super Heroe")
    print("2- Obtener Nombre y Altura de cada Super Heroe")
    print("3- Obtener al SuperHeroe Mas Alto")
    print("4- Obtener al SuperHeroe Mas bajo")
    print("5- Obtener la Altura Promedio de todos los SuperHeroes")
    print("6- Obtener el nombre Del SuperHeroes Mas Alto y Mas bajo")
    print("7- Obtener Al SuperHeroe Mas y Menos Pesado")
    print("8- Salir")
    opcion = input("Ingrese opcion: ")
    return opcion


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



def saludar():
    print("Buenos dias")

def brindar():
    print("Chin,chin....")

def despedir():
    print("Hasta Luego")

#---------------------------------------------------

