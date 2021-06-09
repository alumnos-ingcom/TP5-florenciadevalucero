################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que que determine retornando True
#si un par de listas contienen los mismos elementos que pueden estar estén
# ubicados en diferentes posiciones.
from tp5_ej1 import ingreso_entero
 
def verificar(lista1, lista2):
    coinciden = 0
    longitud = len(lista1)
    for i in range(longitud):
        for j in range(longitud):
            if lista1[i] == lista2[j]:
                coinciden += 1
    if coinciden == longitud:
        return True
    else:
        return False

def prueba():
    cantidad = ingreso_entero("Ingrese la cantidad de elementos que van a tener sus listas: ")
    lista1 = []
    lista2 = []
    for i in range(cantidad):
        elementos = input("Ingrese el elemento de la lista: ")
        lista1.append(elementos)
    
    for i in range(cantidad):
        elementos2 = input("Ingrese los elementos de la segunda lista: ")
        lista2.append(elementos2)
    identificar = verificar(lista1, lista2)
    if identificar:
        print(f"La lista {lista1} es igual a la lista {lista2}")
    else:
        print(f"Las listas no son iguales")


if __name__ == "__main__":
    prueba()