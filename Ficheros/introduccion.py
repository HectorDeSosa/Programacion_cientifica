#Pag 384
#ruta (en ingles, ˂˂path˃˃)
#/home/al55555/nota.txt
#El protocolo de trabajo con ficheros: abrir, leer/escribir, cerrar
# lectura, escritura, lectura/escritura, adicion, cerrar
#importancia de cerrar los archivos


# Paso 1: abrir el fichero.
fichero = open('Ficheros/ejemplo.txt','r')
# Paso 2: leer los datos del fichero.
for linea in fichero:
    print (linea)
# Paso 3: cerrar el fichero.
fichero.close()

"""
#Tratamiento de errores
import os
if os.path.exists("ejemplo.txt"):
    fichero = open("ejemplo.txt", "r")
    for linea in fichero:
        print (linea)
        fichero.close()
    else:
        print ("El fichero no existe.")
#usando try
try:
    fichero = open("ejemplo.txt", "r")
    for linea in fichero:
        print (linea)
        fichero.close()
except IOError:
    print ("El fichero no existe.")

#Eliminar saltos de lineas espureos \n
#esto debido a los saltos al finalizar las lineas
fichero = open("ejemplo.txt", "r")

for linea in fichero:
    if linea[-1] == "\n":
        linea = linea[:-1]
        print (linea)
fichero.close()
"""
#trabajar en copia
nombre = input("Ingrese el nombre del fichero: ")
fichero = open(nombre, "r")
contador = 0        
for linea in fichero:
    contador += 1
    fichero.close()
print (contador)