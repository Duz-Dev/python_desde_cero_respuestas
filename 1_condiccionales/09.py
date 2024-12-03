"""
!El promedio de practicas de un curso se calcula en base a cuatro practicas calificadas de las cuales se elimina la calificación menor, y se promedian las tres restantes. Desarrolla un algoritmo que calcule e 
>>> imprima el promedio de las practicas de un estudiante y la calificación menor.
"""

#*variables
cal_1 = 0.0
cal_2 = 0.0
cal_3 = 0.0
cal_4 = 0.0
cal_menor = 0.0
promedio = 0.0

#*input
print(">>>Datos de las calificaciones<<<")
cal_1 = float(input("ingresa la calificacion 1: "))
cal_2 = float(input("ingresa la calificacion 2: "))
cal_3 = float(input("ingresa la calificacion 3: "))
cal_4 = float(input("ingresa la calificacion 4: "))

#*process
#calificacion menor
cal_menor = cal_1
if cal_2 < cal_menor:
    cal_menor = cal_2
if cal_3 < cal_menor:
    cal_menor = cal_3
if cal_4 < cal_menor:
    cal_menor = cal_4

#promedio
promedio = ((cal_1 + cal_2 + cal_3 + cal_4) - cal_menor)/3

#*output
print("-----Datos de salida--------")
print(f"Promedio del estudiante: {promedio:.2f}")
print(f"calificacion menor: ${cal_menor}")
print("------------------------")

