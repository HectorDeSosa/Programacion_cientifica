class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza


p1 = Perro("Toby", "Bulldog")

print(type(p1))
# Creando perro Toby, Bulldog
print(p1.nombre) # Toby
print(p1.raza)   # Bulldog