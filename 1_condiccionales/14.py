"""
!Dado dos números enteros, desarrolla un algoritmo para determinar, si son iguales, se multiplicaran los dos números. Si el primer numero es mayor que el segundo, se restan los números; y si el primer número es menor que el segundo número, se sumaran ambos.
>>>Imprime la multiplicación, o la resta, o la suma.
"""

#*variables
num_1 = 0
num_2 = 0
resultado = 0

#*input
print(">>>Datos de entrada<<<")
num_1 = int(input("Ingresa el primer numero: "))
num_2 = int(input("Ingresa el segundo numero: "))

#*process
if num_1 == num_2:
    resultado = num_1 * num_2
elif num_1 > num_2:
    resultado = num_1 - num_2
else:
    resultado = num_1 + num_2

#*output
print("\n-----Datos de salida--------")
print(f">>> El resultado es:",resultado)
print("----------------------------")
