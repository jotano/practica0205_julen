def saludar(nombre):
    """
    Función que muestra un saludo.

    Parámetros:
        - nombre: Cadena que contiene el nombre de la persona a saludar.

    Salida:
        Cadena que indica el saludo.
    """
    mensaje = "Saludos " + nombre
    print(mensaje)
    return mensaje
usuario = input("Introduce tu nombre: ")
saludo = saludar(usuario)
input("")

