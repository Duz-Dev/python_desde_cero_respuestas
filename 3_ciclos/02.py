#Ejercicio 2
#!En base a eI ejercicio planteado con la estructura match, donde se creo una calculadora. (ejercicio #5 de la carpeta de match) Crea un menu, donde el usuario ingrese una de las opciones validas, de Io contrario, que vuelva a ingresar dicho valor.

#!Modifica la estructura para que tenga una opción de volver a escoger entre las opciones de la calculadora o salir de la ejecución.
#? Requisitos: 
#* -Usa el ciclo while
#* -Nada de funciones nativas, módulos, funciones.


#*variables
num1 = 0.0
num2 = 0.0
operacion = '' # se espera + , - , * , /
calculo = 0.0


while True:
    #*input
    print("\n>>>Datos de entrada<<<\n")

    num1 = float(input("primer numero: "))
    num2 = float(input("segundo numero: "))
    print("Operacion a realidar: \
        - Suma (`+`) \
        - Resta (`-`) \
        - Multiplicación (`*`) \
        - División (`/`) \
        -salir del programa ('S') \
    ")
    operacion = input(">>: ").upper()

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
        case 'S':
            break
        case _ :
            print("operacion no valida.")
            print("Vuelve a seleccionar una opcion.")
            
#*output        
    print("\n-----Datos de salida--------")
    print(f">>> total: {calculo}")
    print("----------------------------")

#Ejecucion para terminar el ciclo
    if input("¿Desea volver al menú? [S/N] \n>> ").upper() == "N":
        break


