################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas. Siendo 0 sin superposición y uno para cada elemento superpuesto.

['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
y
['H', 'o', 'l', 'a']
Tienen una superposición de cuatro elementos."""
# Reemplazar por las funciones del ejercicio


def devolver_inicio_superposicion(lista1, lista2):
    """
    Esta función toma dos listas y devuelve la posicion en la que se encuentra la primer coincidencia o devuelve un string 
    en caso de que no haya una coincidencia.

    Precondicion: dos listas
    Poscondicion: una tupla o un string
    """
    hay_coincidencia = False
    if len(lista1) > len(lista2):
        i = 0
        while i < len(lista1):
            if lista2[0] == lista1[i]:
                contador = (i, 0)
                hay_coincidencia = True
            else:
                pass
            i = i + 1
    else: 
        i = 0
        while i < len(lista2):
            if lista1[0] == lista2[i]:
                contador = (0, i)
                hay_coincidencia = True
            else: 
                pass                
            i = i + 1
    
    if not hay_coincidencia:
        contador = "No hay coincidencia"
    
    return contador
        


def superposicion(lista1, lista2):
    """
    Esta funcion a partir de la posicion en que coinciden dos listas cuanta la cantidad de veces que se superponen
    hasta que ya no lo hacen mas.

    Precondicion: dos listas
    Poscondicion: un string
    """


    if type(devolver_inicio_superposicion(lista1, lista2)) == tuple:
        indice_lista1 = devolver_inicio_superposicion(lista1, lista2)[0]
        indice_lista2 = devolver_inicio_superposicion(lista1, lista2)[1]
        indice = 0
        contador = 0

        if len(lista1) > len(lista2):
            while indice < len(lista2):
                if lista1[indice_lista1 + indice] == lista2[indice_lista2 + indice]:
                    contador =  contador + 1
                else:
                    break
                indice = indice + 1
        else:
            while indice < len(lista1):
                if lista1[indice_lista1 + indice] == lista2[indice_lista2 + indice]:
                    contador =  contador + 1
                else:
                    break
                indice = indice + 1

        resultado = f"Hay {contador} coincidencias y estan el indice {indice_lista1} de la Lista 1 y en el indice {indice_lista2} de la Lista 2"
    else:
        resultado = devolver_inicio_superposicion(lista1, lista2)
    return  resultado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(superposicion([1,'H', 'o', 'l', 'a', ' ', 'M', 'i', 'c', 'k', 'e', 'y'], ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']))


if __name__ == "__main__":
    principal()
