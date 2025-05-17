#Crear una  carpeta con el nombre “paquetes” donde debe tener 
# un módulo que se llame “saludo.py” que contenga 
# una función saludar la cual permite saludar a un nombre+apellido.

#Respuesta:

def saludar(nombre, apellido):
    """
    Función para saludar a una persona con su nombre y apellido.
    
    Parámetros:
    nombre (str): El nombre de la persona.
    apellido (str): El apellido de la persona.
    
    Retorna:
    str: Un saludo personalizado.
    """
    return f"Hola, {nombre} {apellido}!"

