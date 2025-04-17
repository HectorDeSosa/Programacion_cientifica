# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Pide al usuario que impute una lista de alumnos, separadas con “;”. 
#   Después, pregunta por las notas de ellos. Realizar diccionario para después poder 
#   preguntar a alguien y observar su nota

#Respuesta:

lista = input("Ingrese una lista de alumnos separados por punto y coma: ")

lista_alumnos = lista.split(";")#separa en la lista por punto y coma

cantidad = len(lista_alumnos) #saber la cantidad de alumnos que hay
diccionario = dict()#diccionario vacio
for i in range(cantidad):
    nota = float(input(f'Ingrese la nota del alumno {i+1}: '))
    diccionario[lista_alumnos[i]] = nota

#ingresar un nombre para saber
buscar = input("Ingrese un nombre: ")

print(diccionario[buscar])