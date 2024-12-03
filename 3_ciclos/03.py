#Ejercicio 3
""" 
!Un banco necesita procesar datos de las cuentas corrientes de sus clientes. Cada cuenta se identifica por un número de cuenta y tiene un saldo actual. Los datos deben ingresarse manualmente por el usuario, y el ingreso de información finalizará cuando se introduzca un número de cuenta negativo.

*Se solicita desarrollar un programa que haga lo siguiente:

!Solicitar al usuario el número de cuenta y el saldo actual de forma iterativa.
!Determinar y mostrar el estado de la cuenta según las siguientes reglas:
?Acreedor: Si el saldo es mayor a 10,000.
?Deudor: Si el saldo es menor a 0.
?Nulo: Si el saldo es igual a 10,000.
!Llevar un registro y calcular la suma total de los saldos de las cuentas acreedoras.
!Terminar el programa cuando el usuario ingrese un número de cuenta negativo.
!Al finalizar, mostrar la suma total de los saldos de las cuentas acreedoras.
"""
#? Requisitos: 
#* -Usa el ciclo while
#* -Nada de funciones nativas, módulos, funciones.


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
