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
        if n_esimo > 0:
            while indice < n_esimo:
                if num1 > num2:
                    num2 = num2 + num1
                else:
                    num1 = num1 + num2
                indice = indice + 1

            if num1 > num2:
                resultado = num1
            else:
                resultado = num2
        else:
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
