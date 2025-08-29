import json

#Crear un diccionario con materias y notas
materias = {
    "Matemática": 8,
    "Programación": 10,
    "Bases de Datos": 9,
    "Redes": 7
}

#Opcion 1
archivo = json.dumps(materias, indent=4, ensure_ascii=False)
print("Archivo JSON creado: ",archivo)

#Opcion 2
#Guardar el diccionario en un archivo JSON (escritura)
#with open("materias.json", "w", encoding="utf-8") as archivo:
#    json.dumps(materias, archivo, indent=4, ensure_ascii=False)

#print("Archivo JSON creado")


# Leer el archivo JSON
datos = json.loads(archivo)
print(datos)
