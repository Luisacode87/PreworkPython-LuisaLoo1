'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def calcular_imc (peso, altura):
  imc = peso / (altura**2)
  return imc

peso = float(input ("introduce tu peso en kgs: "))
altura = float(input("introduce tu altura en metros:"))

imc = calcular_imc(peso,altura)
print (f"Tu indice de masa corporal es: {imc:.2f}")
'''imc:.2f para redondear hasta el segundo decimmal'''
