def factorial_bucle_iterativo(numero):
    """
    Función encargada de calcular el factorial de un número usando un bucle iterativo.

    Parámetros:
        - numero: Número entero positivo.

    Salida:
        Factorial del número entero positivo.
    """
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
numero_introducido = int(input("Introduce un número entero positivo: "))
salida_factorial = factorial_bucle_iterativo(numero_introducido)
print("El factorial de", numero_introducido, "es:", salida_factorial)
input("")
