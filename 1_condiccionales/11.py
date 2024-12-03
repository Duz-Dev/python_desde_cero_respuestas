"""
!Dado un numero entero, desarrolla un algoritmo para determinar si el numero es positivo, negativo o no tiene magnitud.
>>>Imprime el numero con el texto "positivo", "negativo" o "no tiene magnitud" cual sea su caso.
"""

#*variables
num = 0
smg = "" #Mensaje de la magnitud del numero

#*input
print(">>>Ingrese el numero<<<")
num = int(input(">>> "))

#*process
if num > 0:
    smg = "positivo"
elif num == 0:
    smg = "no tiene magnitud"
else:
    smg = "negativo"

#*output
print("-----Datos de salida--------")
print(f"El numero es: {smg}")
print("----------------------------")