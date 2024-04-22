'''Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
def area_rectangulo(largo,ancho):
  calcular_area = largo * ancho
  return calcular_area
largo = float(input("introduzca el largo en cms: "))
ancho = float(input("introduzca el ancho en cms: "))
calcular_area = area_rectangulo(largo,ancho)
print(f"el area en cms es: {calcular_area}")
