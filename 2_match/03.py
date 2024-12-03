"""
*Tarifas de Envío:
   - Una empresa de envíos cobra tarifas diferentes según el peso del paquete:
     - Menos de 1 kg: $5
     - 1-5 kg: $10
     - 6-10 kg: $15
     - Más de 10 kg: $20
   - Desarrolla un algoritmo que permita la entrada del peso del paquete y calcule la tarifa de envío correspondiente.
"""

#*variables
peso_paq = 0.0 # pedida del peso peso del paquete
tarifa = 0.0 # tarifa a indicar

#*input
print(">>>Datos de entrada<<<")
peso_paq = float(input("Ingresa el peso del paquete: "))

#*process

match peso_paq:
    case x if 0 <= peso_paq < 1:
      tarifa = 5
    case x if 1 <= peso_paq <= 5:
      tarifa = 10
    case x if 6 <= peso_paq <= 10:
      tarifa = 15
    case x if peso_paq > 10:
      tarifa = 20
    case _ :
      print("se ingreso un dato no esperado")      
#*output
print("\n-----Datos de salida--------")
print(f">>>Precio final de la tarifa: {tarifa}")
print("----------------------------")