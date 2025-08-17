"""
Un restaurante quiere llevar un conteo de pedidos.
Existe una variable global total_pedidos que guarda la cantidad de pedidos hechos en el día.
Cada vez que se hace un pedido, la función nuevo_pedido() debe:

Mostrar cuántos pedidos había antes.
Aumentar el total en 1.
Mostrar cuántos pedidos hay ahora.

Pregunta:
¿Qué pasa si no usamos la palabra global dentro de la función?
¿Cómo se comporta una variable local con el mismo nombre?
"""

# Variable global
total_pedidos = 0  

def nuevo_pedido():
    # Intentar modificar la variable global
    total_pedidos += 1  
    print("Pedidos ahora:", total_pedidos)

nuevo_pedido()

#consigna
#Ejecutar el código tal cual → ¿Qué error aparece?
#Corregir usando global total_pedidos.
#Crear otra variable local llamada total_pedidos dentro de la función, y observar la diferencia.
