def media_numeros(lista):
    """
    Función que recibe una muestra de números en una lista y devuelva su media.


    Parameters:
    -Lista: Lista de números.


    Salida:
    Media de la lista.
    """
    suma = sum(lista)
    media = suma / len(lista)
    return media
muestra = [1, 4, 8, 10, 20]
media= media_numeros(muestra)
print("La media es:", media)
input("")
