################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import esta_en_rango, rotador, codificador, decodificador
"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_codificador_0():
    """
    Esta funcion testea 3 letras mayusculas, 3 minusculas y 3 numeros.
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = codificador("ABCabc123", 3)
    assert resultado == "DEFdef456"
    assert isinstance(resultado, str)

def test_codificador_1():
    """
    Esta funcion testea 3 letras mayusculas, 3 minusculas y 3 numeros en el limite superior, 
    es decir que se verifica que despues de la z se vuelva al inicio del abecedario y despues del 9 se vuelva al 0
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = codificador("XYZxyz789", 3)
    assert resultado == "ABCabc012"
    assert isinstance(resultado, str)

def test_codificador_2():
    """
    Esta funcion testea 3 letras mayusculas, 3 minusculas y 3 numeros en el limite inferior, 
    es decir que se verifica que despues de la 'a', en un caso en que la posicion es negativa, 
    se vuelva al fin del abecedario y despues del 0 se vuelva al 9
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = codificador("ABCabc012", -3)
    assert resultado == "XYZxyz789"
    assert isinstance(resultado, str)

def test_codificador_3():
    """
    Se chequea el caso en el que los parametros ingresados no se condicen con lo
    que solicita la precondicion
    """
    resultado = codificador(2, "A")
    assert resultado == None


def test_decodificador_0():
    """
    Se testea que se decodifique el caso del test_codificador_0
    """
    resultado = decodificador("DEFdef456", 3)
    assert resultado == "ABCabc123"
    assert isinstance(resultado, str)

def test_decodificador_1():
    """
    Se testea que se decodifique el caso del test_codificador_1
    """
    resultado = decodificador("ABCabc012", 3)
    assert resultado == "XYZxyz789"
    assert isinstance(resultado, str)

def test_decodificador_2():
    """
    Se testea que se decodifique el caso del test_codificador_2
    """
    resultado = decodificador("XYZxyz789", -3)
    assert resultado == "ABCabc012"
    assert isinstance(resultado, str)

def test_decodificador_3():
    """
    Se chequea el caso en el que los parametros ingresados no se condicen con lo
    que solicita la precondicion
    """
    resultado = decodificador(2, "A")
    assert resultado == None


def test_esta_en_rango_0():
    """
    Esta funcion testea el caso en el que el parametro ingresado
    esta en el rango de la funcion que son las letras y los numeros.
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = esta_en_rango("ABCabc123")
    assert resultado == True
    assert isinstance(resultado, bool)

def test_esta_en_rango_1():
    """
    Esta funcion testea el caso en el que el parametro ingresado
    NO esta en el rango de la funcion que son las letras y los numeros.
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = esta_en_rango("ABCa*[bc123")
    assert resultado == False
    assert isinstance(resultado, bool)

def test_rotador_0():
    """
    Se testea un caso en el que se rota correctamente
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = rotador("a", 3, 97, 122)
    assert resultado == "d"

def test_rotador_1():
    """
    Se testea un caso en el que se ingresen mal los parametros
    Tambien chequea que el tipo de datos se corresponda con la poscondicion
    """
    resultado = rotador("HOLA","a", 97, 122)
    assert resultado == None