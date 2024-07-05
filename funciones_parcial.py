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

    Returns:
        float: devuelve el resultdo del promedio 
    """
    ai = int(a)
    bi = int(b)
    return (ai + bi) / 2

#------------------------------------------------------------------------------------------------------------------------

def promediar_listas(lista:list)->None:
    """promediras_listas

    Args:
        lista (list): pasamos la lista
    """
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

def each_list_actualizar_sueldos(lista:list,porcentaje)->None:          #"actualizaria" la lista original que nosotros tenemos
    """each_list_actualizar_sueldos
    Args:
        lista (list): pasamos la lista original
        porcentaje (_type_): pasamos el porcentaje de sueldo a actualizar 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i]["sueldo"] = lista[i]["sueldos"] + lista[i]["sueldos"] * porcentaje 

#------------------------------------------------------------------------------------------------------------------------

def each_list_genero_mayusculas(lista:list)->None:          #"actualizaria" la lista original que nosotros tenemos 
    """each_list_genero_mayusculas

    Args:
        lista (list): pasamos la lista original
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i]["genero"] = lista[i]["genero"].upper() 


#------------------------------------------------------------------------------------------------------------------------
def each_list(funcion,lista:list)->None:          #"actualizaria" la lista original que nosotros tenemos 
    """each_list
    Args:
        funcion (_type_): pasamos la funcion que queremos que haga each_list
        lista (list): pasamos la lista original
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i] = (funcion(i))

#each_list(lambda emp: emp.update({["sueldo"] * 1.20}) , empleados)   #asi se utilizan estas funciones
#each_list(lambda emp: emp.update({["genero"].upper()}) , empleados)
#each_list(lambda emp: emp.update({"genero": emp["genero".upper],"sueldo": emp["sueldo"] * 1.20}) , empleados)
    
#------------------------------------------------------------------------------------------------------------------------
    





#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")  #asi se usa la funcion anterior 
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")


def filtrar_listas(funcion,lista:list)->list:                       #sirve para filtrar cualquier lista con cualquier valor
    """filtrar_listas

    Args:
        funcion (_type_): ponemos lo que queramos que filtre nuestra funcion
        lista (list): pasamos la lista original 

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

#--------------------------------------------------------------------------------------------------------------------------
def sumar_lista(lista:list)->int:
    """sumar_lista

    Args:
        lista (list): pasamos la lista original 

    Returns:
        int: retorna la suma de todos los elementos de la lista 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    sum = lista[0]
    for el in lista[1: ]:
        sum += el
    return sum

#------------------------------------------------------------------------------------------------------------------------


def mayor_lista(lista:list)->int:
    """mayor_lista

    Args:
        lista (list): pasamos la lista original 

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

def reduce_list(funcion,lista:list)->any:    #manera generica o mas eficaz de todo lo anterior
    """reduce_list

    Args:
        funcion (_type_): pasamos lo que queremos que haga la funcion
        lista (list): pasamos la lista original 

    Returns:
        any: un entero 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ant = lista[0]
    for el in lista[1: ]:
        ant = funcion(ant,el)
    return ant


numeros = [1,5,7,8,9,2,7]

#total = reduce_list(lambda ant,actual: ant + actual, numeros)   #asi se utiliza el reduce list(con la forma de la funcion suma)
#print(total)
#mayor = reduce_list(lambda ant,actual: ant if ant > actual else actual,numeros)  #asi se utiliza el reduce list(con la forma de la funcion mayor)
#print(mayor)
#------------------------------------------------------------------------------------------------------------------------

def normalizar_datos(lista_heroes: list[dict])-> bool:
    """stark_normalizar_datos

    Args:
        lista_heroes (list[dict]): pasamos un diccionario 

    Returns:
        bool: nos devuelve los datos del diccionario listo para usar
    """
    if not isinstance(lista, list[dict]): raise TypeError ("primer parametro debe ser una lista")
    
    if lista_heroes != []:

        retorno = False
        for i in range(len(lista_heroes)):

            if type(lista_heroes[i]["altura"]) != float:
                altura_float = float(lista_heroes[i]["altura"])
                lista_heroes[i]["altura"] = altura_float
                retorno = True

            if type(lista_heroes[i]["peso"]) != float:
                lista_heroes[i]["peso"] = float(lista_heroes[i]["peso"])
                retorno = True

            if type(lista_heroes[i]["fuerza"]) != int:
                lista_heroes[i]["fuerza"] = int(lista_heroes[i]["fuerza"])
                retorno = True

        return retorno
#------------------------------------------------------------------------------------------------------------------------


