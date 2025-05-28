#Una tienda online desea desarrollar una aplicación básica en Python para gestionar su inventario de productos. Actualmente, todo lo hacen en papel, lo que genera errores y pérdida de información. El objetivo es informatizar el sistema de carga, consulta y análisis del stock.

#Cada producto tiene los siguientes datos:
#Nombre (cadena de texto)
#Precio unitario (número con decimales)
#Cantidad disponible (entero)

#La aplicación debe permitir:
#Cargar productos (nombre, precio y cantidad).
#Listar todos los productos.
#Buscar un producto por nombre.
#Eliminar productos (nombre, cantidad).
#Calcular el valor total del inventario.
#Aplicar descuentos a los productos usando una función.

#Respuesta
from productos import listar_producto

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Producto encontrado: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
def eliminar_producto(inventario, nombre, cantidad):
    if nombre in inventario:
        if inventario[nombre]['cantidad'] >= cantidad:
            inventario[nombre]['cantidad'] -= cantidad
            print(f"Se han eliminado {cantidad} unidades del producto '{nombre}'.")
            if inventario[nombre]['cantidad'] == 0:
                del inventario[nombre]
                print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"No hay suficiente cantidad de '{nombre}' para eliminar.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

#menu
def menu():
    print("1. Cargar producto")
    print("2. Listar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Aplicar descuento a un producto")
    print("7. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion
# cargar productos
inventario = dict()
def main():
    print("Bienvenido al sistema de gestión de inventario.")
    opcion = menu()
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio unitario del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible del producto: "))
        
        inventario[nombre] = {
            'precio': precio,
            'cantidad': cantidad
        }
        print(f"Producto '{nombre}' cargado exitosamente.")
    elif opcion == 2:
        #listar productos
        listar_producto(inventario)
    elif opcion == 3:
        producto = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto(inventario, producto)
    elif opcion == 4:
        producto = input("Ingrese el nombre del producto a eliminar: ")
        cantidad = int(input("Ingrese la cantidad a eliminar: "))
        # llamar lógica de eliminación
        eliminar_producto(inventario, producto, cantidad)
    elif opcion == 5:
        valor_total = sum(datos['precio'] * datos['cantidad'] for datos in inventario.values())
        print(f"El valor total del inventario es: {valor_total:.2f}")
    elif opcion == 6:
        nombre = input("Ingrese el nombre del producto al que desea aplicar un descuento: ")
        descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))
        if nombre in inventario:
            precio_original = inventario[nombre]['precio']
            nuevo_precio = precio_original * (1 - descuento / 100)
            inventario[nombre]['precio'] = nuevo_precio
            print(f"Descuento aplicado. Nuevo precio de '{nombre}': {nuevo_precio:.2f}")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
    elif opcion == 7:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.") 

# Fin del programa