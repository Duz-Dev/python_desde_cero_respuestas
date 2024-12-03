"""
*Cálculo de Calificaciones:
   - Una escuela quiere asignar letras de calificación a los estudiantes basándose en su puntuación numérica. Utiliza `match` para asignar las siguientes letras:
     - A (90-100)
     - B (80-89)
     - C (70-79)
     - D (60-69)
     - F (0-59)
   - Desarrolla un algoritmo que permita la entrada del nombre del estudiante y su puntuación, y que imprima el nombre del estudiante y su letra de calificación.
"""

#*variables
nombre = ''
cal_num = 0.0 # se espera ingresar la calificacion numeral
cal_letra = '' # la calificacion en el rango de los indicados A|B|C|D|F

#*input
print("Calificaciones del estudiante")
print(">>>Datos de entrada<<<")

nombre = input("nombre del estudiante: ")
cal_num = float(input("puntuacion obtenida: "))

#*process

match cal_num:
    case x if 90 <= cal_num <= 100:
        cal_letra = 'A'
    case x if 80 <= cal_num <= 89:
        cal_letra = 'B'
    case x if 70 <= cal_num <= 79:
        cal_letra = 'C'
    case x if 60 <= cal_num <= 69:
        cal_letra = 'D'
    case x if 0 <= cal_num <= 59:
        cal_letra = 'F'
    case _:
        cal_letra = "La puntuación ingresada, no es valida."
#*output
print("\n-----Datos de salida--------")
print("Nombre del estudiante:",nombre)
print(f">>>Calificacion final: {cal_letra}")
print("----------------------------")