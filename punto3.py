class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def cumpleaños(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")
    
    #segunda forma de mostrar datos
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Ejemplo de uso
p1 = Persona("Sebastian", 23)
p1.mostrar_datos()
p1.cumpleaños()
#usando el str
print(p1)