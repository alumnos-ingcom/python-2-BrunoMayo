################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con string está balanceada.
Es decir, si cada corchete que abre, tiene su par que cierra. El resultado debe ser un valor lógico indicando si esta o no balanceado.
La funcion deberia de ignorar todo lo que no sean string.
"""

def string_balanceados(string, simbolo):
    """
    Esta funcion toma un string y un par de simbolos donde uno es de apertura y el otro de cierre.

    Precondicion: un par de simbolos uno de apertura y otro de cierre (por ej () o [])
    Poscondicion: un valor booleano
    """
    
    string_abiertos = 0
    string_cerrados = 0
    indice = 0

    try:
        while indice < len(string):
            if string[indice] == simbolo[0]:
                string_abiertos = string_abiertos + 1
            elif string[indice] == simbolo[1]:
                string_cerrados = string_cerrados + 1
            indice = indice + 1

            if string_cerrados > string_abiertos:
                resultado = False
                break
            else:
                pass
        resultado = (string_abiertos == string_cerrados) and string_abiertos != 0
        return resultado
    except TypeError as exc:
        print("Uno de los parametros no es del tiop de dato string")


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    resultado = string_balanceados("[}[]]", "[]")
    print(resultado)

if __name__ == "__main__":
    principal()
