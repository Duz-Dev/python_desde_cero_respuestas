"""
*tres en uno
?Crea un menú el cual contenga los 3 ejercicios. Ingresaras a cada uno de estos ingresando una entrada por la terminal, si la persona ingresa 1, ejecutara el primer ejercicio, si ingresa 2, el segundo ejercicio y si ingresa 3, el tercer ejercicio. Si la persona ingresa un valor numerico fuera de los especificados, imprime que el dato no es valido y no ejecutes ningun ejercicio.

!Escribe un programa que solicite al usuario ingresar un número y luego verifique si ese número está presente en una lista predefinida de números. Imprime un mensaje indicando si el número está o no en la lista.

!Crea un programa que pida al usuario ingresar una palabra y luego determine si esa palabra está presente en una cadena de texto predefinida. Imprime un mensaje indicando si la palabra está o no en la cadena.

!Estás desarrollando una aplicación para calcular estadísticas básicas sobre los animes que has visto. Quieres un script que tome una lista de puntuaciones de episodios y calcule el promedio y la moda.
?Restricciones
- no usar módulos, funciones, ciclos. Solo condicionales
"""

#? Ejercicio 1

#*variables
num = 0
list_num = [0,1,2,4,5,6,7,8,9]
smg = "" #mensaje de salida

#*input
print(">>>Datos de entrada<<<")
num = int(input("ingresa el numero: "))

#*process
if num in list_num:
    smg = "El numero esta en la lista"
else:
    smg = "el numero no esta en la lista"

#*output
print("\n-----Datos de salida--------")
print(f">>> {smg}")
print("----------------------------")

#? Ejercicio 2
