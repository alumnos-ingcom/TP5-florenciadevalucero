################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una función que determine si una cadena con parentesis está balanceada.

def balanceada(cadena):
    cadena = []
    apertura = 0
    balanceo = True
    
    for caracter in cadena:
        if apertura >= 0:
            if caracter == "(" or caracter == "[" or caracter == "{":
                apertura += 1
            elif caracter == ")" or caracter == "]" or caracter == "}":
                apertura -= 1
        else:
            balanceo = False
    if apertura > 0:
        balanceo = False
    return balanceo
        

def prueba():
    cadena = input("Ingrese un texto que incluya paréntesis: ")
    
    verificar = balanceada(cadena)
    
    if verificar:
        print(f" La cadena {cadena} esta balanceada")
    else:
        print(f"La cadena {cadena} no está balanceada")


if __name__ == "__main__":
    prueba()