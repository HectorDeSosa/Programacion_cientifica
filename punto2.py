# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos (utilizando 
# una función que realice dicha suma).

# Respuesta:

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito) 
    return suma

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0: # Si es cero termina el bucle 
        break
    suma = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma}")
