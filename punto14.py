# De Sosa Hector
# 202X
# Programacion Cientifica
# CONTENIDO del Punto:
#   En un almacén se descuenta 20% del precio al cliente
#   si el valor a pagar es mayor a $200. 
#   Dado un valor de precio, muestre lo que debe pagar el cliente.
#Respuesta:

precio = float(input("Ingrese el precio: "))

if precio > 200:
    pagar = precio * (1-20/100)
else:
    pagar = precio

print("Total a pagar es: ", pagar)


