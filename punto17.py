
# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto: 
#   Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros. 
#   Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.


#Respuesta:
distancia_pies = int(input("Ingrese una distancia en pies: "))
distancia_pulgadas = int(input("Ingrese una distancia en pulgadas: "))

#conversion a centimetros
centimetros = distancia_pies*12*2.54 + distancia_pulgadas*2.54

#centimetros = (distancia_pies*12 + distancia_pies)*2.54 #factor comun

print(f'{distancia_pies} pies y {distancia_pulgadas} pulgadas son {centimetros} centimetros')