def normalizar_datos(lista_heroes: list[dict])-> any:
    """stark_normalizar_datos

    Args:
        lista_heroes (list[dict]): pasamos un diccionario 

    Returns:
        bool: nos devuelve los datos del diccionario listo para usar
    """
    if not isinstance(lista_heroes, list): raise TypeError ("primer parametro debe ser una lista")
    
    if lista_heroes != []:

        retorno = False
        for i in range(len(lista_heroes)):

            if type(lista_heroes[i]["altura"]) != float:
                altura_float = float(lista_heroes[i]["altura"])
                lista_heroes[i]["altura"] = altura_float
                retorno = True

            if type(lista_heroes[i]["peso"]) != float:
                lista_heroes[i]["peso"] = float(lista_heroes[i]["peso"])
                retorno = True

            if type(lista_heroes[i]["fuerza"]) != int:
                lista_heroes[i]["fuerza"] = int(lista_heroes[i]["fuerza"])
                retorno = True

        return retorno
#------------------------------------------------------------------------------------------------------------------------    
    
def mostrar_dato_super_h(lista_super:list,campo)->any:
    """mostrar_dato_super_h

    Args:
        lista_super (list): pasamos la lista original 
        campo (_type_): pasamos el campo que queremos que nos muestre 

    Returns:
        any: devuelve el dato del campo que pedimos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for el in lista_super:
        print(el[campo])
#------------------------------------------------------------------------------------------------------------------------

def mostrar_datos_super_h(lista_super:list,campo1:str,campo2:str)->any:
    """mostrar_datos_super_h

    Args:
        lista_super (list): pasamos la lista original 
        campo1 (_type_): pasamos el primer campo que queremos que nos muestr 
        campo2 (_type_): pasamos el segundo campo que queremos que nos muestr 

    Returns:
        any: _description_
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for el in lista_super:
        print(el[campo1],el[campo2])


#------------------------------------------------------------------------------------------------------------------------


def altura_promedio_super(lista_super:list)->any:
    """altura_promedio_super

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve el promedio de altura de super heroes
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for _ in lista_super:
        nombre_altura_s = mapear_list(lambda alt:(alt["altura"]),lista_super)
        promedio = calcular_promedio_3_lista(nombre_altura_s) 
    mensaje = (f"el promedio de altura de los super heroes es: {promedio}")
    return mensaje



#------------------------------------------------------------------------------------------------------------------------




def super_masculino(lista:list)->any: #A
    """super_masculino

    Args:
        lista (list): pasamos la lista original

    Returns:
        any: nos devuelve el nombre de todos los masculinos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista)
    nombres_masculinos = mapear_list(lambda nombre:(nombre["nombre"]),supers_masculinos)    
    return nombres_masculinos


#------------------------------------------------------------------------------------------------------------------------



def super_Femenino(lista_super:list)->any: #b
    """super_Femenino

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: nos devuelve el nombre de todos los femeninos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femenino = filtrar_listas(lambda emp: emp["genero"] == "F",lista_super)
    nombres_femenino = mapear_list(lambda nombre:(nombre["nombre"]),supers_femenino)    
    return nombres_femenino



#------------------------------------------------------------------------------------------------------------------------


def mas_alto_masculino(lista_super:list)->any:#c
    """mas_alto_masculino

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve el mas alto de los masculinos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista_super)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_masculinos)
    mas_alto = calcular_mayor(datos_masculinos)
    return mas_alto


#------------------------------------------------------------------------------------------------------------------------


def mas_alto_femenino(lista:list)->any:#d
    """mas_alto_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el femenino mas alto 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femeninos = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femeninos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_femeninos)
    mas_alto = calcular_mayor(datos_femeninos)
    return mas_alto


#------------------------------------------------------------------------------------------------------------------------


def mas_bajo_masculino(lista:list)->any:#e
    """mas_bajo_masculino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el mas bajo de los masculinos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")

    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_masculinos)
    mas_bajo = calcular_menor(datos_masculinos)
    return mas_bajo


#------------------------------------------------------------------------------------------------------------------------

def mas_bajo_femenino(lista:list)->any:#f
    """mas_bajo_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: devuelve el mas bajo de los femeninos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femeninos = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femeninos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_femeninos)
    mas_bajo = calcular_menor(datos_femeninos)
    return mas_bajo


#------------------------------------------------------------------------------------------------------------------------

def promedio_alt_masculino(lista_super:list)->any:#g
    """promedio_alt_masculino

    Args:
        lista_super (list): pasamos la lista original 

    Returns:
        any: nos devuelve el promedio de altura masculino
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista_super)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"]),supers_masculinos)
    mas_alto = calcular_promedio_3_lista(datos_masculinos)
    return mas_alto


#------------------------------------------------------------------------------------------------------------------------

