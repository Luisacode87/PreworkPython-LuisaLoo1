'''Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''
def edad_actual (nacimiento):
  calcular_edad = 2024 - nacimiento
  return calcular_edad
nacimiento = int(input("cual es su año de nacimiento: ? "))
edad_2024 = edad_actual(nacimiento)
print(f"tu edad actualmente en el 2024 es: {edad_2024}")
