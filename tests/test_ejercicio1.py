################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import par_o_impar, signo

"""
En estos tests se busca chequear todas las funciones que se utilizan en el ejercicio 1
"""


def test_par_o_impar_0():
    """
    Esta funcion testea un numero par positivo
    """
    resultado = par_o_impar(2)
    assert resultado == True
    assert isinstance(resultado, bool)

def test_par_o_impar_1():
    """
    Esta funcion testea un numero impar positivo
    """
    resultado = par_o_impar(3)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_par_o_impar_2():
    """
    Esta funcion testea un numero par negativo
    """
    resultado = par_o_impar(-8)
    assert resultado == True
    assert isinstance(resultado, bool)

def test_par_o_impar_3():
    """
    Esta funcion testea un numero impar negativo
    """
    resultado = par_o_impar(-23)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_par_o_impar_4():
    """
    Esta funcion testea el numero cero
    """
    resultado = par_o_impar(0)
    assert resultado == True
    assert isinstance(resultado, bool)


def test_par_o_impar_5():
    """
    Esta funcion testea el caso en el que el tipo de entrada no es el especificado en la precondicion
    """
    resultado = par_o_impar("Test")
    assert resultado == None
    

def test_signo_0():
    """
    Esta funcion analiza el caso para un numero positivo
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(10)
    assert resultado == 1
    assert isinstance(resultado, int)
    
    
    
def test_signo_1():
    """
    Esta funcion analiza el caso para el cero
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(0) 
    assert resultado == 0
    assert isinstance(resultado, int)


def test_signo_2():
    """
    Esta funcion analiza el caso para un numero negativo
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(-10.23)
    assert resultado == -1
    assert isinstance(resultado, int)

