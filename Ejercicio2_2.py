def factorial_funcion_recursiva(numero):
    """
    Función que se encarga de calcular el factorial mediante una solución recursiva.


    Parámetros:
        - numero: Número entero positivo.


    Salida:
        Factorial del número entero positivo.
    """
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_funcion_recursiva(numero - 1)


numero_introducido = int(input("Introduce un número entero positivo: "))
salida_factorial = factorial_funcion_recursiva(numero_introducido)
print("El factorial de", numero_introducido, "es:", salida_factorial)
input("")