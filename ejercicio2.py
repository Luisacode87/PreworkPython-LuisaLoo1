'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
def tips_calculator(amount_without_tips):
  tips = amount_without_tips * 0.15
  total_to_cash = amount_without_tips + tips
  return total_to_cash
amount_without_tips = float (input("Total amount before tips is: "))
Total_billing = tips_calculator(amount_without_tips)
print (f"Total of the bill is:  {Total_billing}")




