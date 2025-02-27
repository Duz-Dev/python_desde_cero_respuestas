"""
*Ejercicio: Calcular Aumento Salarial en la Compañía ACME

!Descripción:
La compañía ACME desea calcular el aumento de sueldo de sus trabajadores según las siguientes condiciones basadas en la categoría del trabajador:

1. Si el trabajador tiene categoría 1, se le aplica un aumento del 20%.
2. Si el trabajador tiene categoría 2, se le aplica un aumento del 15%.
3. Si el trabajador tiene categoría 3, se le aplica un aumento del 13%.
4. Si el trabajador tiene categoría 4, se le aplica un aumento del 12%.

?Requisitos:
Desarrolla un algoritmo que permita la entrada de los siguientes datos:
1. Clave del trabajador
2. Nombre del trabajador
3. Categoría del trabajador
4. Sueldo nominal del trabajador

El algoritmo debe calcular el aumento de sueldo de acuerdo con las condiciones dadas. Además, debe imprimir la clave y el nombre del trabajador, su categoría, el sueldo nominal y el sueldo después de impuestos (ISR = 35%).

?Puntos a considerar:
- Queda a disposición del estudiante.
- No usar ciclos, funciones o módulos.

?Ejemplo de salida esperada:
>>Nomina Compañía ACME<<
Clave del trabajador: 12345
Nombre del trabajador: Juan Pérez
Categoría: 2
Sueldo nominal: $10,000.00
Sueldo después de aumento: $11,500.00
Sueldo después de impuestos: $7,475.00
>> generado el dia: x/x/x
"""

#*variables
#datos del trabajador
clave_ = 0
nombre = ""
categoria = 0 # 1 | 2 | 3 | 4 
sueldo_base = 0.0 # sueldo original ingresado
sueldo_incremento = 0.0 # sueldo pos incremento
pago = 0.0 # sueldo pos impuesto e incremento
aumento = 0.0 # aumento decimal del incremento
impuesto = 0.16

#*input
print(">>>Datos de entrada<<<")
nombre = input("Nombre del trabajador: ")
clave = int(input("Clave del trabajador: "))
categoria = int(input("Categoria del trabajador: "))
sueldo_base = float(input("Sueldo base: "))

#*process
match categoria:
    case 1 :
        aumento = 1.20 # 20%
    case 2:
        aumento = 1.15 # 15%
    case 3:
        aumento = 1.13 # 13%
    case 4:
        aumento = 1.12 # 12%
    
sueldo_incremento = sueldo_base * aumento

pago = sueldo_incremento - (sueldo_incremento * impuesto)


#*output
print("\n\n>>Nomina Compañía ACME<<")
print(f"Clave del trabajador: {clave}")
print(f"Nombre del trabajador: {nombre}")
print(f"Categoría: {categoria}")
print(f"Sueldo nominal: {sueldo_base}")
print(f"Sueldo después de aumento: {sueldo_incremento}")
print(f"Sueldo después de impuestos: {pago}")
print("generado el dia: x/x/x")
print("----------------------------")