'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

def count_vowels(text):
    vowels_definition = "aeiouAEIOU"
    counter = 0
    for letter in text:
        if letter in vowels_definition:
            counter += 1
    return counter
text = input("Please enter a text: ")
quantity_vowels = count_vowels(text)
print(f"You have entered this quantity of vowels : {quantity_vowels}")

