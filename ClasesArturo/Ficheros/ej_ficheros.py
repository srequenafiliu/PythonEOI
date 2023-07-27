'''
Crea un fichero llamado numeros.txt. En cada linea contiene un números
Crea un script de Python que lea los números y te muestre la suma y la media de esos números
'''

def ejercicio1(ruta):
    with open(ruta) as f:
        lista_num = [int(linea.strip()) for linea in f]
        print(f"Suma: {sum(lista_num)}")
        print(f"Media: {sum(lista_num)/len(lista_num)}")

'''
Ejercicio donde leemos el archivo productos.txt y a partir del mismo creamos por cada linea un diccionario
(ej:{nombre:'Silla', precio:34}). Guarda los diccionarios en una lista y muestra su contenido.
Además, muestra el producto más barato y la suma de los precios de los productos
'''
def get_lista_dict(ruta):
#   lista = list()
    with open(ruta, encoding='utf-8') as f:
        return [{'Nombre': producto, "Precio": int(precio)} for producto, precio in [linea.strip().split(';') for linea in f]]
#        for linea in f:
#            datos = linea.strip().split(';')
#            lista.append({'Nombre': datos[0], "Precio": datos[1]})
#    return lista

def ejercicio2():
    productos = get_lista_dict("ClasesArturo/Ficheros/Archivos/productos.txt")
    for producto in productos:
        print(producto)
    print(f"Producto más barato: {min(productos, key= lambda x: x['Precio'])}")
    '''
    productos.sort(key=lambda x: x["Precio"])
    print(f"Producto más barato: {productos[0]}")
    '''
    print(f"Suma de los precios: {sum(p['Precio'] for p in productos)}€")
    #print(f"Suma de los precios: {sum(map(lambda p: p['Precio'], productos))}€")

'''
Crea un archivo con varias palabras (a mano)
Crea un programa que lea las palabras del archivo y las guarde en una lista
Pregunta al usuario que adivine una palabra de las de la lista
Si la palabra está, felicítale
Si la palabra no está, díselo y añádela al final del archivo'''

from pathlib import Path
dir = Path("ClasesArturo", "Ficheros", "Archivos")
if not dir.exists():
    dir.mkdir()
file = dir.joinpath("adivinar.txt")

def get_lista_fichero(ruta):
    with open(ruta, encoding='utf-8') as f:
        return [linea.strip() for linea in f]

def ejercicio3():
    palabras = get_lista_fichero(file)
    word = input("Intente adivinar una palabra incluída en el fichero: ")
    print(f"Enhorabuena, \'{word}\' se encuentra en el fichero" if word in palabras else f"La palabra \'{word}\' no se encuentra en el fichero, pero se añadirá a continuación")
    if not word in palabras:
        with open(file, "a", encoding='utf-8') as f:
            f.write(f"{word}\n")

#ejercicio1("ClasesArturo/Ficheros/Archivos/numeros.txt")
#ejercicio2()
ejercicio3()