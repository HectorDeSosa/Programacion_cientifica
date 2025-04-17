# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escriba un programa que, dada una lista o tupla de números, 
#   determine cuáles son los valores máximos y mínimos. 
#   Evite hacer uso de las funciones min o max nativas de Python.
#Respuesta:

lista  = [4,8,12,110,45,65,85,12,3,4,1,0,-5,6,7,-9,-11]
minimo = 0

#buscar el minimo
for i in lista:
    if i < minimo:
        minimo = i
    
print(minimo)

#buscar maximo 