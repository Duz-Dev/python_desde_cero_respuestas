#Ejercicio 8
#!Se quiere saber cuál es el estado con mayor poblacion en mexico. Para ello se sabe que son 32 estados, pero para la muestra se tomaron 16 de estos. Se tiene una lista con la siguiente informacion:
poblacion = {
    "Morelos": 1971520,
    "Nayarit": 1282323,
    "Nuevo León": 5611357,
    "Oaxaca": 4132148,
    "Puebla": 6583278,
    "Querétaro": 2279637,
    "Quintana Roo": 1975530,
    "San Luis Potosí": 2966321,
    "Sinaloa": 3026943,
    "Sonora": 2954915,
    "Tabasco": 2395272,
    "Tamaulipas": 3650604,
    "Tlaxcala": 1342977,
    "Veracruz": 8112505,
    "Ciudad de México": 9209944,
    "Zacatecas": 1622138
}
#!Con esto, muestra el estado y el numero de habitantes en un formato dividido por centenas, Ejemplo "El estado con mayor poblacion es 'sonora' con 2,423,212 habitantes".
#!Muestra el estado con menor poblacion y el que tiene un valor mas secano al promedio entre todos los estados.

#*variables
estado_mayor = ["Morelos", 1971520] #nombre y habitantes del estado con mayor población
estado_menor = ["Morelos", 1971520] #Nombre y habitantes del estado con menor poblacion
estado_prom = ['',0] #Nombre y habitantes del estado con la poblacion mas cercana al promedio.
poblacion_total = 0

diferencia_actual = 0 # Sacamos cuanto es la resta entre cada numero de habitantes y el promedio de la poblacion
diferencia_minima = float('inf') # comparamos que diferencia es la mas chica con respecto a la actual. Es importante especificar que sea un valor infinito, de esta forma nos aseguramos que la primera comparación en nuestro algoritmo se cumpla siempre sin resistencia.

poblacion = {
    "Morelos": 1971520,
    "Nayarit": 1282323,
    "Nuevo León": 5611357,
    "Oaxaca": 4132148,
    "Puebla": 6583278,
    "Querétaro": 2279637,
    "Quintana Roo": 1975530,
    "San Luis Potosí": 2966321,
    "Sinaloa": 3026943,
    "Sonora": 2954915,
    "Tabasco": 2395272,
    "Tamaulipas": 3650604,
    "Tlaxcala": 1342977,
    "Veracruz": 8112505,
    "Ciudad de México": 9209944,
    "Zacatecas": 1622138
}

#*process

for estado in poblacion.items(): #Dividimos por listas los estados junto con su poblacion

#comparamos el valor de los habitantes para verificar cual es el mayor y el menor de todos estos
    if estado_mayor[1] < estado[1]:
        estado_mayor = estado
    if estado_menor[1] > estado[1]:
        estado_menor = estado
    
    poblacion_total += estado[1]

#Promedio de la poblacion en los 16 estados de muestra
poblacion_prom = poblacion_total / 16

for estado in poblacion.items():
    #calculamos el valor absoluto entre poblacion_prom y cada estado
    diferencia_actual = abs(estado[1]-poblacion_prom)
    #Comparamos que diferencia es la mas chica entre las diferencias obtenidas
    if diferencia_actual < diferencia_minima:
        diferencia_minima = diferencia_actual
        estado_prom = estado

# * Resultados
print("\n----- Datos de salida --------")
print(f"Estado con mayor población: {estado_mayor[0]} ({estado_mayor[1]} habitantes)")
print(f"Estado con menor población: {estado_menor[0]} ({estado_menor[1]} habitantes)")
print(f"Población promedio: {poblacion_prom:.2f} habitantes")
print(f"Estado más cercano al promedio: {estado_prom[0]} ({estado_prom[1]} habitantes)")
print("-------------------------------")


#?Nota. Tal vez para este algoritmo nacieron muchas dudas. Te aconsejo que preguntes en la comunidad de discord previamente.

#?En este algoritmo vi que lo menos intuitivo era saber de que manera podriamos saber que estado es el mas cercano al promedio. Para ello recurrimos otra vez a las matematica, pero esta vez fue mas simple. En este caso solo era comprender un elemento clave y era que buscabamos un valor lo mas cercano al promedio. Dicho esto, supongamos que tenemos un valor N el cual es igual al promedio PROM (PROM == N) y si restamos estos numeros sabremos que el resultado seria cero. Entonces si encontraramos un numero que su valor sea digamos una unidad menos N-1 y la restamos veremos que el resultado seria PROM - N = -1  Esto nos ayuda a comprender un principio y es que entre que mas cercas este el resultado de tal diferencia a el cero, dicho N sera el mas cercano al promedio.

#! En este caso como nos importa el valor en si, para evitar problemas de comparacion, haremos que sea positivo siempre. En las matematicas ya existe una herramienta llamada "Valor absoluto" el cual hace que todo valor resultante de este siempre sea positivo. Esto es lo que necesitamos. 

#?Apartir de estos dos puntos mencionados solo basta comparar las diferencias entre la poblacion de cada estado con el promedio que calculamos. Y dicha diferencia (diferencia es sinonimo de resta) la calculamos dentro de un valor absoluto. Posteriormente hay que comparar para evaluar cual es el valor mas chico obtenido y sabiendo esto, sabremos a su vez que estado es el mas sercano al promedio. 

#!OBS. Tal vez te de curiosidad porque "diferencia_minima = float('inf') " y esto se debe a que es mas robusto, intuitivo y confiable porque no depende de valores arbitrarios y siempre garantiza que el algoritmo actualice correctamente la diferencia mínima. Siempre funcionara el algoritmo sin contratiempos si usamos este valor. Al contrario de si le damos un valor de diccionario, ejemplo "diferencia_minima = poblacion["Morelos"]  # O cualquier otro estado" 
""" 
El algoritmo solo podria funcionar, si se cumple los siguientes dos puntos:

*Garantizas que las poblaciones en el diccionario son correctas y completas. Por ejemplo, si todos los estados tienen valores válidos y positivos, entonces siempre habrá una población con una diferencia menor que el valor inicial.

*No hay valores extremos o situaciones inesperadas. Si el promedio está dentro del rango de las poblaciones (lo que normalmente ocurre), entonces cualquier población inicial podría ser eventualmente reemplazada por la población más cercana al promedio.
"""
# En resumen a este ultimo punto, Es por buenas practicas :v