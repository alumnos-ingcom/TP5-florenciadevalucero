################
# Florencia Lucero D'Eva - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# implementar una funcion que retorne una lista con todos los factoriones menores a 1.499.999

def factoriales(numero):
    iterador = 1
    factorial = 1
    while iterador < numero:
        factorial *= iterador + 1
        iterador += 1
    return factorial

def busqueda_factoriones():
    limite = 1499999
    factoriones = []

    for numero in range(limite):
        numero = str(numero)
        suma = 0
        for cifra in numero:
            cifra = int(cifra) #Pasamos a entero para poder buscar el factorial de la cifra
            factorial_digito= factoriales(cifra) #llamamos a la función para tener el factorial de la cifra
            suma = suma + factorial_digito #sumamos los factoriales
        suma = str(suma) #Volvemos a string para comparar
        if suma == numero:
            suma = int(suma)
            factoriones.append(suma)
    return factoriones

def prueba():
    lista_factoriones = busqueda_factoriones()
    print(f"Los factoriones encontrados son: {lista_factoriones} ")

if __name__ == "__main__":
    prueba()