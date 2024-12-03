"""
!Desarrolla un algoritmo que lea un carácter cualquiera desde el teclado, y muestre el mensaje "Es una MAYÚSCULA" cuando el carácter sea una letra mayúscula y el mensaje "Es una MINÚSCULA" cuando sea una minúscula. Cuando se ingrese un carácter que no sea un carácter, muestra el mensaje "No es una letra". Recuerda que debe ser valido el carácter eñe para este ejercicio.
"""

#*variables
caracter = ""
mensaje = ""

#*input
print(">>>Datos de entrada<<<")
caracter = input("Ingrese el caracter: ")

#*process
#?metodo 1
#!Este metodo no funciona, ya que si le aplicamos el upper o lower a un elemento que no es un caracter, este seguiria siendo igual a el mismo, por ende, siempre todo aquello que no sea un caracter seria evaluado como "mayuscula".ñ
# if caracter == caracter.upper():
#     mensaje = "Es una MAYÚSCULA"
# elif caracter == caracter.lower():
#     mensaje = "Es una MINÚSCULA"
# else:
#     mensaje = "No es una letra"

#?Metodo 2
if "a" <= caracter <= "z" or caracter == "ñ":
    mensaje = "Es una MINÚSCULA"
elif "A" <= caracter <= "Z" or caracter == "Ñ":
    mensaje = "Es una MAYÚSCULA"
else:
    mensaje = "No es una letra"

#*output
print("\n-----Datos de salida--------")
print(f">>>{mensaje}")
print("----------------------------")