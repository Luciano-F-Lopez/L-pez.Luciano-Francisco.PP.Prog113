def duplicar (numero:int)->int:
    """duplicar

    Args:
        numero (int): pasamos el numero a duplicar

    Returns:
        int: nos retorna el numero duplicado
    """
    numero = numero * 2
    return numero
    
#-------------------------------------------------------------------------------------

def duplicar_valores(listas:list)->None:
    """duplicar_valores

    Args:
        listas (list): pasamos la lista a duplicar
    """
    for i in range(len(listas)):
        listas [i] = listas [ i] * 2

#-------------------------------------------------------------------------------------


def mostrar_lista(lista:list)->None:
    """mostrar_lista

    Args:
        lista (list): pasamos la lista que queremos mostrar
    """
    for el in lista:
        print(el,end=" ")
    print()

#-------------------------------------------------------------------------------------


def cargar_lista_enteros_random(lista:list, cant:int, desde:int, hasta:int)->None:
    """cargar_lista_enteros_random

    Args:
        lista (list): pasamos lista para meter los numeros random 
        cant (int): pasamos la cantidad que queremos de numeros random 
        desde (int): pasamos desde cuando queremos que arranque 
        hasta (int): pasamos hasta donde queremos que llegue 
    """
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))

#-------------------------------------------------------------------------------------


def crear_lista_enteros_random(cant:int, desde:int, hasta:int)->list:
    """crear_lista_enteros_random

    Args:
        cant (int): pasamos la cantidad que queremos de numeros random
        desde (int): pasamos desde cuando queremos que arranque
        hasta (int): pasamos hasta donde queremos que llegue

    Returns:
        list: retorna una lista de enteros random 
    """
    from random import randint
    lista = [ ]
    for _ in range(cant):
        lista.append(randint(desde, hasta))  
    return lista

#-------------------------------------------------------------------------------------


def totalizar_listas(lista:list)->int:
    """totalizar_listas

    Args:
        lista (list): pasamos la lista a totalizar

    Returns:
        int: nos devuelve  el total de la lista
    """
    total = 0
    for numero in lista:
        total += numero
    return total

#-------------------------------------------------------------------------------------

def calcular_promedio_3_lista(lista:list)->float:
    """calcular_promedio_3_lista

    Args:
        lista (list): pasamos la lista para calcular promedio 

    Raises:
        ValueError: nos tira error si la lista esta vacia 

    Returns:
        float: retorna el promedio de la lista
    """
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_listas(lista) / cant

#-------------------------------------------------------------------------------------
def calcular_mayor(lista:list)->int:
    """calcular_mayor

    Args:
        lista (list): lista para clacular el mayor

    Raises:
        ValueError: si la lista esta vacia tira error

    Returns:
        int: retorna el mayor de la lista
    """

    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero > num_mayor :
            num_mayor = numero
            flag = True
    return num_mayor

#------------------------------------------------------------------------------------
def calcular_menor(lista:list)->int:
    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero < num_menor :
            num_menor = numero
            flag = True
    return num_menor


#-----------------------------------------------------------------------------------
def buscar_in_lista(lista:list, target:int)->int:
    """buscar_in_lista

    Args:
        lista (list): pasamos la lista en la que queremos buscar algo
        target (int): elegimos el target a buscar

    Returns:
        int: nos retorna cuantas veces esta 
    """
    indice = -1

    for i in range(len(lista)):
        if lista[i] == target:
            indice = i
            break
    return indice
            

#busca el elemento y te dice en que posicion esta, sino esta posicion es -1 (ver como lo hacen en clase)
#-----------------------------------------------------------------------------------
def contar_in_lista(lista:list, target:int)->int:
    contador_elemento = 0
    for numero in lista:
        if numero == target:
            contador_elemento+= 1
    return contador_elemento
#busca el elemento y te dice cuantas veces esta

#-----------------------------------------------------------------------------------
def ordenar_listas_ascendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def ordenar_listas_descendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#----------------------------------------------------------------------------------
def menu_listas()->str:
    print(" Menu de Opciones")
    print("1- Ascendente")
    print("2- descendente")
    opcion = input("Ingrese opcion: ")
    return opcion
#-----------------------------------------------------------------------------------

def ordenar_lista_A_D(lista:list)->None:
    match menu_listas():
        case "1":
            ordenar_listas_ascendente(lista)        
        case "2":
            ordenar_listas_descendente(lista)
    return lista

def ordenar_lista_A_D2(lista:list, asc:bool = True)->None:
        tam = len(lista)
        if asc:
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] > lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux       
        else:
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] < lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

        return lista

            



#Nosotros elegimos como lo queremos ordenar de manera ascendente / descendente 

            
    





