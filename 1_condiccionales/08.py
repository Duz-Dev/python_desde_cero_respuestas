"""
!Elabora un algoritmo para calcular e imprimir el precio de un terreno del cual se tienen los siguientes datos: largo, ancho, y el precio por metro cuadrado. Si el terreno tiene mas de 400 metros cuadrados, se hace un descuento de 10%.
>>>imprime el area del terreno y el precio.
"""

#*variables
largo = 0.0
ancho = 0.0
precio = 0.0
area = 0.0

#*input
print(">>>Datos del terreno<<<")
largo = float(input("Ingresa el largo: "))
ancho = float(input("Ingresa el ancho: "))
precio = float(input("Ingresa el precio del metro cuadrado: "))

#*process
area = round((largo * ancho))
if area > 400:
    precio *= 0.9

#*output
print("-----Datos de salida--------")
print(f"Area del terreno: {area}u²")
print(f"precio: ${precio}")
print("------------------------")

