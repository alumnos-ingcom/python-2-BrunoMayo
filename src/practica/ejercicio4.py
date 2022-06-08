################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores.
En la misma, los dos primeros términos son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1) 
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci.
Siendo este número un entero positivo mayor a 2.
"""


def fibonacci(n_esimo):
    """
    Esta funcion toma un numero y devuelve el numero correspondiente a la posicion del mismo en fibonacci

    Precondicion: un numero
    Poscondicion: un entero
    """
    num1 = 0
    num2 = 1
    indice = 2

    try:
        if n_esimo > 0: #se comprueba que el n_esimo numero sea mayor que cero
            while indice < n_esimo: #Se recorre el loop n veces
                if num1 > num2: #si el numero 1 es mayor que el numero 2
                    num2 = num2 + num1 #se guarda en el numero 2 la suma de ambos
                else: #si el numero 2 es mas grande que el numero 1
                    num1 = num1 + num2 #se guarda en el numero 1 la suma de ambos
                indice = indice + 1

            if num1 > num2: #Se compara la variable numero1 con la numero2 y se devuelve el numero mas grande
                resultado = num1
            else:
                resultado = num2
        else:#Si el numero n_esimo es menor que cero el resultado que se retorna es cero
            resultado = 0
        return resultado
    except TypeError as exc:
        print("El valor ingresado no es un numero")



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    n_esimo = int(input("Ingrese un numero: "))
    resultado = fibonacci(n_esimo)
    print(resultado)


if __name__ == "__main__":
    principal()
