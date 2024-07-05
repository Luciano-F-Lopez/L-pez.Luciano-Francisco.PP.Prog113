from funciones_listas_parcial import *
from math import *
from random import randint
import csv
import json
import os 


def calcular_promedio_enteros(a:int,b:int)->float:
    """calcular_promedio_enteros 

    Args:
        a (int): paso el primer entero 
        b (int): paso el segundo entero

    Raises:
        TypeError: si no es una lista nos tira un error 

    Returns:
        float: devuelve el resultdo del promedio 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")

    ai = int(a)
    bi = int(b)
    return (ai + bi) / 2

#------------------------------------------------------------------------------------------------------------------------

def promediar_listas(lista:list)->None:
    """promediras_listas

    Args:
        lista (list): pasamos la lista

    Raises:
        TypeError: si no es una lista nos tira un error
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    nota_1 = 3
    nota_2 = 4
    promedio = 5 
    tam = len(lista)
    for i in range(tam):
        promedios =  ((lista[i][nota_1] + lista[i][nota_2] / 2))
        lista[i][promedio] = promedios

def swap_lista(lista:list, i:int, j: int)->None:
    aux =lista[i]
    lista[i] = lista[j]
    lista[j] = aux

    
    

#------------------------------------------------------------------------------------------------------------------------

lista = [3,213,21,3,43,24,325,43,5]

def mapear_list(funcion,lista:list)->list:          #funcion que hace mas facil el mapeo de una lista y devuelve una modificacion de lo que habia 
    """mapear_list

    Args:
        funcion (_type_): pasamos una funcion de lo que queremos que saque de la lista
        lista (list[dict]): pasamos la lista origina

    Raises:
        TypeError: si no es una lista nos tira un error 

    Returns:
        list: retorna una lista con el mapeo que le pedimos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


#empleados = []

#lista_destino = mapear_list(lambda emp: (emp["nombre"],emp["sector"], empleados)) #como utilizar la funcion del mapeo de lista simplificada
#lista_destino = mapear_list(lambda emp: (emp["edad"]))
#lista_destino = mapear_list(lambda emp: (emp["genero"]))
#lista_destino = mapear_list(lambda emp: (emp["nombre"],emp["apellido"], empleados))

#Con las siguientes funciones mantenemos la lista original remplazando solo el valor que queremos

#------------------------------------------------------------------------------------------------------------------------

#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")  #asi se usa la funcion anterior 
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")


def filtrar_listas(funcion,lista:list)->list:                       #sirve para filtrar cualquier lista con cualquier valor
    """filtrar_listas

    Args:
        funcion (_type_): ponemos lo que queramos que filtre nuestra funcion
        lista (list): pasamos la lista original
    Raises:
        TypeError: si no es una lista nos tira un error
        
    Returns:
        list: retorna la lista filtreada 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        if funcion(el): 
            lista_retorno.append((el))
    return lista_retorno

#empleadas = filtrar_listas(lambda emp: emp["genero"] == "f",empleados)      #asi se usa la funcion anterior que es la mejor y mas completa con lambda 
#empleados = filtrar_listas(lambda emp: emp["genero"] == "m",empleados)
#empleados_lanus = filtrar_listas(lambda emp: emp["genero"] == "m" and emp["localidad"] == "lanus",empleados) #fijarse bien como esta escrito por que sino tira error

#------------------------------------------------------------------------------------------------------------------------


def mayor_lista(lista:list)->int:
    """mayor_lista

    Args:
        lista (list): pasamos la lista original

    Raises:
        TypeError: si no es una lista nos tira un error

    Returns:
        int: nos devuelve el mayor de la lista que pasamos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mayor = lista[0]
    for el in lista[1: ]:
        if mayor < el:
            mayor = el 
    return mayor
    
#------------------------------------------------------------------------------------------------------------------------



def menor_lista(lista:list)->int:
    """menor_lista

    Args:
        lista (list): pasamos la lista original

    Raises:
        TypeError: si no es una lista nos tira un error

    Returns:
        int: retorna el menor de la lista que pasamos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    menor = lista[0]
    for el in lista[1: ]:
        if menor > el:
            menor = el
    return menor

#------------------------------------------------------------------------------------------------------------------------



