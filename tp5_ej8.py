################
# Florencia Lucero D'Eva - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
#Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
from tp5_ej1 import ingreso_entero

def codificacion(posicion, texto):
    lista_codificar = []
    
    for letra in texto:
        entero_letra = ord(letra)
        entero_letra_modificada = entero_letra + posicion
        
        if (entero_letra_modificada > 122): #Códo ascii: 122= z
            entero_letra_modificada = entero_letra_modificada - 26
            
        elif (entero_letra_modificada > 90) and (entero_letra_modificada < 97): #90= Z , 97= a
            entero_letra_modificada = entero_letra_modificada - 26 # 90 - 26 = A  
            
        elif entero_letra_modificada > 57 and entero_letra_modificada < 65: # 57= 9, 65= A
            entero_letra_modificada = entero_letra_modificada - 10
            
        letra_modificada = chr(entero_letra_modificada)
        lista_codificar.append(letra_modificada)
    texto = "".join(lista_codificar)
    return texto
        

def decodificacion(texto, posicion):
    lista_codificar = []
    
    for letra in texto:
        entero_letra = ord(letra)
        entero_letra_modificada = entero_letra - posicion
        
        if (entero_letra_modificada < 97) and (entero_letra_modificada > 90):
            entero_letra_modificada = entero_letra_modificada + 26
            
        elif (entero_letra_modificada < 65) and (entero_letra_modificada > 57):
            entero_letra_modificada = entero_letra_modificada + 26
            
        elif (entero_letra_modificada < 48): # 48 = 0
            entero_letra_modificada = entero_letra_modificada + 10
            
        letra_modificada = chr(entero_letra_modificada)
        lista_codificar.append(letra_modificada)
    texto = "".join(lista_codificar)
    return texto

def prueba():
    texto = input("Ingrese el mensaje que desea codificar: ")
    posicion = ingreso_entero("Ingrese el número que desea que se roten las letras en el Cifrado de César: ")
    codificado = codificacion(posicion, texto)
    decodificado = decodificacion(codificado, posicion)
    print(f" El mensaje codificado es: {codificado}")
    print(f" El mensaje decodificado es: {decodificado}")
    

if __name__ == "__main__":
    prueba()