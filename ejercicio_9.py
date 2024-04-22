'''Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''
def dia_semana (numero):
  lista_dias_semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
  if numero >=1 and numero <=7:
    return lista_dias_semana[numero-1]
  else:
    print ("no es un número entre el 1 y 7, vuelva a introducir un numero dentro de este rango")

numero = int(input("introduce un numero del 1 al 7: "))
nombre_dia = dia_semana(numero)
print (f"El dia de la semana es {nombre_dia}")


   