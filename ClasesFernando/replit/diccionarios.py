def ejercicio1():
  lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
  dict_numeros = dict()
  for n in lista:
    dict_numeros[n] = lista.count(n)
  print(dict_numeros)

def ejercicio2():
  diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
  valores = list(set(diccionario.values()))
  print(valores)

def ejercicio3():
  usuarios = {
    "iperurena": {
      "nombre": "Iñaki",
      "apellido": "Perurena",
      "password": "123123"
    },
    "fmuguruza": {
      "nombre": "Fermín",
      "apellido": "Muguruza",
      "password": "654321"
    },
    "aolaizola": {
      "nombre": "Aimar",
      "apellido": "Olaizola",
      "password": "123456"
    }
  }
  intentos = 3
  for intento in range(intentos, -1, -1):
    input_u = input('Introduzca el nombre de usuario: ')
    input_p = input('Introduzca la contraseña: ')
    if input_u in usuarios and input_p == usuarios[input_u]['password']:
      print(f"¡Bienvenid@ {usuarios[input_u]['nombre']} {usuarios[input_u]['apellido']}!")
      break
    else:
      print('Datos incorrectos.', f'Intentos restantes: {intento}' if intento != 0 else 'Has agotado todos tus intentos')


def get_float(texto):
  num = None
  while (type(num) != float):
    num = input('Introduzca '+texto+': ')
    try:
      num = float(num)
    except:
      print('El dato introducido no es un número')
  return num

def add_students(diccionario, nombre):
  nota = get_float(f'la nota de {nombre}')
  diccionario[len(diccionario)+1] = {'nombre': nombre, 'nota': nota}
  
def ejercicio4():
  n_estudiantes = 10
  estudiantes = dict()
  for i in range(1, n_estudiantes+1):
    nombre = input(f'Introduzca el nombre del estudiante ({i}/{n_estudiantes}) o \'fin\' para acabar: ')
    if (nombre != 'fin'):
      add_students(estudiantes, nombre)
    else:
      break
  aprobados = [estudiante['nombre'] for estudiante in estudiantes.values() if estudiante["nota"] >= 5]
  suspendidos = [estudiante['nombre'] for estudiante in estudiantes.values() if estudiante["nota"] < 5]
  notas = [estudiante['nota'] for estudiante in estudiantes.values()]
  print('Lista de alumnos suspendidos:', ', '.join(suspendidos))
  print('Lista de alumnos aprobados:', ', '.join(aprobados))
  print(f'Media de los alumnos: {(sum(notas)/len(notas)):.2f}')