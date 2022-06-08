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
    resultado = True #Se supone que la secuencaia es alfanumerica
        
    while indice < len(texto): #Se recorre el texto ingresado
        if texto[indice] == ' ': #Si el caracter es igual a un espacio no se hace nada
            pass
        #se chequea que segun el codigo ASCII el caracter no sea alfanumerico y si no lo es se retorna Falso
        elif ord(texto[indice]) < 48: #Si el numero de ASCII es menor a 48 y por lo tanto representa un simbolo que no es alfanumerico
            resultado = False 
        elif ord(texto[indice]) > 57 and ord(texto[indice]) < 65: 
            resultado = False 
        elif ord(texto[indice]) > 90 and ord(texto[indice]) < 97:
            resultado = False
        indice = indice + 1
    return resultado #Se retorna True si la secuencia es alfanumerica y False si contiene un simbolo no permitido


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

        if posiciones > 0: #Se calcula la cantidad de posiciones que se puede desplazar un numero dentro de los valores planteados
            while posiciones - rango > 0:
                posiciones = posiciones - rango
        else:
            while posiciones + rango < 0:
                posiciones = posiciones + rango

        nueva_posicion = ord(texto) + posiciones #Se calcula la nueva posicion
        if nueva_posicion < inicio: #Si la nueva posicion es menor al inicio que funciona como cota inferior del rango
            nueva_posicion = inicio - nueva_posicion #Se calcula la diferencia entre la cota inferior y la nueva posicion
            nuevo_texto = nuevo_texto + chr((fin + 1) - nueva_posicion) #Se asigna a una variable el caracter que corresponde
        elif nueva_posicion > fin: #Si la nueva posicion es mayor al inicio que funciona como cota superior del rango
            nueva_posicion = nueva_posicion - fin #Se calcula la diferencia entre la cota superior y la nueva posicion
            nuevo_texto = nuevo_texto + chr((inicio - 1) + nueva_posicion) #Se asigna a una variable el caracter que corresponde
        else: #Si la nueva posicion esta en el rango ingresado
            nuevo_texto = nuevo_texto + chr(nueva_posicion) #Se asigna a una variable el caracter que corresponde
        return nuevo_texto #se retorna el carracter con el corrimiento hecho
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

    
        if esta_en_rango(texto): #Si la secuencia es alfanumerica
            while indice < largo: #Se recorre la secuencia
                if texto[indice] == ' ': #si el caracter es un espacio se guarda en la variable nuevo_texto
                    nuevo_texto = nuevo_texto + ' '
                else: #Si el caracter no es un espacio
                    if ord(texto[indice]) >= 48 and ord(texto[indice]) <= 57: #Caso en el que el caracter del texto es un numero
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 48, 57) #Se suma el caracter a la variable nuevo_texto
                    elif ord(texto[indice]) >= 65 and ord(texto[indice]) <= 90: #Caso en el que el caracter del texto es una letra mayuscula
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 65, 90) #Se suma el caracter a la variable nuevo_texto
                    elif ord(texto[indice]) >= 97 and ord(texto[indice]) <= 122: #Caso en el que el caracter del texto es una letra minuscula
                        nuevo_texto = nuevo_texto + rotador(texto[indice], posiciones, 97, 122)#Se suma el caracter a la variable nuevo_texto
                    else:
                        pass
                indice = indice + 1
            return nuevo_texto #Se devuelve la secuencia codificada
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
    posiciones = posiciones * -1 #Se convierte el texto ingresado en la direccion contraria a la funcion codificador
    return codificador(texto, posiciones) #se devuelve la codificacion decodificada



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(codificador("Abc Def 123", 1))
    print(decodificador("Bcd Efg 234", "a"))
    
    
    

if __name__ == "__main__":
    principal()
