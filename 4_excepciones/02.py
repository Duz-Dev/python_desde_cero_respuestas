
#!Ejercicio 2: Acceder a elementos de una lista
""" 
Crea un programa que le pida al usuario ingresar un índice para acceder a un elemento de una lista. La lista contiene 5 elementos de tipo string. Si el usuario ingresa un índice fuera de rango o algo no numérico, el programa debe manejar estos errores con el bloque try-except y mostrar un mensaje adecuado.
>>>Lista de ejemplo: ["Manzana", "Banana", "Cereza", "Durazno", "Uva"].
"""

lista = ["Manzana", "Banana", "Cereza", "Durazno", "Uva"]

try:
    indice = int(input("Ingresa el indice: "))

    print(f"Elemento: {lista[indice]}")

except IndexError:
    print("[ERROR]. Indice fuera de rango de la lista")
except ValueError:
    print("[ERROR]. Tipo de dato no numerico")