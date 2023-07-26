def ejercicio1():
  nombre = 'Michael Jordan'
  edad = 50
  media_puntos = 28.5
  activo = False
  print('Nombre:', nombre)
  print('Edad:', edad)
  print('Media de puntos:', media_puntos)
  print('¿Está activo?', 'Sí' if activo else 'No')

def ejercicio2():
  nombre = input('Introduzca su nombre: ')
  dni = input('Introduzca su DNI: ')
  edad = input('Introduzca su edad: ')
  print('Nombre:', nombre)
  print('DNI:', dni)
  print('Edad:', edad)

def ejercicio3():
  cadena = None
  while(cadena == None or len(cadena)<3):
    cadena = input('Introduzca una cadena de mínimo 3 caracteres: ')
  print('Resultado:', cadena[:3] + cadena[-3::])


def get_int(texto):
  num = None
  while (type(num) != int):
    num = input('Introduzca '+texto+': ')
    try:
      num = int(num)
    except:
      print('El dato introducido no es un número')
  return num

def ejercicio4():
  cadena = input('Introduzca una cadena: ')
  n1 = get_int('la posición del inicio de la subcadena')
  n2 = get_int('la longitud de la subcadena')
  print(cadena[n1:n1+n2] if len(cadena)>=n1+n2 else 'No se ha podido obtener la subcadena')

def ejercicio5():
  frase = input('Introduzca una frase: ')
  letra_reemplazada = input('Introduzca la letra que se quiere reemplazar: ')[0]
  reemplazo = input('Introduzca la letra que será el reemplazo: ')[0]
  print('Número de coincidencias:', frase.count(letra_reemplazada))
  print('Frase cambiada:', frase.replace(letra_reemplazada, reemplazo))