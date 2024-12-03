
#!Ejercicio 7: Manejar múltiples excepciones
""" 
Crea un programa que realice una operación matemática donde el usuario ingrese dos números. El programa debe manejar:
*	ZeroDivisionError si el usuario intenta dividir entre cero.
*	ValueError si el usuario ingresa un valor no numérico.
*	OverflowError si el número es demasiado grande para manejarlo. Haz que el programa 
>>>imprima un mensaje personalizado para cada tipo de error.

"""
div = 0
try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    #div
    div = num1 / num2
except ZeroDivisionError:
    print("el segundo numero no puede ser cero. No es posible la division")
except ValueError:
    print("Datos no validos")
except OverflowError:
    print("Los numeros son demaciado grandes")