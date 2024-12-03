
#!Ejercicio 5: Sumar elementos de una lista
""" 
Ejercicio 5: Sumar elementos de una lista
Escribe un programa que calcule la suma de los números en una lista. La lista puede tener valores no numéricos. Si encuentra un valor que no es un número (por ejemplo, una cadena de texto), debe capturar el error y mostrar un mensaje de advertencia. La suma debe continuar con los elementos que sean números.
>>>Lista de ejemplo: [1, 2, 3, 'a', 4, 'b'].
"""

lista = [1, 2, 3, 'a', 4, 'b']
suma = 0
print("Lista a sumar:",lista)

for i in lista:
    try:
        if type(i) == int:
            suma += i
        else:
            raise TypeError(f"ADVERTENCIA. '{i}' Tipo de dato no valido para sumar.")
    except TypeError as e:
        print(e)
    continue

print(suma)