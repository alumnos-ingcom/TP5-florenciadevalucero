################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que dado un texto y una palabra,
# retorne la ubicación de la palabra en el texto o una excepción
# si la palabra no forma parte del texto
from tp5_ej1 import IngresoIncorrecto

def busqueda(texto, palabra):
    lista_texto = texto.split()
    for i in range(len(lista_texto)):
        if lista_texto[i] == palabra:
            ubicacion = i+1
            return ubicacion
    raise IngresoIncorrecto(f"La palabra {palabra} no se encuentra en el texto")


def prueba():
    texto = input("Ingrese un texto: ")
    palabra = input("Ingrese la palabra que desea buscar en el texto: ")
    posicion= busqueda(texto, palabra)
    print(f" La palabra '{palabra}' se encuentra en la posicion: {posicion}")

if __name__ == "__main__":
    prueba()