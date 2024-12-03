"""
!Desarrolla un algoritmo que calcule el desglose en billetes y monedas de una cantidad exacta en pesos mexicanos. Hay billetes de 500, 200, 100, 50, 20 y monedas de 10, 5, 2 y 1.
!Por ejemplo, si deseamos conocer el desglose de $434, el programa mostrara por pantalla el siguiente resultado:
? 2 billetes de 200 pesos.
? 1 billete de 20 pesos.
? 1 billete de 10 pesos.
? 2 monedas de 2 pesos.
"""

#*variables
cantidad = 0 #cantidad a ingresar
billete_500 = 0
billete_200 = 0
billete_100 = 0
billete_50 = 0
billete_20 = 0
moneda_10 = 0
moneda_5 = 0
moneda_2 = 0
moneda_1 = 0

#*input
print(">>>Datos de entrada<<<")
cantidad = int(input("ingresa la cantidad a evaluar: "))

#*process
billete_500 = cantidad//500
cantidad -= billete_500 * 500


billete_200 = cantidad//200
cantidad -= billete_200 * 200


billete_100 = cantidad//100
cantidad -= billete_100 * 100


billete_50 = cantidad//50
cantidad -= billete_50 * 50


billete_20 = cantidad//20
cantidad -= billete_20 * 20


moneda_10 = cantidad//10
cantidad -= moneda_10 * 10


moneda_5 = cantidad//5
cantidad -= moneda_5 * 5

moneda_2 = cantidad//2
cantidad -= moneda_2 * 2

moneda_1 = cantidad//1
cantidad -= moneda_1

#*output
print("\n-----Datos de salida--------\n")
if not(billete_500 == 0):
    print(f"{billete_500} billetes de 500 pesos.")

if not(billete_200 == 0):
    print(f"{billete_200} billetes de 200 pesos.")

if not(billete_100 == 0):
    print(f"{billete_100} billetes de 100 pesos.")

if not(billete_50 == 0):
    print(f"{billete_50} billetes de 50 pesos.")

if not(billete_20 == 0):
    print(f"{billete_20} billetes de 20 pesos.")

if not(moneda_10 == 0):
    print(f"{moneda_10} monedas de 10 pesos.")

if not(moneda_5 == 0):
    print(f"{moneda_5} monedas de 5 pesos.")

if not(moneda_2 == 0):
    print(f"{moneda_2} monedas de 2 pesos.")

if not(moneda_1 == 0):
    print(f"{moneda_1} monedas de 1 pesos.")

print("\n----------------------------")


