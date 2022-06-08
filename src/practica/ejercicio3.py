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
    if len(lista1) > len(lista2): #Si la longitud de la primer lista es mayor a la segunda
        i = 0
        while i < len(lista1): #se recorre la lista mas grande
            if lista2[0] == lista1[i]: #Se compara el primer caracter de la secuencia mas chica con la mas grande
                contador = (i, 0) #Si hay coincidencia se retorna la posicion de donde coinciden
                hay_coincidencia = True 
            else:
                pass
            i = i + 1
    else: #Si la longitud de la segunda lista es mayor o igual a la de la primera
        i = 0
        while i < len(lista2): #Se recorre la lista
            if lista1[0] == lista2[i]: #Si conincide el primer elemento de la lista1 con alguno de la segunda
                contador = (0, i) #Se retorna la posicion donde coinciden
                hay_coincidencia = True
            else: 
                pass                
            i = i + 1
    
    if not hay_coincidencia: #Si no hay conincidencia se retorna un mensaje que avisa que no existe coincidencia
        contador = "No hay coincidencia"
    
    return contador 
        


def superposicion(lista1, lista2):
    """
    Esta funcion a partir de la posicion en que coinciden dos listas cuanta la cantidad de veces que se superponen
    hasta que ya no lo hacen mas.

    Precondicion: dos listas
    Poscondicion: un string
    """


    if type(devolver_inicio_superposicion(lista1, lista2)) == tuple: #Si la funcion retorna una tupla con el elemento donde coinciden
        indice_lista1 = devolver_inicio_superposicion(lista1, lista2)[0] #se guarda el elemento de la lista 1 donde coinciden 
        indice_lista2 = devolver_inicio_superposicion(lista1, lista2)[1] #se guarda el elemento de la lista 2 donde coinciden 
        indice = 0
        contador = 0

        if len(lista1) > len(lista2): #Si la longitud de la lista1 es mayor a la de la lista2
            while indice < len(lista2): #Se recorre la lista mas chica
                if lista1[indice_lista1 + indice] == lista2[indice_lista2 + indice]: #Partiendo desde las coordenadas donde coinciden se comparan los elementos
                    contador =  contador + 1 #Si los elementos coinciden se suma 1 al contador
                else:# Si no coinciden
                    break #Se deja de comparar
                indice = indice + 1
        else: #Si la longitud de la lista2 es mayor a la de la lista1
            while indice < len(lista1): #Se recorre la lista mas chica
                if lista1[indice_lista1 + indice] == lista2[indice_lista2 + indice]:#Partiendo desde las coordenadas donde coinciden se comparan los elementos
                    contador =  contador + 1#Si los elementos coinciden se suma 1 al contador
                else:# Si no coinciden
                    break#Se deja de comparar
                indice = indice + 1
        #se devuelve un string con el valor del contador y las cordenadas donde comienzan a coincidir
        resultado = f"Hay {contador} coincidencias y estan el indice {indice_lista1} de la Lista 1 y en el indice {indice_lista2} de la Lista 2"
    else: #Si la funcion de devolver inicio de superposicion no retorna una tupla
        resultado = devolver_inicio_superposicion(lista1, lista2) #Se devuelve el string "No hay coincidencia"
    return  resultado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(superposicion([1,'H', 'o', 'l', 'a', ' ', 'M', 'i', 'c', 'k', 'e', 'y'], ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']))


if __name__ == "__main__":
    principal()
