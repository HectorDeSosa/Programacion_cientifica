# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Pide la hora actual (formato 24h) e imprime:
#   "Buenos días" si es antes de las 12.
#   "Buenas tardes" si es entre las 12 y 18.
#   "Buenas noches" si es después de las 18.

#Respuesta:

hora = input("Ingrese la hora en formato 24h: ")
#formato 12:30
#formato 23:50 

formato_hora = int(hora [:2])

#print(formato_hora) #ayuda para ver avance de algoritmo

if formato_hora < 12:
    print("Buenos dias")
elif formato_hora  < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")