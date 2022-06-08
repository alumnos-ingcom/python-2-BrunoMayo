################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
El cifrado César o cifrado de rotación usa una encriptación de sustitución simple. Esto significa que cada caracter se sustituye por otro caracter de acuerdo con un sistema especifico.
La codificación debe ser tal que la palabra codificada contenga unicamente caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas letras del abecedario se vuelva a las primeras letras.
Por ejemplo, el método conocido y muy utilizado ROT13 rota el alfabeto con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
Una buena forma para verificar este ejercicio es codificar y decodificar un texto y compararlo con lo que fué ingresado originalmente.
Tip: Implementar las funciones utilizando las funciones ord y chr."""


def esta_en_rango(texto):
    """
    Esta funcion chequea que los caracteres de un texto esten dentro de los
    rangos ASCII permitidos. Estos son (48 - 57), (65 - 90) y (97 - 122).
    La funcion devuelve True si todos sus caracteres estan en los rangos permitidos y False
    en caso contrario.

    Precondicion: Un string
    """
    indice = 0
    resultado = True
        
    while indice < len(texto):
        if texto[indice] == ' ':
            pass
        elif ord(texto[indice]) < 48:
            resultado = False
        elif ord(texto[indice]) > 57 and ord(texto[indice]) < 65:
            resultado = False
        elif ord(texto[indice]) > 90 and ord(texto[indice]) < 97:
            resultado = False
        indice = indice + 1
    return resultado


def rotador(texto, posiciones, inicio, fin):
    """
    Esta funcion se encarga de recibir un caracter, cuantas posiciones debe ser rotado y dentro de
    que valores de ASCCI se debe rotar. Por ejemplo, si el inicio es 10 y el fin es 20, si el
    texto es un caracter cuyo valor ASCCI es 19 y se lo desea rotar tres posiciones el mismo se convertira
    al caracter representado por el numero 11.
    
    Precondicion: un string de largo 1 y tres numeros enteros
    Poscondicion: Un string de largo 1
    """
    try:
        nuevo_texto = ''
        rango = fin - inicio + 1

        if posiciones > 0:
            while posiciones - rango > 0:
                posiciones = posiciones - rango
        else:
            while posiciones + rango < 0:
                posiciones = posiciones + rango

        nueva_posicion = ord(texto) + posiciones
        if nueva_posicion < inicio:
            nueva_posicion = inicio - nueva_posicion
            nuevo_texto = nuevo_texto + chr((fin + 1) - nueva_posicion)
        elif nueva_posicion > fin:
            nueva_posicion = nueva_posicion - fin
            nuevo_texto = nuevo_texto + chr((inicio - 1) + nueva_posicion)
        else:
            nuevo_texto = nuevo_texto + chr(nueva_posicion)
        return nuevo_texto
    except TypeError as exc:
        print("Se ha ingresado un parametro incorrectamente\nEl primer parametro debe ser un caracter y los otros 3 parametros deben ser enteros")


def codificador(texto, posiciones):
    """
    Esta funcion recibe un texto compuesto por caracteres y numeros. También recibe cuantas posiciones
    se desea rotar a los mismos.
    Devuelve un texto con los caracteres rotados las posiciones especificadas de acuerdo a su valor en la tabla ASCII.

    Precondicion: un string y un numero entero
    Poscondicion: un string
    """
    try:
        largo = len(texto)
        indice = 0
        nuevo_texto = ''

    
        if esta_en_rango(texto):
            while indice < largo:
                if texto[indice] == ' ':
                    nuevo_texto = nuevo_texto + ' '
                else:
                    if ord(texto[indice]) >= 48 and ord(texto[indice]) <= 57: #Caso en el que el caracter del texto es un texto
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 48, 57)
                    elif ord(texto[indice]) >= 65 and ord(texto[indice]) <= 90: #Caso en el que el caracter del texto es un texto
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 65, 90)
                    elif ord(texto[indice]) >= 97 and ord(texto[indice]) <= 122: #Caso en el que el caracter del texto es un texto
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 97, 122)
                    else:
                        pass
                indice = indice + 1
            return nuevo_texto
        else:
            pass
    except TypeError as exc:
        print("El valor del primer parametro debe ser un string y el del segundo un entero")
    

def decodificador(texto, posiciones):
    """
    Esta funcion recibe un texto y cuantas posiciones se lo desea rotar.
    La misma devuelve el texto rotado inversamente a lo especificado de acuerdo a su valor en la tabla ASCII.

    Precondicion: un string y un numero entero
    Poscondicion: un string    
    """
    posiciones = posiciones * -1
    return codificador(texto, posiciones)



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(codificador("Abc Def 123", 1))
    print(decodificador("Bcd Efg 234", "a"))
    
    
    

if __name__ == "__main__":
    principal()
