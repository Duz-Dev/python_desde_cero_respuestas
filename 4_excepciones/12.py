"""
!Evaluación de Préstamos Bancarios
* Imagina que trabajas en el área de préstamos de un banco, y tu tarea es evaluar si un cliente es elegible para un préstamo. Para esto, el cliente debe cumplir ciertas condiciones:

Ingresos anuales: Deben ser mayores a $20,000. Si los ingresos son menores, lanza una excepción IngresoInsuficienteError.
Historial crediticio: El usuario debe ingresar "bueno" o "malo". Si el valor ingresado no es válido, lanza una excepción HistorialInvalidoError.
Cantidad solicitada: No puede ser mayor al 40% de sus ingresos anuales. Si es mayor, lanza una excepción CantidadSolicitadaExcesiva.
Tareas:

Escribe una función que tome estos datos y determine si el cliente es elegible o no.
Utiliza try y except para capturar errores y mostrar mensajes de advertencia en cada caso.
Al final, si todos los datos son válidos, el programa debe imprimir “Préstamo aprobado” o “Préstamo denegado” en función de los ingresos y el historial.
Salida esperada:

El sistema debe informar al usuario cada vez que no cumpla con una condición y permitirle intentarlo nuevamente.
El resultado final debe ser un mensaje que indique si el préstamo fue aprobado o denegado.

"""
class IngresoInsuficienteError(Exception):
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f"Ingreso insuficiente: ${self.valor}")

class HistorialInvalidoError(Exception):
    def __init__(self, historial):
        super().__init__(f"Historial inválido: {historial}")

class CantidadSolicitadaExcesiva(Exception):
    def __init__(self, cantidad, max_permitido):
        super().__init__(f"Cantidad solicitada no permitida: ${cantidad}. Máximo permitido: ${max_permitido}")

# Variables para almacenar datos del usuario
ingreso_anual = 0
historial_crediticio = ""
cantidad = 0
prestamo_aprobado = False  # Estado inicial

try:
    # Entrada de datos
    ingreso_anual = float(input("Ingresos anuales: "))
    if ingreso_anual < 20_000:
        raise IngresoInsuficienteError(ingreso_anual)
    
    historial_crediticio = input("Historial crediticio [bueno/malo]: ").lower()
    if historial_crediticio not in ["bueno", "malo"]:
        raise HistorialInvalidoError(historial_crediticio)
    
    cantidad = float(input("Cantidad a solicitar: "))
    max_cantidad = ingreso_anual * 0.4
    if cantidad > max_cantidad or cantidad <= 0:
        raise CantidadSolicitadaExcesiva(cantidad, max_cantidad)
    
    # Si todas las condiciones se cumplen
    prestamo_aprobado = True

except ValueError:
    print("ERROR: Entrada no válida. Asegúrate de ingresar números correctos.")
except Exception as e:
    print("Error.",e)

if prestamo_aprobado:
    if historial_crediticio == "bueno":
       print("Préstamo aprobado.")
    else:
        print("Préstamo aprobado con restricciones por historial crediticio.")
else:
    print("Préstamo denegado.")
