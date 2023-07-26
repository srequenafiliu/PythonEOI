import math

def get_number():
  num = None
  while (type(num) != int or not num in range(1, 10)):
    num = input('Introduzca un número del 1 al 10: ')
    try:
      num = int(num)
    except:
      print('El dato introducido no es un número')
  return num

def ejercicio1():
  num = get_number()
  print(f'Tabla de multiplicar del {num}: ')
  for n in range(1, 11):
    print(f'· {num} x {n} = {n*num}')

def get_int(texto):
  num = None
  while (type(num) != int):
    num = input('Introduzca '+texto+': ')
    try:
      num = int(num)
    except:
      print('El dato introducido no es un número')
  return num

def ejercicio2():
  n1 = get_int('el primer número')
  n2 = get_int('el segundo número')
  print(f'Suma: {n1+n2}')
  print(f'Resta: {n1-n2}')
  print(f'Multiplicación: {n1*n2}')
  print(f'División: {n1/n2}' if n2 != 0 else 'No se puede dividir entre cero')

def area_circulo(r):
  return math.pi*(r**2)

def ejercicio3():
  radio = get_int('el radio')
  print(f'Área del círculo con radio {radio}: {area_circulo(radio)}')