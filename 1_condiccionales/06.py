"""
!Dado un numero entero de tres cifras, desarrolla un algoritmo para verificar que efectivamente sean 3 cifras e invertir el numero de entrada.
>>>Imprime el numero invertido
?Restricciones:
- No utilizar listas ni tuplas
- No utilizar funciones built-in, ni módulos
- Solo utiliza procesos lógicos y matemáticos
"""
#*variables
unidad = 0
decena = 0
centena = 0
numero_invertido = 0


#*input
numero = int(input("Introduce un número entero de tres cifras: "))

#*process
if 100 <= numero <= 999:
    centena = numero // 100        
    decena = (numero // 10) % 10  
    unidad = numero % 10           

    numero_invertido = (unidad * 100) + (decena * 10) + centena

else:
    print("El número no tiene tres cifras.")


#*output
print(f"Numero inverso: {numero_invertido}")
