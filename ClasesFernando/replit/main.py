import variables
import operadores
import estructuras_de_control
import listas_y_tuplas
import diccionarios
import funciones

def print_menu(tema, n_ej):
  print(f'Tema {tema}')
  for n in range (1, n_ej+1):
    print(f'{n}. Ejercicio {n}')
  print('0. Salir')
  return input('Seleccione un ejercicio: ')

def ej_variables():
  opcion = print_menu('Variables y tipos de datos', 5)
  match opcion:
    case "1":
      variables.ejercicio1()
    case "2":
      variables.ejercicio2()
    case "3":
      variables.ejercicio3()
    case "4":
      variables.ejercicio4()
    case "5":
      variables.ejercicio5()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

def ej_operadores():
  opcion = print_menu('Operadores y expresiones', 3)
  match opcion:    
    case "1":
      operadores.ejercicio1()
    case "2":
      operadores.ejercicio2()
    case "3":
      operadores.ejercicio3()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

def ej_estructuras_de_control():
  opcion = print_menu('Estructuras de control', 7)
  match opcion:
    case "1":
      estructuras_de_control.ejercicio1()
    case "2":
      estructuras_de_control.ejercicio2()
    case "3":
      estructuras_de_control.ejercicio3()
    case "4":
      estructuras_de_control.ejercicio4()
    case "5":
      estructuras_de_control.ejercicio5()
    case "6":
      estructuras_de_control.ejercicio6()
    case "7":
      estructuras_de_control.ejercicio7()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

def ej_listas_y_tuplas():
  opcion = print_menu('Listas y tuplas', 2)
  match opcion:
    case "1":
      listas_y_tuplas.ejercicio1()
    case "2":
      listas_y_tuplas.ejercicio2()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

def ej_diccionarios():
  opcion = print_menu('Diccionarios', 4)
  match opcion:
    case "1":
      diccionarios.ejercicio1()
    case "2":
      diccionarios.ejercicio2()
    case "3":
      diccionarios.ejercicio3()
    case "4":
      diccionarios.ejercicio4()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

def ej_funciones():
  opcion = print_menu('Funciones', 3)
  match opcion:
    case "1":
      funciones.ejercicio1()
    case "2":
      funciones.ejercicio2()
    case "3":
      funciones.ejercicio3()
    case "0":
      print('Volviendo al menú principal...')
    case _:
      print('Opción no válida')

tema = None
while tema != '0':
  print('''
  Ejercicios del libro "https://leanpub.com/aprende-python/"

  1. Variables y tipos de datos
  2. Operadores y expresiones
  3. Estructuras de control
  4. Listas y tuplas
  5. Diccionarios
  6. Funciones
  0. Salir
  ''')
  tema = input('Seleccione un tema: ')
  match tema:
    case "1":
      ej_variables()
    case "2":
      ej_operadores()
    case "3":
      ej_estructuras_de_control()
    case "4":
      ej_listas_y_tuplas()
    case "5":
      ej_diccionarios()
    case "6":
      ej_funciones()
    case "0":
      print('Hasta pronto :)')
    case _:
      print('Opción no válida')