def promedio_alt_femenino(lista:list)->any:#h
    """promedio_alt_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el promedio mas alto femenino 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femenino = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femenino = mapear_list(lambda datos_mas:(datos_mas["altura"]),supers_femenino)
    mas_alto = calcular_promedio_3_lista(datos_femenino)
    return mas_alto

#------------------------------------------------------------------------------------------------------------------------


def tipo_color_ojos(lista:list,color_a_elegir:str)->any: # j
    """tipo_color_ojos

    Args:
        lista (list): pasamos la lista original 
        color_a_elegir (str): elegimos el color de ojos que queremos 

    Returns:
        any: devuelo cuantas personas tienen ese tipo de color de ojos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["color_ojos"]),lista)
    color = contador_color_ojos(ojos,color_a_elegir)
    return color

#------------------------------------------------------------------------------------------------------------------------


def agrupar_color_ojos(lista:list,target:str)->any:  #m
    """agrupar_color_ojos

    Args:
        lista (list): pasamos la lista original 
        target (str): elegimos el color de ojos que queremos 

    Returns:
        any: devuelve el nombre de todos los que  tienen ese color de ojos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mismo_ojos_color = filtrar_listas(lambda ojos:(ojos["color_ojos"]== target),lista)
    super_nombre_ojos =  mapear_list(lambda nombre: (nombre["nombre"]),mismo_ojos_color)
    return super_nombre_ojos


#------------------------------------------------------------------------------------------------------------------------


def agrupar_color_pelo(lista:list,target:str)->any: #n
    """agrupar_color_pelo

    Args:
        lista (list): pasamos la lista original 
        target (str): pasamos el color de pelo que queremos 

    Returns:
        any: nos devuelve el nombre de todos los que tienen ese color de pelo 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mismo_pelo_color = filtrar_listas(lambda ojos:(ojos["color_pelo"]== target),lista)
    super_nombre_pelo =  mapear_list(lambda nombre: (nombre["nombre"]),mismo_pelo_color)
    return super_nombre_pelo

#------------------------------------------------------------------------------------------------------------------------


def agrupar_inteligencia(lista:list,target:str)->any:  #0 
    """agrupar_inteligencia

    Args:
        lista (list): pasamos la lista original
        target (str): pasamos la inteligencia que queremos 

    Returns:
        any: nos devuelve el nombre de todos los que tienen esa inteligencia 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    misma_inteligencia = filtrar_listas(lambda ojos:(ojos["inteligencia"]== target),lista)
    super_nombre_inteligencia =  mapear_list(lambda nombre: (nombre["nombre"]),misma_inteligencia)
    return super_nombre_inteligencia


#------------------------------------------------------------------------------------------------------------------------

def tipo_color_pelo(lista:list,color_a_elegir:str)->any: #i
    """tipo_color_pelo

    Args:
        lista (list): lista
        color_a_elegir (str): elegimos el color de pelo que queremos 

    Returns:
        any: nos devuelve la cantidad de heroes que tienen el color de ojos que elgimos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["color_pelo"]),lista)
    color = contador_color_ojos(ojos,color_a_elegir)
    return color


#------------------------------------------------------------------------------------------------------------------------

def tipo_inteligencia(lista:list,inteligencia:str)->any: #i
    """tipo_inteligencia

    Args:
        lista (list): pasamos la lista original 
        inteligencia (str): elegimos la inteligencia que queremos 

    Returns:
        any: nos devuelve la cantidad de heroes que tienen esa inteligencia 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["inteligencia"]),lista)
    rojo = contador_color_ojos(ojos,inteligencia)
    return rojo

#------------------------------------------------------------------------------------------------------------------------


def contador_color_ojos(lista:list, target:str)->int:
    """contador_color_ojos

    Args:
        lista (list): pasamos la lista orignial 
        target (str): pasamos el target que queremos contar 

    Returns:
        int: devuelve la cantidad de veces que esta el target en la lista
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    contador_elemento = 0
    for color in lista:
        if color == target:
            contador_elemento+= 1
    return contador_elemento



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


#la funcion siguiente funciona con cualquier csv la de arriba se tiene que modificar 

# def cargar_csv(nombre_archivo):
#     """
#     Carga un archivo CSV y lo convierte en una lista de diccionarios.

#     Parámetros:
#     nombre_archivo (str): El nombre del archivo CSV (incluye la extensión .csv).

#     Retorna:
#     list: Una lista de diccionarios, donde cada diccionario representa una fila del archivo CSV.
#     """
#     try:
#         with open(nombre_archivo, 'r') as archivo:
#             lector_csv = csv.DictReader(archivo)
#             lista = [fila for fila in lector_csv]
#         print(f"El archivo {nombre_archivo} ha sido cargado exitosamente.")
#         return lista
#     except Exception as e:
#         print(f"Error al cargar el archivo: {e}")
#         return []




