""" 
!Ejercicio: Verificación de Archivo de Configuración
Descripción: Imagina que tu programa depende de un archivo de configuración llamado config.txt. Crea un programa que intente abrir este archivo y valide que contenga ciertos datos necesarios para que el programa funcione correctamente. El archivo debe contener el texto clave=valor

Si el archivo config.txt no existe, el programa debe capturar la excepción FileNotFoundError y crear un archivo nuevo con datos predeterminados.
Si el archivo existe pero está vacío o incompleto, el programa debe capturar una excepción personalizada llamada ConfiguracionInvalidaError.
En el caso de que el archivo esté completo, el programa debe leer y mostrar el contenido del archivo.
>>>Pistas:Considera un bloque finally para cerrar el archivo en caso de que haya sido abierto.

"""
class ConfiguracionInvalidaError(Exception):
    pass

try:
    with open("config.txt", 'r') as config:
        contenido = config.read()
        if not contenido:
            raise ConfiguracionInvalidaError("La configuracion del archivo es incorrecta")
        
        if "clave" not in contenido or "valor" not in contenido:
            raise ConfiguracionInvalidaError("Datos de configuracion incorrectos o invalidos")
        
        print("Contenido del archivo: ")
        print(contenido)

except FileNotFoundError:
    print("Archivo no encontrado, se creara uno")
    with open("config.txt", "w") as config:
        config.write("clave=valor\n")

except ConfiguracionInvalidaError as e:
    print(f"Error: {e}")
