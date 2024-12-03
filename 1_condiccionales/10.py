"""
!Dado un numero entero, desarrolla un algoritmo para determinar si no es par, imprimir el mensaje 'el numero no pertenece a los pares', de lo contrario imprime 'el numero pertenece a los pares'.
"""

#*variables
numero = 0

#*input
numero = int(input("Ingresa el numero:"))

#*process
if not((numero % 2) == 0):
    mensaje = "El numero no pertenece a los pares"
else:
    mensaje = "El numero pertenece a los pares"

#*output
print(mensaje)