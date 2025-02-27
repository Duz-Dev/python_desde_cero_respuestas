"""
!Una compañía de taxis cobra una tarifa base de $50.00, más una tarifa por kilómetro recorrido y una tarifa adicional por tráfico pesado. Las tarifas son las siguientes:

!    $10.00 por kilómetro si la distancia es menor a 10 km.
!    $8.00 por kilómetro si la distancia está entre 10 km y 50 km.
!    $5.00 por kilómetro si la distancia es mayor a 50 km.
!    Se añade una tarifa adicional de $20.00 si el tráfico es pesado.

!Desarrolla un algoritmo que calcule e
>>>imprima el costo total del viaje en taxi.
"""

#*variables
recorrido = 0.0 #kilometros recorridos
tarifa = 50 #la tarifa base es $50
trafico = ""

#*input
print(">>>Datos de entrada<<<")
recorrido = float(input("kilometros recorridos: "))
trafico = input("el trafico fue pesado[s/n]: ").lower()

#*process
if recorrido < 10:
    tarifa += (10 * recorrido)
elif recorrido <= 50:
    tarifa += (8 * recorrido)
else:
    tarifa += (5 * recorrido)

if trafico == "s": #Evaluo si el trafico estuvo pesado, entonces la tarifa se le suma 20
    tarifa += 20

#*output
print("\n-----Datos de salida--------")
print(f">>>El total a cobrar es: ${tarifa:.2f}")
print("----------------------------")