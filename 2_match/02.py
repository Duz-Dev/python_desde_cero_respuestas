"""
*Descuentos en Tienda:
   Una tienda ofrece descuentos según la cantidad de productos comprados:
    1-5 productos: 5% de descuento
    6-10 productos: 10% de descuento
    11-20 productos: 15% de descuento
    Más de 20 productos: 20% de descuento
    Desarrolla un algoritmo que permita la entrada del nombre del cliente, la cantidad de productos comprados y el precio total antes del descuento. Calcula el precio final con el descuento aplicado.
"""

#*variables

nombre = "" #nombre cliente
n_productos = 0 # cantidad de productos a comprar
subtotal = 0.0 # precio antes de descuento
total = 0.0 # precio post descuento
descuento = 0 # cantidad decimal a descontar 
desc_cant = 0.0 # cantidad de descuento monetario
desc_str = '' # descuento porcentual de forma simbólica | 5% | 10% ..

#*input
print(">>>Datos de entrada<<<")

nombre = input("Nombre del cliente: ")
n_productos = int(input("cantidad de productos: "))
subtotal = float(input("Precio a cobrar: "))

#*process

match n_productos:
    case x if 1 <= n_productos <= 5:
        descuento = 0.05
    case x if 6 <= n_productos <= 10:
        descuento = 0.10
    case x if 11 <= n_productos <= 20:
        descuento = 0.15
    case x if n_productos > 20:
        descuento = 0.20

#calculo del subtotal
desc_cant = subtotal * descuento
total = subtotal - desc_cant
desc_str = str(int(descuento * 100)) + "%"


#*output
print("\n-----Datos de salida--------")
print(f">>>Cliente: {nombre}")
print(f">>>Subtotal: {subtotal}")
print(f">>>Descuento {desc_str} : {desc_cant}")
print(f">>>Total a pagar: {total}")
print("----------------------------")