
#!Ejercicio 6: Convertir un string a un número
""" 
Escribe un programa que intente convertir una cadena de texto ingresada por el usuario en un número flotante. Si el usuario ingresa algo que no se puede convertir a número (por ejemplo, una palabra), debe mostrar un mensaje indicando que la conversión falló.
"""

try:
    num = int(input("Ingresa un texto para convertir a numero: "))
except ValueError:
    print("La conversion fallo")