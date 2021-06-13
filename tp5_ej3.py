################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que permita obtener el n-esimo termino de la suceción Tribonacci,
#siendo este termino un numero entero positivo mayor a 3.
#1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, 2209, 40
from tp5_ej1 import ingreso_entero

def trifibonacci(numero):
    sucesion = [1, 1, 1]
    for i in range(numero - 2):
        sucesion.append(sucesion[-1] + sucesion[-2] + sucesion[-3])
    return sucesion[-1]
    
    
    
def prueba():
    numero = ingreso_entero("Ingrese hasta donde quiere que llegue la serie, que sea un numero mayor a 3:")
    termino = trifibonacci(numero)
    while numero < 4:
        print("El número ingresado no es mayor a 3")
        numero = ingreso_entero("\nIngrese un número correcto: ")
        termino = trifibonacci(numero)
    print(f"El n-esimo termino de la sucecion Trifibonacci es: {termino}")
    
    

if __name__ == "__main__":
    prueba()
