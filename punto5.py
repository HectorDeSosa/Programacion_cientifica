
#Respuesta
from productos import listar_producto

def cargar_producto(inventario):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio unitario del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible del producto: "))
        #usar diccionarios anidados
        inventario[nombre] = {'precio': precio,'cantidad': cantidad}
        print(f"Producto '{nombre}' cargado exitosamente.")
    except ValueError:
        print("Error: Precio o cantidad no válidos. Por favor, ingrese valores numéricos.")
    return inventario

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Producto encontrado: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        
def main():
    inventario = {}
    while True:
        try:
            print("\n")
            print("Bienvenido al sistema de gestión de inventario.")
            print("1. Cargar producto")
            print("2. Listar productos")
            print("3. Buscar producto por nombre")
            print("4. Calcular valor total del inventario")
            print("5. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                #cargar producto
                inventario = cargar_producto(inventario)
            elif opcion == 2:
                #listar productos
                listar_producto(inventario)
            elif opcion == 3:
                try:
                    #buscar producto
                    producto = input("Ingrese el nombre del producto a buscar: ")
                    buscar_producto(inventario, producto)
                except ValueError:
                    print("Error: Entrada no válida. Por favor, ingrese un nombre de producto válido.")
            elif opcion == 4:
                #calcular valor total del inventario
                for datos in inventario.values():
                    valor_total = sum(datos['precio'] * datos['cantidad'])
                print(f"El valor total del inventario es: {valor_total:.2f}")
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.") 
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero para la opción.")
if __name__ == "__main__":
    main()
# Fin del programa