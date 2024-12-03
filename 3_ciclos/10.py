#Ejercicio 10
#!Crea un algoritmo para registrar una contraseña segura para ingresar a un menu el cual contendra todos los algoritmos de la carpeta ciclos.
#* Primeramente muestra al usuario un menu el cual sea, registrarse o ingresar. En el registro, tendra que ingresar un usuario y contraseña. Los requisitos para el usuario son:
#? - Entre 4 a 12 caracteres
#? - no puede iniciar con un numero o simbolo
#? - Tiene que empezar con mayúscula

#* Para la contraseña:
#? - Entre 5 a 8 caracteres
#? - Que contenga al menos un simbolo valido: * , _ , $
#? - no puede iniciar con un numero o simbolo
#? - No puede ser igual a el nombre de usuario
#* valida esta misma dos veces, la primera para el registro y la segunda de confimacion.

#* Una vez terminado el registro, da la opcion de volver al menu principal de registro o ingresar. Al ingresar, pide al ususario que ingrese los datos del registro y solo tendra 5 intentos, si no lo ingresa correctamente, finaliza la ejecucion. 
#! Al dar con los datos correctos muestra un menu el cual muestre el script del ejercicio 1, 2 y 3.

#>>> No utilices funciones, funciones nativas, módulos ni excepciones 

usuario = None
contraseña = None
op = None # Variable de control para el menú

while True:
    print("-----MENÚ-----")
    print(">>-lNGRESAR-<<\t>>-REGISTRARSE-<<\t>>-SALIR-<<")
    print("opcion 1\topcion 2\t\topcion 3")

    #Valida que OP sea un valor esperado
    while True:
        op = int(input(">>: ")) 
        if 1 <= op <= 3:
            break
        else:
            print("\nIngresa un numero entre las 3 opciones dadas\n\n")
    
    match op:
        case 1:
            print("-----INGRESAR-----\n")
            if usuario == None:
                print("No existe un usuario actual. Registrate")
                continue
            for i in range(5):
                if input("Usuario: ") == usuario and input("contraseña: ") == contraseña:
                    print("---Entrada exitosa---\n\n")
                    #>>>Codigo
                    
                    while True:
                        print("Menú. Ingresa una opcion: 1 | 2 | 3")
                        print("oprime 0 para salir.")
                        op_sub = int(input(": "))
                        match op_sub:
                            case 1:
                                print("Ejercicio 1. \n")
                                numeros = [10,30,43,143,13,23,23,566,33,16]
                                suma = 0

                                i = 0 # variable aux contadora del 0-9 / 10 digitos


                                #*input
                                print(">>>Datos de entrada<<<")
                                print(numeros)

                                #*process
                                while i < 10:
                                    suma += numeros[i]
                                    i += 1    

                                #*output
                                print("\n-----Datos de salida--------")
                                print(f">>>suma total: {suma}")
                                print("----------------------------")
                        
                            case 2:
                                print("Ejercicio 2\n")
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
                            case 3:
                                print("Ejercicio 3\n")
                                #*variables
                                num_cuenta = 0
                                saldo = 0.0
                                saldo_acreedoras = 0.0

                                #*input

                                while True:
                                    print(">>>Datos de entrada<<<")
                                    num_cuenta = int(input("numero de cuenta: "))
                                    saldo = float(input("Saldo de la cuenta: "))

                                    if num_cuenta < 0:
                                        print("Numero de cuenta no valido.")
                                        break

                                    if saldo > 10_000:
                                        print("Es deudor")
                                    elif saldo == 10_000:
                                        print("Es acreedor")
                                        saldo_acreedoras += saldo
                                    elif saldo == 0:
                                        print("Cuenta sin fondos. Utilice el flujo de su cuenta. Nulo")
                                
                                #*process

                                #*output
                                print("\n-----Datos de salida--------")
                                print(f">>> Saldo total de acreedores: {saldo_acreedoras}")
                                print("----------------------------")
                            
                            case 0:
                                print("Saliendo de la ejecucion")
                                break
                            

                else:
                    print("Datos incorrectos, Volver a intentar")
                if i == 4:
                    print("Intentos excedidos")
                    exit()
        case 2:
            print("-----REGISTRARSE-----\n")
            while True:
                print("_<REGISTRO USUARIO>_ \nReglas:",
                        "\n- Entre 4 a 12 caracteres",
                        "\n- no puede iniciar con un numero o simbolo"
                        )
                print("nombre de usuario: ")
                usuario = input(":: ")
                usuario_pass = False

                if (4 <= len(usuario) <= 12) and ("A" <= usuario[0] <= "Z"):
                   usuario_pass = True

                if usuario_pass == True:
                    print("\n---USUARIO DISPONIBLE---")
                    print(f"Su usuario es: {usuario}.")
                    print(f"Esta de acuerdo?[S/N]")
                    if input(":: ").upper()== "S":
                        break
                else:
                    print(f"\n[ALERTA]-> El usuario {usuario} no es valido <-\n")
            while True:
                print("_<REGISTRO CONTRASEÑA>_ \nReglas:",
                     "\n   - Entre 5 a 8 caracteres"
                     "\n   - Que contenga al menos un simbolo valido: * , _ , $"
                     "\n   - no puede iniciar con un numero o simbolo"
                     "\n   - No puede ser igual a el nombre de usuario"
                    )
                print("nombre la contraseña: ")
                contraseña = input(":: ")
                contraseña_pass = [0,0,0,0]
                #?VALIDACIONES:
                # Simbolos validos
                if any(simbolo in contraseña for simbolo in '*_$'):
                    contraseña_pass[0] = 1 # True
                else:
                    print("No cumple los simbolos asignados")
                # Tamaño de la contraseña
                if  5 <= len(contraseña) <= 8:
                    contraseña_pass[1] = 1 #True
                else:
                    print("Fuera del rango indicado")
                # Caracter inicial
                if "A" <= contraseña[0] <= "Z" or "a" <= contraseña[0] <= "z":
                    contraseña_pass[2] = 1 #True
                else:
                    print("No empeza con una letra")
                # Evitar igualdad
                if contraseña != usuario:
                    contraseña_pass[3] = 1
                else:
                    print("No pueden ser la misma contraseña y usuario")
                #?Confirmación  
                if sum(contraseña_pass) == len(contraseña_pass):
                    print("\n---CONTRASEÑA CREADA---")
                    print(f"Su CONTRASEÑA: {contraseña}.")
                    print(f"Esta de acuerdo?[S/N]")
                    if input(":: ").upper()== "S":
                        break
                
        case _:
            print("Saliendo")
            break
    
