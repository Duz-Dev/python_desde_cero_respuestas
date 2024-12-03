"""
!Dado un carácter alfanumérico, desarrolla un algoritmo para determinar si es una vocal o no es una vocal.
>>> Imprimir el carácter junto con el mensaje "es una vocal" o "no es una vocal".
?Restricciones
- No puedes utilizar métodos, funciones o módulos incorporados (built-in).
- Solo utilizando la estructura if-elif-else.
"""

#*variables
caracter = ""
mensaje = ""

#*input
print(">>>Datos de entrada<<<")
caracter = input("ingresa un caracter:").lower() #La entrada sera en minusculas

#*process

#?Solucion 1
# if (caracter == "a" or caracter == "e" or 
#     caracter == "i" or caracter== "o" or caracter == "u"):
#     mensaje = "es una vocal"
# else:
#    mensaje = "no es una vocal"

#?Solucion 2. Pythonica
if caracter in "aeiou":
    mensaje = "es una vocal"
else:
    mensaje = "no es una vocal"

#*output
print("-----Datos de salida--------")
print(f">>> '{caracter}' {mensaje}")
print("----------------------------")