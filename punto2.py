#cnotenido 
"""
Métodos y propiedades; Métodos especiales (__init__, __str__, etc.). 
Herencia y herencia múltiple; 
"""

"""
Realizar un programa que conste de una clase llamada Alumno que tenga como
atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus
atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha
aprobado o no.
"""

#definir una clase

class Alumno():
    #definir el constructor
    def __init__(self, nombre, nota=None):
        self.nombre = nombre
        self.nota = nota
    """
    def mostrar(self):
        print(f"Soy el alumno {self.nombre} y me saque una nota de: {self.nota}")
    """
    def __str__(self):
        return f"Soy el alumno {self.nombre} y me saque una nota de: {self.nota}"

    def regular(self):#metodo regular
        if self.nota > 7:
            print("Aprobado")
        else:
            print("Desaprobado")
            

dic_alumnos = {"Sabestian":10, "Luciana":9, "Hector":4, "Debora":9}

for nombre, nota in dic_alumnos.items():
    alum = Alumno(nombre, nota) #instancia
    alum.regular()









