# Importar un módulo y modificar el nombre 
# del mismo colocando un nombre más corto. 
# ¿Qué beneficio tiene este cambio de nombre?

# Respuesta:

from paquetes.saludos import saludar
# Importar el módulo "saludos" desde el paquete "paquetes"

saludo = saludar("Juan", "Matias")
# Llamar a la función "saludar" del módulo "saludos"

print(saludo)