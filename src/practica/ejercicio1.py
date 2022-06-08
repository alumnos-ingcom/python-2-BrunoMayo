################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un número entero es par y
False cuando no lo sea, sin utilizar módulo. (%)
"""


def signo(numero):
    """
    Esta funcion recibe un numero y devuelve 1 si el numero es positivo,
    -1 si el numero es negativo o cero si el numero es cero

    precondicion: numero
    poscondicion: numero entero (1, 0, -1)
    """
    valor_absoluto = abs(numero)
    if numero == 0: #Si el numero es 0 se va a retornar cero
        resultado = 0
    elif numero - valor_absoluto == 0: #Si el numero es positivo se va a retornar 1
        resultado = 1
    else: #Si el numero es negativo se va a retornar -1
        resultado = -1
    return resultado




def par_o_impar(numero):
    """
    Esta funcion recibe un numero como parametro y devuelve True si el numero es par
    o False si el numero no es par

    Precondicion: un numero entero
    Poscondicion: un valor booleano o None
    """
    try:
        if signo(numero) == 1: #Si el numero es positivo, le resto 2 hasta que el numero sea 1 o 0
            while numero >= 1: 
                numero = numero - 2
        else:
            while numero <= -1:#Si el numero es negativo, le sumo 2 hasta que el numero sea 1 o 0
                numero = numero + 2
        return numero == 0 #Si el numero es 0 significa que es par y retorna True. Si el numero es 1 entonces es impar y retorna False
    except TypeError as exc:
        print("El valor ingresado no es un numero")


def principal():
    """
    Esta funcion es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    #numero = int(input("Ingrese un numero entero: "))
    resultado = par_o_impar("0")
    print(resultado)



if __name__ == "__main__":
    principal()
