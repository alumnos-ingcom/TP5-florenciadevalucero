################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escriba una funcion que determine la distancia entre dos números.
def ingreso_numero(mensaje):
    ingreso = input(mensaje + "# ")
    try:
        numero = float(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return numero


def distancia(numero, numero2):
    if numero < numero2:
        determinar_distancia = numero2 - numero
        return determinar_distancia
    else:
        determinar_distancia = numero - numero2
        return determinar_distancia
        


def prueba():
    numero = ingreso_numero("Ingrese el primer número: ")
    numero2 = ingreso_numero("Ingrese el otro número para determinar la distancia: ")
    resultado = distancia(numero, numero2)
    print(f"La distancia entre {numero} y {numero2} es: {resultado} unidades de distancia")


if __name__ == "__main__":
    prueba()