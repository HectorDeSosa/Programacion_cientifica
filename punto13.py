# De Sosa Hector
# 2025
# Programacion Cientifica
# CONTENIDO del Punto:
#   Escribir un programa que pregunte al usuario 
#   por el número de horas trabajadas y el coste 
#   por hora. Después debe mostrar por pantalla la paga que le corresponde.
#Respuesta:
horas = int(input('Ingrese las horas que trabaja por dia: '))

costo_por_hora = float(input("Ingrese el costo por hora: "))

monto_a_pagar = horas * costo_por_hora

print('El monto a pagar es: ',monto_a_pagar)