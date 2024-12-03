"""
!El director del departamento deportivo de una facultad esta interesado en conocer que porcentaje de mujeres y hombres hay en la facultad. Desarrolla un algoritmo para calcular los porcentajes de hombres y mujeres que hay.
>>>imprime el porcentaje de cada sexo
"""

#*variables
mujer = 0
hombre = 0
porcentaje = 0

#*input
print(">>>Datos de los estudiantes<<<")
mujer = int(input("Total de mujeres inscritas: "))
hombre = int(input("Total de hombres inscritos: "))

#*process
porcentaje = mujer + hombre
por_mujer = (mujer / porcentaje)*100
por_hombre = (hombre / porcentaje)*100

#*output
print("-----Porcentajes--------")
print(f"hombres: {por_hombre}%")
print(f"mujeres: {por_mujer}%")
print("------------------------")
