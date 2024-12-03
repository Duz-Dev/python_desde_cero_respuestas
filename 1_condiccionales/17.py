"""
!Desarrolla un algoritmo que, dados dos números enteros, muestre por pantalla uno de estos mensajes:
!- El segundo es el cuadrado exacto del primero.
!- El segundo es menor que el cuadrado del primero
!- El segundo es mayor que el cuadrado del primero.
!Dependiendo de la verificación de la condición correspondiente al significado de cada mensaje.
"""

#*variables
num_1 = 0
num_2 = 0
mensaje = ""

#*input
print(">>>Datos de entrada<<<")
num_1 = int(input("Ingresa el primer numero: "))**2
num_2 = int(input("Ingresa el segundo numero: "))

#*process
if num_2 == (num_1):
    mensaje = "El segundo es el cuadrado exacto del primero."
elif num_2 < num_1:
    mensaje = "El segundo es menor que el cuadrado del primero"
elif num_2 > num_1:
    mensaje = "El segundo es mayor que el cuadrado del primero."

#*output
print("\n-----Datos de salida--------")
print(f">>>{mensaje}")
print("----------------------------")