################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio2 import min_max_promedio, ordenar_secuencia, devolver_maximo, devolver_minimo, devolver_promedio


"""
En estos tests se busca chequear todas las funciones que se utilizan en el ejercicio 2
"""



def test_min_max_promedio_0():
    """
    Esta funcion prueba una secuencia con todos numeros positivos
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = min_max_promedio([9,1,7,6,3,4,5,2,8])
    assert resultado == ("Minimo: 1", "Maximo: 9", "Promedio: 5.0")
    assert isinstance(resultado, tuple)


def test_min_max_promedio_1():
    """
    Esta funcion prueba una secuencia con todos numeros negativos
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = min_max_promedio([-9,-1,-7,-6,-3,-4,-5,-2,-8])
    assert resultado == ("Minimo: -9", "Maximo: -1", "Promedio: -5.0")
    assert isinstance(resultado, tuple)


def test_min_max_promedio_2():
    """
    Esta funcion prueba una secuencia con numeros negativos y positivos
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = min_max_promedio((-9,1,-7,6,4,-5,2,8,9))
    assert resultado == ("Minimo: -9", "Maximo: 9", "Promedio: 1.0")
    assert isinstance(resultado, tuple)

    

def test_ordenar_secuencia_0():
    """
    Esta funcion testea que la funcion ordene una secuencia de numeros
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = ordenar_secuencia([1,3,2,5,4])
    assert resultado == [1,2,3,4,5]
    assert isinstance(resultado, list)


def test_ordenar_secuencia_1():
    """
    Esta funcion testea el caso en el que la secuencia no es numerica
    """
    resultado = ordenar_secuencia([1,"P",2,5,4])
    assert resultado == None
    
    
def test_devolver_promedio():
    """
    Esta funcion testea que dada una lista de numeros se devuelva el promedio
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = devolver_promedio([1, 2, 3])
    assert resultado == 2
    assert isinstance(resultado, float)


def test_devolver_minimo():
    """
    Esta funcion testea que se devuelva el minimo de una lista
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = devolver_minimo([1,2,3])
    assert resultado == 1
    assert isinstance(resultado, int)


def test_devolver_maximo():
    """
    Esta funcion testea que se devuelva el maximo de una lista
    Tambien chequea que el tipo de dato que devuelve se corresponda con la poscondicion
    """
    resultado = devolver_maximo([1,2,3])
    assert resultado == 3
    assert isinstance(resultado, int)