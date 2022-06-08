################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""

def ordenar_secuencia(secuencia):
    """
    Esta funcion se encarga de ordenar una secuencia de menor a mayor.

    Precondicion: una secuencia de numeros
    Poscondicion: una lista ordenada
    """
    ###Quise probar usar QuickSort y me parece que para este ejercicio es util

    try:        
        largo = len(secuencia)
        if largo <= 1: #Si la lista tiene largo 0 o 1 la devuelvo
            return secuencia
        else: #Sino
            pivot = secuencia[largo - 1] #Elige el ultimo valor de la lista
            mayor = [] #Crea una lista vacia
            menor = [] #Crea otra lista vacia
            indice = 0 
            while indice < largo - 1: #Recorre todos los elementos de la lista menos el ultimo que es el pivot
                if secuencia[indice] > pivot: #Si el elemento es mayor al pivot lo agrega a la lista Mayor
                    mayor.append(secuencia[indice])
                else: #Si el elemento es menor o igual al pivot agrega el elemento a la lista Menor
                    menor.append(secuencia[indice])
                indice = indice + 1
        #Devuelve la suma de lo que retornallmar recursivamente a la lista menor 
        #mas el pivot mas lo que retorna llamar recursivamente a la lista mayor
        return ordenar_secuencia(menor) + [pivot] + ordenar_secuencia(mayor) 
    except TypeError as exc:
        print("La secuencia ingresada no esta compuesta unicamente por numeros")
    
            


def devolver_maximo(secuencia):
    """
    Esta funcion toma una secuencia y devuelve el valor mas chico

    Precondicion: una secuencia de numeros
    Posconcicion: un numero
    """

    secuencia_ordenada = ordenar_secuencia(secuencia) #se ordena la secuencia de menor a mayor
    return secuencia_ordenada[len(secuencia) - 1] #se devuelve el ultimo elemento que es el de mayor valor



def devolver_minimo(secuencia):
    """
    Esta funcion toma una secuencia y devuelve el valor mas gramde

    Precondicion: una secuencia de numeros
    Posconcicion: un numero
    """
    secuencia_ordenada = ordenar_secuencia(secuencia) #se ordena la secuencia de menor a mayor
    return secuencia_ordenada[0] #se devuelve el primer elemento que es el de mayor valor



def devolver_promedio(secuencia):
    """
    Esta funcion toma una secuencia y devuelve el promedio

    Precondicion: una secuencia de numeros
    Posconcicion: un numero
    """

    total = 0
    indice = 0
    while indice < len(secuencia): #Se recorre la secuencia
        total = total + secuencia[indice] #Se suman todos los elementos
        indice = indice + 1
    return total / len(secuencia) #Se retorna el promedio de la secuencia
    


def min_max_promedio(secuencia):
    """
    Esta funcion toma una secuencia de numeros y devuelve el minimo, el maximo y el promedio

    Precondicion: una secuendia de numeros
    Poscondicion: una tupla
    """
    
    minimo = f"Minimo: {devolver_minimo(secuencia)}"
    maximo = f"Maximo: {devolver_maximo(secuencia)}"
    promedio = f"Promedio: {devolver_promedio(secuencia)}"
    return (minimo, maximo, promedio)
    
    



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    resultado = min_max_promedio((1,3,2,4,2,2.7))
    print(resultado)
    


if __name__ == "__main__":
    principal()
