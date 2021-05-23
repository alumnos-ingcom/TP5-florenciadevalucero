################
# Lucero D'Eva Florencia - @florenciadevalucero
# Plantilla de ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que retorne True cuando un número
#entero es par y False cuando no lo sea, sin utilizar módulo. (%)
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""


def ingreso_entero(mensaje):
    ingreso = input(mensaje + "# ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def numero_par(entero):
    if entero >= 0:
        while entero > 0:
            entero = entero - 2
        return entero
        
    else:
        while entero < 0:
            entero = entero + 2
        return entero
        

def prueba():
    mensaje = ("Ingrese un numero para verificar si es par o no: ")
    numero = ingreso_entero(mensaje)
    verificar = numero_par(numero)
    if verificar == 0:
        print(f" El {numero} es un numero par")
    else:
        print(f"El {numero} no es un numero par")
    

if __name__ == "__main__":
    prueba()