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

def cargar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    #usar diccionarios anidados
    inventario[nombre] = {'precio': precio,'cantidad': cantidad}
    print(f"Producto '{nombre}' cargado exitosamente.")
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
            #buscar producto
            producto = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(inventario, producto)
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

if __name__ == "__main__":
    main()
# Fin del programa