# Variable global
total_pedidos = 0  

def nuevo_pedido():
    global total_pedidos   # avisar que se va usar la global
    print("Pedidos antes:", total_pedidos)
    total_pedidos += 1
    print("Pedidos ahora:", total_pedidos)

# Llamamos varias veces
nuevo_pedido()
nuevo_pedido()
nuevo_pedido()