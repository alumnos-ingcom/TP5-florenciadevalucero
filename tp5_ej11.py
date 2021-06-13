################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una función que obtenga una lista con el promedio móvil de otra lista con números enteros.
'''Para calcular la media ponderada hay que asignar un peso a los distintos valores que se van a tomar para
obtener dicha media. La suma de todos los valores por sus pesos se divide finalmente
por la suma de todos los pesos y se obtiene la media ponderada.
'''
from tp5_ej1 import ingreso_entero
def promedio_movil(numeros, peso):
    suma = 0
    suma_pesos = 0
    longitud = len(numeros)
    for i in range(longitud):
        multiplicacion= numeros[i] * peso
        suma += multiplicacion
        suma_pesos += peso
    promedio = suma / suma_pesos
    return promedio


def prueba():
    cantidad = ingreso_entero("Ingrese la cantidad de numeros que desea sacar el promedio móvil: ")
    peso = ingreso_entero("Ingrese el peso por el que se multiplicará cada valor que se sacará el promedio: ")
    numeros_ingresados = []
    for i in range(cantidad):
        numeros = ingreso_entero("Ingrese los números para sacar el promedio móvil: ")
        numeros_ingresados.append(numeros)
    resultado = promedio_movil(numeros_ingresados, peso)
    print(f"El promedio móvil de {numeros_ingresados} es: {resultado}")

if __name__ == "__main__":
    prueba()