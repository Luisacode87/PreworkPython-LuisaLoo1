'''Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
def suma(a,b):
  return a + b
def resta(a,b):
  return a - b
def multiplicacion(a,b):
  return a * b
def division(a,b):
  if b != 0:
   return a / b
  else:
    return("error matematico, b no puede ser 0")
print("las operaciones disponibles son:")
print("1. suma")
print("2. resta")
print("3. multiplicacion") 
print("4. division")
opcion = int(input("selecciona una opcion (1,2,3,4) : "))
num1 = float(input("introduzca el numero 1: "))
num2 = float(input("introduzca el numero 2: "))

if opcion ==1:
  resultado = suma(num1,num2)
elif opcion ==2:
  resultado = resta(num1,num2)
elif opcion ==3:
  resultado = multiplicacion(num1,num2)
elif opcion ==4:
  resultado = division(num1,num2)
else:
  resultado = "operacion no valida"
print(f"el resultado de la operacion es: {resultado}")

