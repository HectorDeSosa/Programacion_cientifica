#
class Vehiculo:
    def __init__(self, marca, color, año, tamaño, peso):
        self.marca = marca
        pass

class Auto(Vehiculo):
    def __init__(self, marca, cantidad_ruedas, puertas, asiento):
        super().__init__(marca)
        self.puertas = puertas

class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)

class Avion(Vehiculo):
    def __init__(self, marca, color, año, tamaño, peso):
        super().__init__(marca, color, año, tamaño, peso)