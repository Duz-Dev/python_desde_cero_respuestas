"""
!Ejercicio 11

*Un equipo de meteorólogos quiere analizar las temperaturas diarias de una semana en una ciudad específica. Las temperaturas se registran en grados Celsius, y el equipo necesita saber lo siguiente:

*El promedio de las temperaturas registradas en la semana.
*Cuántos días estuvieron por encima del promedio.
*Cuántos días estuvieron por debajo del promedio.

?Para realizar el análisis:

*Las temperaturas se ingresan manualmente una por una.
*Las temperaturas deben ser valores válidos (números enteros o decimales positivos o negativos).

?Restricciones:

*Usa únicamente ciclos while o for.
*No se permite el uso de funciones nativas de Python, ni la creación de funciones propias, ni módulos.
*Haz las validaciones necesarias para asegurar que las temperaturas ingresadas sean datos válidos.

?Requerimientos Finales:
Al final, muestra:
*Las temperaturas ingresadas.
*El promedio de las temperaturas.
*La cantidad de días con temperaturas por encima y por debajo del promedio."""


#*variables
temperatura = [0,0,0,0,0,0,0] # Recolecta la temperatura de la semana
i = 0
promedio = 0
prom_mayores = 0
prom_menores = 0

#*input
print(">>>Datos de entrada<<<")
while i < 7:
    temperatura[i] = float(input(f"Dia #{i+1}: "))
    if not(-89.2 < temperatura[i] < 60 ):
        print("Dato no valido, vuelve a ingresarlo")
        continue    
    i+=1

promedio = sum(temperatura) / len(temperatura)

for j in range(7):
    if temperatura[j] > promedio:
        prom_mayores += 1
    elif temperatura[j] < promedio:
        prom_menores += 1
        
#*process

#*output
print("\n-----Datos de salida--------")
print(f"El promedio de las temperaturas registradas en la semana: {promedio}")
print(f"Cuántos días estuvieron por encima del promedio: {prom_mayores}")
print(f"Cuántos días estuvieron por debajo del promedio: {prom_menores}")
print("----------------------------")