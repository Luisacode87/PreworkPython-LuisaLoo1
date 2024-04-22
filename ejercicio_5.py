'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
suma = 0
for number in range (0,101):
   if number%2 == 0:
      suma += number
print(f"The sum of the numbers is: {suma}")
