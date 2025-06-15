# listar productos
def listar_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

#if __name__ == "__main__":
    #este modulo de por si no tiene sentido ejecutarlo
    #por lo tanto estas lineas no hacen falta
    #listar_producto(inventario)