"""
!Desarrolla un algoritmo que reciba las longitudes de los tres lados de un triángulo y determine si es equilátero, isósceles o escaleno. Además, verifica si los lados ingresados pueden formar un triángulo válido.
>>>Imprimir el tipo de triángulo o un mensaje indicando que no es un triángulo válido.
"""

#*variables
lado_a = 0.0
lado_b = 0.0
lado_c = 0.0
mensaje = ""

#*input
print(">>>Datos de entrada<<<")
lado_a = int(input("valor de lado a: "))
lado_b = int(input("valor de lado b: "))
lado_c = int(input("valor de lado c: "))

#*process
#?La solucion radica en usar el teorema de la desigualdad del triángulo, el cual establece que la suma de dos lados del triángulo siempre es mayor que la medida del tercer lado. Si esto resulta ser verdad para todas las tres combinaciones de las sumas, entonces tienes un triángulo.

if not((lado_a + lado_b > lado_c) and (lado_b + lado_c > lado_a) and (lado_c + lado_a > lado_b)):
    mensaje = "No es un triangulo valido"
else:
    if lado_a == lado_b == lado_c:
        mensaje = "equilatero"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        mensaje = "isósceles"
    else:
        mensaje = "escaleno"
#*output
print("\n-----Datos de salida--------")
print(f">>>El triangulo es: {mensaje}")
print("----------------------------")
