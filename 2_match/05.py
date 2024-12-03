"""
---
*Ejercicio: Calculadora Básica en Python*

!Desarrolla una calculadora sencilla en Python que permita realizar operaciones básicas como suma, resta, multiplicación y división, exponenciación y división entera. La calculadora debe solicitar al usuario dos números y la operación que desea realizar. Luego, debe mostrar el resultado de la operación.

?Requisitos:
1. La calculadora debe ofrecer las siguientes operaciones:
   - Suma (`+`)
   - Resta (`-`)
   - Multiplicación (`*`)
   - División (`/`)

2. El programa debe realizar las siguientes tareas:
   - Pedir al usuario que ingrese el primer número.
   - Pedir al usuario que ingrese el segundo número.
   - Pedir al usuario que ingrese la operación que desea realizar.
   - Validar que la operación ingresada sea una de las cuatro operaciones básicas mencionadas.
   - Realizar la operación solicitada y mostrar el resultado.

?Puntos a considerar:
- El programa debe manejar posibles errores.
- No utilizar ciclos, ni funciones built-in o módulos.
"""

#*variables
num1 = 0.0
num2 = 0.0
operacion = '' # se espera + , - , * , /
calculo = 0.0

#*input
print(">>>Datos de entrada<<<")

num1 = float(input("primer numero: "))
num2 = float(input("segundo numero: "))
print("Operacion a realidar: \
      - Suma (`+`) \
      - Resta (`-`) \
      - Multiplicación (`*`) \
      - División (`/`) \
")

operacion = input(">>: ")

#*process

match operacion:
   case '+':
      calculo = num1 + num2
   case '-':
      calculo = num1 - num2
   case '*':
      calculo = num1 * num2
   case '/':
      if num2 == 0:
         print("error. No se puede dividir por cero")
      else:
         calculo = num1 // num2
   case _ :
      print("operacion no valida.")


#*output
print("\n-----Datos de salida--------")
print(f">>> total: {calculo}")
print("----------------------------")