def get_path_actual(nombre_archivo):
    """get_path_actual

    Args:
        nombre_archivo (_type_): ponemos el nombre que queremos que tenga 

    Returns:
        _type_: no devuelve nada
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual,nombre_archivo)
#------------------------------------------------------------------------------------------------------------------------


def leer_archivo_csv(nombre_archivo_csv:str)->list:
    """leer_archivo_csv

    Args:
        nombre_archivo_csv (str): le pasamos el nombre del archivo csv

    Returns:
        list: nos devuelve una lista con el contenidos del archivo que le pasamos
    """
    try:
        with open(get_path_actual(nombre_archivo_csv),"r",encoding="utf-8") as archivo: 
            lista = []
            encabezado = archivo.readline().strip("\n").split(",")

            for linea in archivo.readlines():
                persona = {}
                linea = linea.strip("\n").split(",")

                id,user,likes,dislikes,followers = linea
                persona["id"] = int(id)
                persona["user"] = (user)
                persona["likes"] = int(likes)
                persona["dislikes"] = int(dislikes)
                persona["followers"] = int(followers)
                lista.append(persona)
        print(f"El archivo {nombre_archivo_csv} ha sido cargado exitosamente.")
        return lista
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []


def guardar_archivo_csv(lista:list,nombre_archivo_csv)->any:
    """guardar_archivo_csv

    Args:
        lista (list): paso una lista
        nombre_archivo_csv (_type_): el nombre del archivo que quiero ponerle 
    
    Raises:
        TypeError: si no es una lista nos tira un error

    Returns:
        any: no devuelve nada
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    with open(get_path_actual(nombre_archivo_csv), "w", encoding="utf-8") as archivo: #hace lo mismo que el anterior pero aca pasa el nombre a mayusculas
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)

            linea = ",".join(l) + "\n"
            archivo.write(linea)

#------------------------------------------------------------------------------------------------------------------------
    
def tomar_ruta_actual(archivo):
    """tomar_ruta_actual

    Args:
        archivo (_type_): pasamos el archivo del que queremos saber su ruta

    Returns:
        _type_: nos devuelve la ruta del archivo 
    """
    ruta_actual = os.path.dirname(__file__)
    return os.path.join(ruta_actual, archivo)

#------------------------------------------------------------------------------------------------------------------------

def leer_archivo_json(archivo_json:str):
    """leer_archivo_json

    Args:
        archivo_json (str): pasamos el archivo a leer

    Returns:
        _type_: devuelve una lista con los datos listos para usar 
    """
    with open(get_path_actual(archivo_json),"r",encoding="utf-8") as archivo: # ya podemos usar los datos del.json
        lista = json.load(archivo)
        return lista

    
def guardar_archivo_json(archivo_json, lista):
    with open(tomar_ruta_actual(archivo_json), "w", encoding="utf-8") as archivo_json:
        return json.dump(lista, archivo_json, indent = 4)


#------------------------------------------------------------------------------------------------------------------------
def cambiar_likes_random(lista:list)->list:
    """cambiar_likes_random

    Args:
        lista (list): pasamos la lista 

    Raises:
        TypeError: si no es una lista nos tira un error 

    Returns:
        list: devuelve la lista con los likes randoms
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(500, 3000)
        lista[i]["likes"] = lista_tiempo    
    return lista
#------------------------------------------------------------------------------------------------------------------------
def cambiar_dislikes_random(lista:list)->list:
    """cambiar_dislikes_random

    Args:
        lista (list): pasamos la lista

    Raises:
        TypeError: si no es una lista nos tira un error 

    Returns:
        list: devuelve la lista con los dislikes random
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(300, 3500)
        lista[i]["dislikes"] = lista_tiempo    
    return lista

#------------------------------------------------------------------------------------------------------------------------
def cambiar_followers_random(lista:list)->list:
    """cambiar_followers_random

    Args:
        lista (list): pasamos la lista 

    Raises:
        TypeError: si no es una lista nos tira un error

    Returns:
        list: nos devuelve la lista con los followers random 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(10000, 20000)
        lista[i]["followers"] = lista_tiempo    
    return lista


#------------------------------------------------------------------------------------------------------------------------


def ordenar_ascendente_por_nombre_user(lista):
    """ordenar_ascendente_por_nombre

    Args:
        lista (_type_): pasamos la lista a ordenar

    Raises:
        TypeError: si no es una lista nos tira un error

    Returns:
        _type_: devuelve la lista ordenada de forma ascendente 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['user'] < lista[min_idx]['user']:
                min_idx = j
        # Intercambiar elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista




def post_mas_likeado(lista:list)->str:
    """post_mas_likeado

    Args:
        lista (list): pasamos la lista

    Raises:
        TypeError: si no es una lista nos tira un error 

    Returns:
        str: devuelve el post_mas_likeado
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")

    nombre_likes = mapear_list(lambda likesynombre: (likesynombre["likes"],likesynombre["user"]),lista)
    ganador = calcular_mayor(nombre_likes)
    mensaje = f"el user con mas likes es  {ganador[1]} y la cantidad de likes son: {ganador[0]}"
    return mensaje


#para terminar  Luciano López: git init
# Luciano López: git add .
# Luciano López: git commit -m "mensaje"
# Luciano López: y lo que despues te dice el coso de git en el repo
            