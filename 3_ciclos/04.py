#Ejercicio 4
#!Desarrolla un algoritmo para ingresar el peso en kilogramos para un conjunto de n piezas, el proceso termina cuando ingresamos un peso de cero. Imprime cuantas piezas tienen un peso entre 9.8kg y 10.2kg. Cuantas piezas tienen un peso de mas de 10.2kg y cuantas tienen un peso menor a 9.8kg. Ademas, imprime el total de piezas procesadas.
#? Requisitos: 
#* -Usa el ciclo while
#* -Nada de funciones nativas, módulos, funciones.


#*variables
peso = 0.0 # peso en kilogramos
piezas_tipoA = 0 #Piezas de un peso entre 9.8 - 10.2
piezas_tipoB = 0  # peso mayor 10.2
piezas_tipoC = 0  # peso meno 9.8
i = 0 # variable aux contadora / n piezas a usar

#*input
print(">>>Datos de entrada<<<")

while True:
    #code
    i+=1 # Va contando el total de ciclos

    peso = float(input(f"Peso #{i} a ingresar: "))
    
    if 9.8 <= peso <= 10.2 :
        piezas_tipoA += 1
    if peso > 10.2:
        piezas_tipoB += 1
    if  0 < peso < 9.8:
        piezas_tipoC += 1


    #sentencia para terminar el ciclo
    if peso == 0:
        print("Proceso terminado..")
        break

#*process

#*output
print("\n-----Datos de salida--------")
print(f">>>Totales:")
print(f">>>Numero de piezas entre '9,8 y 10,2': {piezas_tipoA}")
print(f">>>Numero de piezas mayor a '10,2': {piezas_tipoB}")
print(f">>>Numero de piezas menor a '9,8': {piezas_tipoC}")
print("----------------------------")