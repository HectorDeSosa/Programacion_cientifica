# cargar productos
def listar_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")