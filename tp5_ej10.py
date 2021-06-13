################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una funcion que dado un numero entero positivo,
#retorne una cadena de texto con su representación binaria.
#Implementar una funcion que haga el proceso inverso

from tp5_ej1 import ingreso_entero

def cadena_binario(numero):
    lista_binario = []
    while numero >= 1:
        resto = numero % 2
        resto = str(resto)
        lista_binario.insert(0, resto)
        numero = numero // 2
          
    cadena = "".join(lista_binario)
    return(cadena)
    
def  entero(cadena):
    '''Para pasar numero binario a entero:multiplicar cada dígito del número binario por 2 elevado a
        la posición del dígito teniendo en cuenta que las posiciones, de derecha a izquierda,
        son 0, 1, 2, etc. Finalmente se suma el resultado de todas las multiplicaciones.'''
    exponente = (len(cadena)) - 1
    longitud = len(cadena)
    suma = 0
    for i in range(longitud):
        digito = int(cadena[i])
        conversion = digito *(2 ** (exponente - i))
        suma = suma + conversion 
    return suma
    

def prueba():
    numero = ingreso_entero("Ingrese un número para representarlo en su cadena binaria: ")
    binario = cadena_binario(numero)
    print(f"La representación de {numero} en binario es: {binario}")
    
    numero_binario =input("Ingrese una cadena en binario para representarla en número entero: ")
    numero_entero= entero(numero_binario)
    print(f"El número binario {numero_binario} es el número decimal {numero_entero}")
    
    

if __name__ == "__main__":
    prueba()