'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
def temperature_converter(Celcius_grades):
  Fahrenheit = 0
  Fahrenheit = (Celcius_grades * (9/5)) + 32
  return Fahrenheit
Fahrenheit_grades = temperature_converter (20)
print(Fahrenheit_grades)
