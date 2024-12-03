
""" 
#!Ejercicio 8: Comprobar edad
*Escribe un programa que le pida al usuario su edad y determine si puede ingresar a un lugar que tiene una restricción de edad mínima. Si el usuario ingresa algo que no es un número, debe capturarse el error y mostrar un mensaje adecuado. Además, si la edad ingresada es negativa, debe mostrar un mensaje indicando que la edad no puede ser negativa.

"""

try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 18:
        print("Solo se admiten mayores de 18 años")
    else:
        print("Puede pasar")
    if edad < 0:
        raise ValueError("[ERROR]. El dato no puede ser negativo")
except ValueError as e:
    print(">>> ",e)