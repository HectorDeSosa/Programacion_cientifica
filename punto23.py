# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son.
#   Se recuerda que una gruesa son doce docenas.

#Respuesta:

cantidad = int(input("Ingrese una cantidad: "))

gruesas = int(cantidad/144)

resto_gruesas = cantidad % 144

docenas =int(resto_gruesas / 12)

resto_final = resto_gruesas % 12 #unidades seria el resto final

print(f'{cantidad} son {gruesas} gruesas {docenas} docenas y {resto_final} unidades')
