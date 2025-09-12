class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")


# Ejemplo de uso
p1 = Persona("Juan", 23)
p1.mostrar_datos()
p1.es_mayor_de_edad()

p2 = Persona("Brenda", 15)
p2.mostrar_datos()
p2.es_mayor_de_edad()
