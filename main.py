from funciones_parcial import *
from menu_parcial import *


flag_asignar_estadisticas = False
carga_correcta_csv = False
while True:
    match menu_01():
        case"1":
            nombre_arc = input("ingrese el nombre del archivo: ").lower()
            if nombre_arc != "posts":
                print("ese no es el nombre del csv reingreselo: ")
            else: 
                post = leer_archivo_csv(f"{nombre_arc}.csv")
                carga_correcta_csv = True
        case"2":
            print(post)
        case"3":
            if carga_correcta_csv == True:
                cambiar_likes_random(post)
                cambiar_dislikes_random(post)
                cambiar_followers_random(post)
                flag_asignar_estadisticas = True
                print("se asignaron las estadisticas con exito")
            else: 
                print("no se cargo el csv reintentelo")
        case"4":
            if flag_asignar_estadisticas == True:
                mas_likes = filtrar_listas(lambda mas2000:(mas2000["likes"] > 2000),post)
                guardar_archivo_csv(mas_likes,f"mas_likes_superior_a_2000.csv")
                print("se filtraron y se guardaron los users con mas de 2000 likes")
            else:
                print("falta asignar las estadisticas vuelva a intentarlo")
        case"5":
            if flag_asignar_estadisticas == True:
                mas_dislikes = filtrar_listas(lambda mas2000:(mas2000["dislikes"] > mas2000["likes"]),post)
                guardar_archivo_csv(mas_dislikes,f"mas_dislikes_que_likes.csv")
                print("se filtraron y se guardaron los users con mas dislikes que likes")
            else:
                print("falta asignar las estadisticas vuelva a intentarlo")
        case"6":
            if flag_asignar_estadisticas == True:
                follower = mapear_list(lambda followers:(followers["followers"]),post)
                promedio = calcular_promedio_3_lista(follower)
                print(f"el promedio de follower es {promedio}")
            else:
                print("falta asignar las estadisticas vuelva a intentarlo")       
        case"7":
            ordenar_ascendente_por_nombre_user(post)
            guardar_archivo_json("ordenados_ascendente_nombre.json",post)
            print("se ordenaron y se guardaron los users de forma ascendente por su nombre")
        case"8":
            if flag_asignar_estadisticas == True:
                mas_popular = post_mas_likeado(post)
                print(mas_popular)
            else:
                print("falta asignar las estadisticas vuelva a intentarlo") 
        case"9":
            break
    pausar()
print("Fin del programa")


    
