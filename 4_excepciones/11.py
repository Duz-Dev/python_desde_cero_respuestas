""" 
!Ejercicio: Calculadora de Operaciones Matemáticas
Descripción: Diseña una calculadora que permita realizar operaciones de suma, resta, multiplicación y división entre dos números, y agrega funcionalidades para validar cada paso.

El programa debe preguntar al usuario qué operación desea realizar e ingresar dos números.
Si el usuario elige una operación no válida, lanza una excepción llamada OperacionInvalidaError.
Maneja posibles errores de entrada (valores no numéricos) y errores de división entre cero.
En el bloque finally, imprime un mensaje de despedida independientemente de si la operación fue exitosa o no.
Salida esperada:

Mensajes de error en caso de seleccionar una operación inválida o ingresar un valor no numérico.
Resultado de la operación si se ingresaron datos válidos.
"""
class OperacionInvalidaError(Exception):
    pass

resultado = 0
num1 = 0
num2 = 0

#*input
print(">>>CALCULADORA<<<")
print("SUMA '+'\t RESTA '-'\t MULTI '*'\t Division '/'")
op = input("Ingresa el operador a realizar: ")

try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    match op:
        case "+":
            print("Suma")
            resultado = num1 + num2
        case "-":
            print("resta")
            resultado = num1 - num2
        case "*":
            print("Multiplicacion")
            resultado = num1 * num2
        case "/":
            print("Division")
            resultado = num1 / num2
        case _:
            raise OperacionInvalidaError("Operacion ingresada no valida.")
        
except OperacionInvalidaError as e:
    print("ERROR:",e)
except ValueError:
    print("ERROR: Datos numericos ingresados no validos")
except TypeError as e:
    print("Se intento operar con valores no validos.",e)
except ZeroDivisionError:
    print("El 2do numero ingresado no es valido. No es posible dividir entre cero.")
else:

    #*output
    print("\n-----Datos de salida--------")
    print(f">>>Operacion:{num1} {op} {num2} = {resultado}")
    print("----------------------------")