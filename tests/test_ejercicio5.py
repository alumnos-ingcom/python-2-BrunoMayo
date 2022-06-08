################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio5 import string_balanceados

"""
En estos tests se busca chequear todas las funciones que se utilizan en el ejercicio 5
"""


def test_string_balanceados_0():
    """
    Esta funcion testea un caso verdadero.
    Tambien chequea que el tipo de dato de retorno sea el que corresponde con la poscondicion
    """
    resultado = string_balanceados("[][]", "[]")
    assert resultado == True
    assert isinstance(resultado, bool)

def test_string_balanceados_1():
    """
    Esta funcion testea otro caso verdadero pero con distinto simbolo
    Tambien chequea que el tipo de dato de retorno sea el que corresponde con la poscondicion
    """
    resultado = string_balanceados("()test()", "()")
    assert resultado == True
    assert isinstance(resultado, bool)

def test_string_balanceados_2():
    """
    Esta funcion testea un caso falso.
    Tambien chequea que el tipo de dato de retorno sea el que corresponde con la poscondicion
    """
    resultado = string_balanceados("][][", "[]")
    assert resultado == False
    assert isinstance(resultado, bool)

def test_string_balanceados_3():
    """
    Esta funcion testea el caso en donde uno de los parametros no es del tipo indicado
    """
    resultado = string_balanceados(22, 2)
    assert resultado == None