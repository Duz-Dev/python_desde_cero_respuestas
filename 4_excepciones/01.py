
#!Ejercicio 1: Dividir dos números
""" 
*Escribe un programa que le pida al usuario ingresar dos números y luego realice la división. Asegúrate de manejar los siguientes errores:
>>>	Si el usuario ingresa algo que no sea un número, muestra un mensaje indicando que se esperaba un número.
>>>	Si el usuario intenta dividir por cero, muestra un mensaje indicando que no se puede dividir entre cero.
"""

#*variables
num1 = 0
num2 = 0
div = 0


#*process
print(">>>Datos de entrada<<<")

try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    div = num1 / num2

except ValueError:
    print("[ERROR] Datos no validos")
except ZeroDivisionError:
    print("[ERROR] No se puede dividir entre cero")

#*output
print("\n-----Datos de salida--------")
print(f">>>Resultado: {div}")
print("----------------------------")


