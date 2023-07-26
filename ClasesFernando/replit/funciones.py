from random import randint, uniform, random

def esPrimo(numero):
  for i in range(numero-1, 1, -1):
    if numero%i == 0:
      return False
  return True

def ejercicio1():
  n1, n2 = 13, 6
  print(f'El número {n1} '+('no ' if not esPrimo(n1) else '')+'es primo')
  print(f'El número {n2} '+('no ' if not esPrimo(n2) else '')+'es primo')

def get_number(n_max):
  num = None
  while (type(num) != int or not num in range(1, n_max+1)):
    num = input(f'Introduzca un número del 1 al {n_max}: ')
    try:
      num = int(num)
    except:
      print('El dato introducido no es un número')
  return num

def comprobar(intento):
  if intento < numero:
    print(f'El número que buscas es mayor que {intento}')
  elif intento > numero:
    print(f'El número que buscas es menor que {intento}')
  else:
    return True
  return False

def ejercicio2():
  numero = randint(1,10)
  n_input = None
  n_intento = 1
  while n_input != numero:
    n_input = get_number(10)
    acierto = comprobar(n_input)
    if acierto:
      print(f'Enhorabuena. Has acertado en tu intento nº{n_intento}')
      break
    else:
      n_intento+=1

def n_in_list(num, lista):
    return num in lista

def ejercicio3():
  lista_num = [6,14,11,3,2,1,15,19]
  n_input = get_number(20)
  print(f'El número {n_input} '+('no ' if not n_in_list(n_input, lista_num) else '')+'se encuentra en la lista')