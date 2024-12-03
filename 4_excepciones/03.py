
#!Ejercicio 3: Calcular el área de un triángulo
""" 
Escribe un programa que calcule el área de un triángulo. Pide al usuario ingresar la base y la altura. Si el usuario ingresa un valor no numérico o negativo, el programa debe capturar la excepción y mostrar un mensaje que indique que solo se aceptan números positivos. La fórmula del área del triángulo es: Área = (base * altura) / 2.

"""
#*variables
base = 0
altura = 0
area = 0

#*input
print(">>>Datos de entrada<<<")
try:
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    #Validando que sean positivos o da error
    if base < 0 or altura < 0:
        raise TypeError("[ERROR]-> No se admiten valores negativos, solo positivos")
    
#Muestra error en caso de no ingresar números
except ValueError:
    print("[ERROR]-> Datos no validos")
except TypeError as e:
    print(e)

#*process
#Calculando area    
area = (base * altura) / 2

#*output
print("\n-----Datos de salida--------")
print(f">>>Area : {area}")
print("----------------------------")