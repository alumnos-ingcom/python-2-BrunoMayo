################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import devolver_inicio_superposicion, superposicion

"""
En estos tests se busca chequear todas las funciones que se utilizan en el ejercicio 3
"""


def test_superposicion_0():
    """
    Esta funcion testea el caso en que no coincidan las listas
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = superposicion(['H', 'o', 'l', 'a'], ['C', 'h', 'a', 'u'])
    assert resultado == "No hay coincidencia"
    assert isinstance(resultado, str)

def test_superposicion_1():
    """
    Esta funcion testea el caso en que las listas son iguales
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = superposicion(['H', 'o', 'l', 'a'], ['H', 'o', 'l', 'a'])
    assert resultado == "Hay 4 coincidencias y estan el indice 0 de la Lista 1 y en el indice 0 de la Lista 2"
    assert isinstance(resultado, str)

def test_superposicion_2():
    """
    Esta funcion testea el caso en que las listas coincidan parcialmente
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = superposicion(['H', 'o', 'l', 'a'], ['H', 'o', 'l', 'l', 'a'])
    assert resultado == "Hay 3 coincidencias y estan el indice 0 de la Lista 1 y en el indice 0 de la Lista 2"
    assert isinstance(resultado, str)

def test_superposicion_3():
    """
    Esta funcion testea el caso en que las listas estan compuestas por distintos tipos de datos
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = superposicion([1.1, "a", 3, 4], [0, 1.1, "a", 3, 5])
    assert resultado == "Hay 3 coincidencias y estan el indice 0 de la Lista 1 y en el indice 1 de la Lista 2"
    assert isinstance(resultado, str)


def test_devolver_inicio_superposicion_0():
    """
    Esta funcion testea el caso en que no coincidan las listas
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = devolver_inicio_superposicion(['H', 'o', 'l', 'a'], ['C', 'h', 'a', 'u'])
    assert resultado == "No hay coincidencia"
    assert isinstance(resultado, str)


def test_devolver_inicio_superposicion_1():
    """

    Esta funcion testea el caso en que coincidan las listas parcialmente y devuelve los indices donde comienza la coincidencia
    Tambien chequea que el tipo de dato de la poscondicion sea el que corresponde
    """
    resultado = devolver_inicio_superposicion(['H', 'o', 'l', 'a'], ['C', 'h', 'H', 'o'])
    assert resultado == (0, 2)
    assert isinstance(resultado, tuple)