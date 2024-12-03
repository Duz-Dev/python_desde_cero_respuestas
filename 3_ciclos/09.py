#Ejercicio 9
#!Crea un algoritmo para pedirle al usuario un numero positivo y muestra en pantalla todos los numeros del 1 hasta dicho numero comprendido y posteriormente ve restando desde el numero dado hasta el 1.


#*variables
num = 0

#*input
print(">>>Datos de entrada<<<")

while True:
    num = int(input("Ingresa un numero hasta cual contar: "))
    if num < 0:
        print("Numero no valido, vuelve a ingresa un valor positivo")
    else:
        break


#*process
print("\n-----Datos de salida--------")

for i in range(1,num+1):
    if not(i==num):
        print(i)
    else:
        print("----------------------------")
        print(i)
        print("----------------------------")


for j in range(1,num):
    i-=1
    print(i)

#?Otra solucion
#for i in range(numero, 0, -1):
 #   print(i)

print("----------------------------")
