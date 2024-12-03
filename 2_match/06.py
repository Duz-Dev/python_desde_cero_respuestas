"""
*Sistema de Puntos en una Tienda de Ropa:

    Una tienda de ropa tiene un sistema de puntos para sus clientes frecuentes. Cada cliente recibe puntos por cada compra que realiza. Los puntos se pueden canjear por descuentos en compras futuras. La tienda ofrece las siguientes opciones:
        Si el cliente tiene más de 1000 puntos, recibe un 20% de descuento.
        Si el cliente tiene entre 500 y 1000 puntos, recibe un 10% de descuento.
        Si el cliente tiene menos de 500 puntos, no recibe descuento.
        Además, si el cliente realiza una compra los martes, recibe un descuento adicional del 5%.
    Desarrolla un programa que pida el nombre del cliente, el día de la semana, el número de puntos y el monto de la compra. El programa debe calcular el descuento aplicable y mostrar el total a pagar después de aplicar los descuentos.
"""

#*variables
nombre = "" # nombre del cliente
fecha = "" # dia de la semana
puntos = 0 # puntos obtenidos
subtotal = 0.0 # monto de la compra antes de descuento
descuento = 0.0 # descuento en formato decimal
descuento_cantidad = 0.0 # cantidad monetaria a descontar
total = 0.0 # total a pagar


#*input
print(">>>Datos de entrada<<<")
nombre = input("Nombre del cliente: ")
fecha = input("Fecha de compra: ")
puntos = int(input("puntos del cliente: "))
subtotal = float(input("monto de los artículos: "))

#*process

#descuento
match puntos:
    case x if x > 1000: #recuerda que en todo momento x esta tomando el valor del dato a evaluar, en este caso "puntos"
        descuento = 0.20 # 20%
    case x if 500 <= x <= 1000:
        descuento = 0.10 # 10%
    case x if x < 500:
        descuento = 0
    case _:
        print("dato no valido")
        
#calculo del descuento
descuento_cantidad = subtotal * descuento
total = subtotal - descuento_cantidad

#*output
print("\n-----Datos de salida--------")
print(f"Fecha | {fecha}")
print(f"Nombre cliente | {nombre}")
print(f"Subtotal | ${subtotal}")
print(f"descuento de {int(descuento * 100)}% | ${descuento_cantidad}")
print(f"TOTAL:: ${total}")
print("----------------------------")
