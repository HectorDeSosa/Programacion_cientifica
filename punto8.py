# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#   los almacene en una lista y los muestre por pantalla ordenados de menor a mayor..
#Respuesta:

#son 6 numeros que se deben ingresar 
lista_numeros =[]

for x in range(1,7):
    numero = int(input(f'Ingrese el numero {x}: '))
    lista_numeros.append(numero)
lista_numeros.sort()

print('La lista de numeros de la primitiva ordenado es: ', lista_numeros)