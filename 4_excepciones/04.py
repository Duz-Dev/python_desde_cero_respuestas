
#!Ejercicio 4: Leer de un archivo
""" 
Escribe un programa que intente leer el contenido de un archivo. Si el archivo no existe, el programa debe mostrar un mensaje de error informando que el archivo no fue encontrado. Si ocurre otro error al intentar abrir el archivo (por ejemplo, permisos), debe mostrar un mensaje genérico de error.

"""
try:
    with open("Texto.txt", 'r') as archivo:
        pass
except FileNotFoundError:
    print("[ERROR]. El archivo que se intento leer no existe")
except Exception as e:
    print("[ERROR]",e)

