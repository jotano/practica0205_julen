def decimal_binario(decimal):
    """
    Convierte un número decimal a binario.

    Parámetros:
        -Decimal: Número en formato decimal.

    Salida:
        -Binario: Número en formato binario (0b0 representa binario). 
    """
    if decimal < 0:
        return "No puedes introducir un número negativo."
    if decimal == 0:
        return "0b0"
    
    binario = bin(decimal)
    return binario


def binario_decimal(binario):
    """
    Convierte un número binario a decimal.

    Parámetros:
        -Binario: Número en formato binario (0b0 representa binario). 

    Salida:
        -Decimal: Número en formato decimal.
    """
    decimal = int(binario, 2)
    return decimal