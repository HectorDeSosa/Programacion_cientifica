# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escriba un programa que reciba un entero positivo. 
#   Sí el número ingresado es múltiplo de 5 deberá imprimir en pantalla 
#   El número es múltiplo de 5, en cualquier otro caso deberá imprimir 
#   El número no es múltiplo de 5.
#Respuesta:

#repetir mientras
entero = int(input("Ingrese un entero: "))# si o si se debe ingresar una primera vez
while entero < 1 :
    entero = int(input("Ingrese un entero: "))

print(entero)#muestro el numero para  tener presente que esta bien

#si es multiplo de 5 el resto es cero
multiplo_5 = entero % 5 #obtener el resto

if multiplo_5 == 0:
    print("El número es multiplo de 5")
else:
    print("El número no es multiplo de 5")


