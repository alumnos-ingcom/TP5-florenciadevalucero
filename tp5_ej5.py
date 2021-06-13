################
# Lucero D'eva Florencia - @florenciadevalucero
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una funcion que dada un texto, deje en minuscula
#lo que esté en mayuscula y en mayuscula lo que esté en minuscula.
def intercambio(texto):
    for letra in texto:
        es_minus = letra.islower()
        es_mayus = letra.isupper()
        if es_minus:
            letras_minusculas = letra
            letras_minusculas = letras_minusculas.upper()
            texto = texto.replace(f"{letra}", f"{letras_minusculas}") # reemplaza la letra minuscula por la mayuscula
        elif es_mayus:
            letras_mayusculas = letra
            letras_mayusculas = letras_mayusculas.lower()
            texto = texto.replace(f"{letra}", f"{letras_mayusculas}")
    return texto
        
def prueba():
    texto = input("Ingrese una cadena de texto para intercambiar minusculas por mayusculas y viceversa: ")
    cambio_letras = intercambio(texto)
    print(f"El texto ingresado: {texto}. El texto intercambiando las letras queda: {cambio_letras}")
    

if __name__ == "__main__":
    prueba()