def ejercicio1():
  lista = [12, 23, 5, 29, 92, 64]
  lista.insert(0, lista.pop())
  print('1.', lista)
  lista.append(lista.pop(1)) # Segunda posición = 1
  print('2.', lista)
  lista.insert(0, 14)
  print('3.', lista)
  suma = 0
  for n in lista:
    suma += n
  lista.append(suma)
  print('4.', lista)
  lista.extend([4, 11, 32])
  print('5.', lista)
  lista = [i for i in lista if i%2 == 0]
  print('6.', lista)
  lista.sort()
  print('7.', lista)
  lista.clear() 
  print('8.', lista)

def guardar_nums():
  lista = list()
  dato = None
  while dato != 'fin':
    dato = input('Introduzca un número o \'fin\' para acabar: ')
    try:
      if dato != 'fin':
        dato = int(dato)
        lista.append(dato)
      else:
        break
    except:
      print('El dato introducido no es un número')
  return lista

def ejercicio2():
  lista_1, lista_2 = guardar_nums(), guardar_nums()
  conjunto_1, conjunto_2 = set(lista_1), set(lista_2)
  print('Lista 1:', lista_1)
  print('Lista 2:', lista_2)
  print('Números coincidentes:', list(conjunto_1.intersection(conjunto_2)))