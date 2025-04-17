# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escribir un programa que guarde en un diccionario los 
#   precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de 
#   kilos y muestre por pantalla el precio de ese número de kilos de fruta

#Respuesta:

diccionario_frutas = {"manzana":500,"pera":400,"anana":2000,"sandia":1000,"melon":400,"uva":3500,"naranja":800,\
                      "mandarina":700,"pomelo":3000,"maracuya":600}

print("Frutas disponibles: ",diccionario_frutas)

fruta = input("Ingrese una fruta: ")
kilos_fruta = float(input("Ingrese el peso en kg: "))

precio = diccionario_frutas[fruta]

print("Total a pagar es: $",precio*kilos_fruta)