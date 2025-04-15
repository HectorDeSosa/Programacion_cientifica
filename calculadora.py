def suma (a,b):
    return a + b
def resta (a,b):
    return a - b
def multiplicacion (a,b):
    return a*b
def división (a,b):
    return a/b

print ("bienvenido a la calculadora basica")
print ("1=suma. 2=resta. 3=multiplicación. 4=división")
opcion = int(input("elige operación (1-4):" ))
num1 = float(input("primer número:" ))
num2 = float(input("segundo número:" ))           
if opcion == 1:
   print("resultado:", suma(num1, num2))
elif opcion == 2:
   print("resultado:", resta(num1, num2))  
elif opcion == 3:
   print("resultado:", multiplicacion(num1, num2))
elif opcion == 4:
   print("resultado:", división(num1, num2))


            