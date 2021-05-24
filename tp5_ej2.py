################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una funcion que permita obtener el n-esimo termino de la sucesión de Fibonacci.
#Siendo este número un entero positivo mayor a 2.
# 0 1 1 2 3 5 8 13 21 34 
from tp5_ej1 import ingreso_entero

def fibonacci(numero):
    sucesion = [0, 1]
    for i in range(numero - 1):
        sucesion.append(sucesion[-1] + sucesion[-2])
    return sucesion[-1]
    
        
def prueba():
    numero = ingreso_entero("Ingrese hasta qué número desea que llegue la serie mayor a 2: ")
    sucesion = fibonacci(numero)
    while numero < 3:
        print("El numero no es mayor a dos")
        numero = ingreso_entero("\nIngrese un numero correcto: ")
        sucesion = fibonacci(numero)
        
    print(f"El n-esimo termino de la sucesión de Fibonacci es: {sucesion}")

if __name__ == "__main__":
    prueba()
