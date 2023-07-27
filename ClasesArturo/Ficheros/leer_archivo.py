def leer_fichero(ruta):
    with open(ruta, encoding='utf-8') as f:
        print(f.read())

def leer_fichero_linea(ruta):
    with open(ruta, encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            print(linea.strip())
            linea = f.readline()

def leer_fichero_linea_2(ruta):
    with open(ruta, encoding='utf-8') as f:
        for linea in f:
            print(linea.strip())

def leer_fichero_linea_3(ruta):
    with open(ruta, encoding='utf-8') as f:
        lineas = [linea.strip() for linea in f]
        print(lineas)
print("Método 1:")
leer_fichero("ClasesArturo/Ficheros/Archivos/palabras.txt")
print("Método 2:")
leer_fichero_linea("ClasesArturo/Ficheros/Archivos/palabras.txt")
print("Método 3:")
leer_fichero_linea_2("ClasesArturo/Ficheros/Archivos/palabras.txt")
print("Método 4:")
leer_fichero_linea_3("ClasesArturo/Ficheros/Archivos/palabras.txt")