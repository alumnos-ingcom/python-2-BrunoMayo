################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio4 import fibonacci

"""
En estos tests se busca chequear todas las funciones que se utilizan en el ejercicio 4
"""


def test_fibonacci_0():
    """
    Esta funcion testea un valor positivo de entrada y chequea que el resultado sea correcto
    Tambien testea que el tipo de dato que devuelve la funcion se correponda con la poscondicion
    """
    resultado = fibonacci(8)
    assert resultado == 13
    assert isinstance(resultado, int)


def test_fibonacci_1():
    """
    Esta funcion testea un valor negativo y chequea que el resultado sea cero
    Tambien testea que el tipo de dato que devuelve la funcion se correponda con la poscondicion
    """
    resultado = fibonacci(-8)
    assert resultado == 0
    assert isinstance(resultado, int)



def test_fibonacci_3():
    """
    Esta funcion chequea el caso en el que el parametro no es del tipo solicitado por la precondicion
    """
    resultado = fibonacci("test")
    assert resultado == None
    