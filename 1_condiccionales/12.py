"""
!Dada la función (ver url)[https://i.postimg.cc/tgyBJ6xQ/imagen.png]
!Desarrolla un algoritmo que calcule la función para un valor dado de 'x' que indica dependiendo del caso.
>>> Imprime el valor de la función
"""

#*variables
x = 0.0
funcion = 0.0

#*input
print(">>>Datos de entrada<<<")
x = float(input("ingresa el valor de x: "))

#*process
if (x <= 0) :
    funcion = x**2 - x
else:
    funcion = -(x**2) + 3*x

#*output
print("-----Datos de salida--------")
print("Valor de la funcion:",funcion)
print("----------------------------")