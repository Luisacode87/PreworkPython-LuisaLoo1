'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.

'''


def age_verify (age):
  if age >= 18:
    return ("Adult age verified sucessfully")
  else:
    return("Adult age was not able to verified")  
age = int (input("Please enter your age: "))
feedback_output = age_verify(age)
print(feedback_output) 




        