#Ejercicio 1
#! Dado diez números enteros, desarrolla un algoritmo para calcular la suma y el promedio de los diez números enteros, imprime la suma y el promedio.
#? Requisitos: 
#* -Usa el ciclo while
#* -Nada de funciones nativas, módulos, funciones.

#*variables

#?Analisis. Dado que no se describe exactamente la manera de adquirir esos 10 numeros, podemos llevar el algoritmo acabo de diferentes formas. Optare por una lista.
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