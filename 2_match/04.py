"""
*Sistema de Calificación de Películas:
    - Un sitio de críticas de películas quiere asignar calificaciones basadas en la opinión de los usuarios:
      - 0-1 estrellas: Muy Mala
      - 2-3 estrellas: Mala
      - 4-5 estrellas: Regular
      - 6-7 estrellas: Buena
      - 8-9 estrellas: Muy Buena
      - 10 estrellas: Excelente
    - Crea un programa que reciba el nombre de la película y la calificación del usuario, y que imprima la calificación correspondiente.
"""

#*variables
nombre = '' #nombre de la pelicula
cal_usr = '' # calificacion brindada por el usario
cal_msj = '' # MenSaJe de acuerdo a la calif obtenida

#*input
print(">>>Datos de entrada<<<")
nombre = input("Nombre de la pelicula: ")
cal_usr = int(input("calificacion a dar. \n Recuerda que tiene que ser entre 0 y 10\n :"))

#*process

match cal_usr:
    case 0 | 1:
        cal_msj = "Muy Mala"
    case 2 | 3:
        cal_msj = "Mala"
    case 4 | 5:
        cal_msj = "Regular"
    case 6 | 7:
        cal_msj = "Buena"
    case 8 | 9:
        cal_msj = "Muy Buena"
    case 10:
        cal_msj = "Excelente"
    case _:
        print("Calificacion no valida")
        cal_msj = "nula"

#*output
print("\n-----Datos de salida--------")
print(f">>>Pelicula: {nombre}")
print(f">>>Calificacion obtenida: {cal_msj}")
print("----------------------------")