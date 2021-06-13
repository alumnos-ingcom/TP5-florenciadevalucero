################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que determine si un numero entero positivo
#es un número perfecto.
from tp5_ej1 import ingreso_entero

def numero_perfecto(numero):
    suma = 0
    
    for i in range( 1, numero):
        if numero % i == 0:
            suma += i
    return suma


def prueba():
    numero = ingreso_entero("Ingrese un numero entero positivo para verificar si es perfecto: ")
    es_perfecto = numero_perfecto(numero)
    if numero == es_perfecto:
        print(f"El {numero} es un número perfecto")
    else:
        print(f"El {numero} no se trata de un número perfecto")

if __name__ == "__main__":
    prueba()

