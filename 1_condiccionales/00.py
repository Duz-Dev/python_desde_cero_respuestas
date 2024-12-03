"""
!Desarrolla un algoritmo para calcular el precio de venta de un articulo. Se tiene como datos, la descripción del articulo y el costo de producción, el precio de venta se calcula añadiéndole el costo de producción del 120% como utilidad y el 15% de impuesto de fabricación.
>>>Se imprimirá la descripción del articulo y el precio de venta.
"""

descripcion = input("Ingresar la descripción del artículo: ")
costo_produccion = float(input("Ingresar el costo de producción del artículo: "))

utilidad = costo_produccion * 1.20
impuesto_fabricacion = costo_produccion * 0.15  
precio_venta = costo_produccion + utilidad + impuesto_fabricacion

# Imprimir descripción del artículo y precio de venta
print(f"Descripción del artículo: {descripcion}")
print(f"Precio de venta: ${precio_venta:.2f}")
