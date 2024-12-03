"""
!Ejercicio 6

*Un historiador matemático está investigando los números primos utilizados en la encriptación antigua. Te solicita que desarrolles un algoritmo que permita determinar la suma de todos los números primos dentro de un rango definido por el usuario.

El programa debe cumplir con lo siguiente:

*Solicitar al usuario dos números: el límite inferior y el límite superior del rango. Ambos valores deben ser enteros positivos mayores a 1, y el límite superior debe ser mayor al límite inferior.
*Validar que los valores ingresados cumplen las condiciones antes de proceder.
*Determinar cuáles números dentro de ese rango son primos.
*Calcular e imprimir la suma de esos números primos.

?Restricciones:

*No se pueden usar funciones nativas como isnumeric(), sum(), etc.
*No se pueden usar funciones definidas por el usuario ni módulos externos.
*Usa únicamente ciclos (while o for), estructuras condicionales (if, else), y operaciones básicas.

?Salida esperada:

Una lista de los números primos encontrados.
La suma total de esos números."""


#*variables
lim_superior = 0
lim_inferior = 0
primos = []
i = 0
suma_primos = 0

#*process

while True:
    #*input
    print(">>>Datos de entrada<<<")
    lim_inferior = int(input("Ingresa el limite inferior: "))
    lim_superior = int(input("Ingresa el limite superior: "))

    # Validamos que dichos valores sean los que esperamos:
    if lim_inferior <= 1 or lim_inferior >= lim_superior:
        print("La entrada de datos no es valida. Vuelve a ingresarlos.")
    else:
        break


for i in range(lim_inferior, lim_superior + 1):
    divisor = 2
    es_primo = True

    while divisor**2 <= i:

        if i%divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        primos.append(i)
        suma_primos += i

print("\n----- Resultados -----")
print(f"Números primos encontrados: {primos}")
print(f"Suma de los números primos: {suma_primos}")
print("----------------------")


#?Nota. Tal vez para este algoritmo nacieron muchas dudas. Te aconsejo que preguntes en la comunidad de discord previamente.
""" 
En este ejercicio partimos de intentar encontrar una manera de saber que numero es primo, para esto hacemos uso de las matemáticas, mas en concreto del teorema fundamental de la aritmética el cual ya nos cuenta que:

Todo número entero mayor que 1 puede descomponerse en un producto único de números primos.

Esto implica que, si un número no es primo, necesariamente se puede dividir entre números primos más pequeños, y esos divisores estarán en el rango de 2 a raiz de n

Con estas premisas podemos desarrollar el algoritmo. Es simple, solo hay que tener un numero el cual asumamos que es primo hasta que se demuestre lo contrario, para validar esto solo hay que dividir dicho numero candidato a primo entre cada uno y de forma individual los numeros que estan entre el 2 y el valor dado de sacar la raiz cuadrada de nuestro candidato a primo.

Recuerda, ya teniendo hasta que numero vamos a dividir, solo basta la manera de crear dicha condicion, en este caso esperaríamos que mientras nuestro candidato al ser dividido por el divisor que tengamos asignado en el rango de [2,n**(1/2)] Si es cero, se descarta que sea primo, ya que los primos no pueden dar division exacta, a no ser que se divida por 1 o el mismo. En caso contrario este seguiria siendo un posible numero primo, hasta terminarlo de dividir por cada numero que tengamos en el rango, ya que existiran numeros que posiblemente al principio no den division sin residuo, pero después si, esto dando a su vez un falso positivo, por lo que es mejor analizar cada numero de dicho rango hasta acabar la lista de posibles valores.


#obs. tal vez te confunda la operación "divisor**2 <= i" pero esto es equivalente a divisor <= raiz cuadrada de (i)", por simple ley de la desigualdad. Por lo que matemáticamente es correcto ya sea usar el primero o el segundo para nuestro algoritmo.
"""