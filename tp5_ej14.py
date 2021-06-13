################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que determine si un numero entero positivo es capicúa.
from tp5_ej1 import ingreso_entero
def capicua(numero):
    if str(numero) == str(numero)[::-1]:
        return True
    else:
        return False

def prueba():
    numero = ingreso_entero("Ingrese un número entero positivo para verificar si es capicua: ")
    verificar = capicua(numero)
    if verificar:
        print(f"El número {numero} es capicua")
    else:
        print(f"El número {numero} no es capicua")

if __name__ == "__main__":
    prueba()