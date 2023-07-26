def get_int(texto):
  num = None
  while (type(num) != int):
    num = input('Introduzca '+texto+': ')
    try:
      num = int(num)
    except:
      print('El dato introducido no es un número')
  return num

def comparador(num):
    respuesta = f'El número {num} es '
    if num > 0:
        return respuesta+'un número positivo'
    elif num < 0:
        return respuesta+'un número negativo'
    else:
        return respuesta+'igual a cero'

def ejercicio1():
  print(comparador(get_int('un número')))
  print(comparador(get_int('un número')))
  print(comparador(get_int('un número')))
  
def ejercicio2():
  n1 = get_int('el número de inicio')
  n2 = get_int('el número de fin')
  suma = 0
  for num in range(n1, n2+1) if n2>n1 else range(n2,n1+1):
    suma += num
  print(f'El resultado es {suma}')

def ejercicio3():
  n1 = get_int('el número de inicio')
  n2 = get_int('el número de fin')
  s_par, s_impar = 0, 0
  for num in range(n1, n2+1) if n2>n1 else range(n2,n1+1):
    if num%2 == 0:
      s_par += num
    else:
      s_impar += num
  print(f'Los pares suman {s_par} y los impares suman {s_impar}')

def ejercicio4():
  usuario, password = 'root', 'toor'
  input_u = input('Introduzca el nombre de usuario: ')
  input_p = input('Introduzca la contraseña: ')
  print('¡Bienvenido' if input_u is usuario and input_p is password else 'Acceso fallido')

def ejercicio5():
  usuario, password = 'root', 'toor'
  intentos = 3
  for intento in range(intentos, -1, -1):
    input_u = input('Introduzca el nombre de usuario: ')
    input_p = input('Introduzca la contraseña: ')
    if input_u == usuario and input_p == password:
      print('¡Bienvenido!')
      break
    else:
      print('Datos incorrectos.', f'Intentos restantes: {intento}' if intento != 0 else 'Has agotado todos tus intentos')
      
def ejercicio6():
  lista_num = list()
  for i in range(0, 5):
    lista_num.append(get_int(f'el número ({i+1}/5)'))
  print(f"Lista de números: {lista_num}")
  print(f'El número más alto es {max(lista_num)}')

def ejercicio7():
  lista_num = list()
  dato = None
  while dato != 'fin':
    dato = input('Introduzca un número o \'fin\' para acabar: ')
    try:
      if dato != 'fin':
        dato = int(dato)
        lista_num.append(dato)
      else:
        break
    except:
      print('El dato introducido no es un número')
  print(f"Lista de números: {lista_num}")
  print(f'El número más alto es {max(lista_num)}')