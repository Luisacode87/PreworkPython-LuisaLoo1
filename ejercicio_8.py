'''Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros'''
def conversor_usd_eur (dolares):
  total_eur = dolares * 0.85
  return total_eur
dolares = float(input("dime cuantos dolares son: "))
total_eur = conversor_usd_eur(dolares)
print (f"El importe en euros es {total_eur:.2f}")


'''def calcular_imc (peso, altura):
  imc = peso / (altura**2)
  return imc

peso = float(input ("introduce tu peso en kgs: "))
altura = float(input("introduce tu altura en metros:"))

imc = calcular_imc(peso,altura)
print (f"Tu indice de masa corporal es: {imc:.2f}")'''

