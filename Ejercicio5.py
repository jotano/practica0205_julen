def numeros_cuadrados(lista):
    """
    Función que recibe una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.


    Parámetros:
        -Lista: Una lista de números.


    Salida:
        -Lista: Lista con los números al cuadrado.
    """
    cuadrados = [x**2 for x in lista]
    return cuadrados
muestra = [1, 3, 5, 8, 10]
cuadrados_resultado = numeros_cuadrados(muestra)
print("Los números al cuadrado son:", cuadrados_resultado)
input("")