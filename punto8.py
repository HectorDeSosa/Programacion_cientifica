# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Desarrolle un programa que, dados los tres lados 
#   de un triángulo rectángulo en centímetros, calcule y muestre 
#   tanto su área como su perímetro. A continuación, podemos 
#   observar un ejemplo de lo que se espera que el programa muestre 
#   en el caso de que el usuario ingrese valores de 3, 4 y 5 para cada 
#   uno de los lados (tener en cuenta que valores pueden adoptar una unidad de medida).

#Respuesta:
lado_a = float(input("Ingrese el primer lado del triángulo: "))
#verificar los valor
while lado_a <= 0:
    print("Incorrecto lado a")
    lado_a = float(input("Ingrese el primer lado del triángulo: "))

lado_b = float(input("Ingrese el segundo lado del triángulo: "))
while lado_b <= 0:
    print("Incorrecto lado b")
    lado_b = float(input("Ingrese el segundo lado del triángulo: "))

lado_c = float(input("Ingrese el tercer lado del triángulo: "))
while lado_c <= 0:
    print("Incorrecto lado c")
    lado_c = float(input("Ingrese el tercer lado del triángulo: "))

area  = (lado_a * lado_b) /2

perimetro = lado_a + lado_b + lado_c


#mostrar en pantalla
print("El área del triángulo es: ", area)
print("El perímetro del triángulo es: ", perimetro)