def guardar_archivo_csv(lista:list,nombre_archivo_csv)->any:
    """guardar_archivo_csv

    Args:
        lista (list): paso una lista
        nombre_archivo_csv (_type_): el nombre del archivo que quiero ponerle 

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


#la siguiente funcion hace lo mismo que la anterior 
# def cargar_archivo_json(archivo):
#     with open(tomar_ruta_actual(archivo),"r", encoding="utf-8") as archivo_json:
#         return json.load(archivo_json)
    
def guardar_archivo_json(archivo_json, lista):
    with open(tomar_ruta_actual(archivo_json), "w", encoding="utf-8") as archivo_json:
        return json.dump(lista, archivo_json, indent = 4)




#------------------------------------------------------------------------------------------------------------------------


def cargar_lista_enteros_random(lista:list, cant:int, desde:int, hasta:int)->any:
    """cargar_lista_enteros_random

    Args:
        lista (list): pasamos lista para meter los numeros random 
        cant (int): pasamos la cantidad que queremos de numeros random 
        desde (int): pasamos desde cuando queremos que arranque 
        hasta (int): pasamos hasta donde queremos que llegue 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))


#------------------------------------------------------------------------------------------------------------------------

def bicileta_random(lista:list)->list:
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(50, 120)
        lista[i]["tiempo"] = lista_tiempo    
    return lista

#------------------------------------------------------------------------------------------------------------------------
def cambiar_likes_random(lista:list)->list:
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(500, 3000)
        lista[i]["likes"] = lista_tiempo    
    return lista
#------------------------------------------------------------------------------------------------------------------------
def cambiar_dislikes_random(lista:list)->list:
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(300, 3500)
        lista[i]["dislikes"] = lista_tiempo    
    return lista

#------------------------------------------------------------------------------------------------------------------------
def cambiar_followers_random(lista:list)->list:
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista_tiempo = randint(10000, 20000)
        lista[i]["followers"] = lista_tiempo    
    return lista




#------------------------------------------------------------------------------------------------------------------------

def mapear_tiempo_nombre(lista:list)->any:
    """mapear_altura_nombre

    Args:
        lista (list): paso la lista original

    Returns:
        list:retorna una lista con solo la altura y el nombre
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["tiempo"],emp["nombre"]))
    return lista_retorno


#------------------------------------------------------------------------------------------------------------------------

def mapear_tiempo_nombre(lista:list)->list:
    """mapear_altura_nombre

    Args:
        lista (list): paso la lista original

    Returns:
        list:retorna una lista con solo la altura y el nombre
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["tiempo"],emp["nombre"]))
    return lista_retorno

#------------------------------------------------------------------------------------------------------------------------

def ganador_bicicleta(lista:list)->str:
    """ganador_bicicleta

    Args:
        lista (list): pasamos la lista 

    Returns:
        str: devuelve el ganador con menos tiempo
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")

    tiempo_nombre = mapear_tiempo_nombre(lista)
    ganador = calcular_menor(tiempo_nombre)
    mensaje = f"el ganador de la carrera es {ganador[1]} y el tiempo que tardo es {ganador[0]} minutos"
    return mensaje

#------------------------------------------------------------------------------------------------------------------------


def tipo_bicicletas(lista:list,bicicleta_a_elegir:str)->any: # j
    """tipo_color_ojos

    Args:
        lista (list): pasamos la lista original 
        color_a_elegir (str): elegimos el color de ojos que queremos 

    Returns:
        any: devuelo cuantas personas tienen ese tipo de color de ojos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_nueva = []
    
    bici = mapear_list(lambda bici:(bici["id_bike"],bici["nombre"],bici["tipo"] == bicicleta_a_elegir,bici["tiempo"]),lista)

    lista_nueva.append(bici)
    

    return lista_nueva


#------------------------------------------------------------------------------------------------------------------------

def promedio_tipo_bici(lista:list,target)->any:#c
    """promedio_tipo_bici

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve el promedio
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    tipo = filtrar_listas(lambda tiempo: (tiempo["tipo"] == target),lista)
    tiempo = mapear_list(lambda tiempo: (tiempo["tiempo"]),tipo)
    promedio = calcular_promedio_3_lista(tiempo)
    return promedio

#------------------------------------------------------------------------------------------------------------------------


def ordenar_ascendente_por_nombre_user(lista):
    """ordenar_ascendente_por_nombre

    Args:
        lista (_type_): pasamos la lista a ordenar

    Returns:
        _type_: devuelve la lista ordenada de forma ascendente 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if len(lista[j]['user']) < len(lista[min_idx]['user']):
                min_idx = j
        # Intercambiar elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista




def post_mas_likeado(lista:list)->str:
    """post_mas_likeado

    Args:
        lista (list): pasamos la lista 

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
            