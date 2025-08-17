# Para modificar el valor de una variable global.
# Para hacer que una variable local sea accesible fuera del alcance local.
x = 10 

def mostrarX():
    global x
    x = x + 2
    print("El valor de x es", x)
    

mostrarX()
# El valor de x es 12