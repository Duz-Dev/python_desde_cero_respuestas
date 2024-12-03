"""
!Sistema de Reseñas de Productos
* Estás diseñando un sistema de reseñas para una tienda en línea. Cada usuario puede dejar una reseña para un producto, pero debes validar que las reseñas cumplan con ciertas condiciones:

Puntuación del producto: Debe ser un número entre 1 y 5. Si el usuario ingresa un número fuera de este rango, lanza una excepción PuntuacionInvalida.
Comentario: Debe tener al menos 15 caracteres. Si el comentario es demasiado corto, lanza una excepción ComentarioCortoError.
ID del producto: Debe ser un número entero positivo. Si el ID no es válido, lanza una excepción IDProductoInvalido.
Tareas:

Utiliza try, except, y finally para gestionar errores y, al final, confirmar si la reseña fue guardada.
Almacena las reseñas válidas en una lista reseñas.
Salida esperada:

El programa debe mostrar mensajes de error cada vez que un campo no cumpla con los requisitos.
Si la reseña es válida, se guarda en la lista y muestra un mensaje de confirmación.
"""

class PuntuacionInvalida(Exception):
    pass
class ComentarioCortoError(Exception):
    pass
class IDProductoInvalido(Exception):
    pass

#*variables
puntuacion = 0
comentario = ""
id_producto = 0
reseña = {"puntuacion": puntuacion,
         "comentario": comentario,
         "id_producto": id_producto,}
reseñas = []

while True:
    try:
        #*input
        print(">>>Ingresa una reseña<<<")
        puntuacion = int(input("ingresa una puntación [1-5]: "))
        comentario = input("Ingresa un comentario: ")
        id_producto = int(input("Ingresa la id del producto: "))

        #Validaciones
        if not(1<= puntuacion <= 5):
            raise PuntuacionInvalida("Puntuacion no valida. Debe ser entre 1 y 5")
        if len(comentario) < 15:
            raise ComentarioCortoError("Comentario corto. Debe ser mayor a 15 caracteres")
        if id_producto < 1:
            raise IDProductoInvalido("El id del producto no es valido")
        
        # Si pasa todas las validaciones, guardamos la reseña
        reseña = {
            "puntuacion": puntuacion,
            "comentario": comentario,
            "id_producto": id_producto,
        }
        reseñas.append(reseña)
        print("Reseña guardada con éxito.")

    except ValueError:
        print("Error: Ingresaste un tipo de dato no válido. Intenta nuevamente.")
    except (PuntuacionInvalida, ComentarioCortoError, IDProductoInvalido) as e:
        print(f"Error: {e}")

    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas ingresar otra reseña? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Mostrar todas las reseñas al final
print("\n----- Reseñas Guardadas -----")
for i, reseña in enumerate(reseñas, start=1):
    print(f"Reseña #{i}: {reseña}")
print("----------------------------")