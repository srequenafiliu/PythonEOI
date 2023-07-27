def sobreescribir(ruta):
    with open(ruta, 'w', encoding='utf-8') as f:
        for i in range(5):
            palabra = input(f"Dime la palabra nº{i+1}: ")
            f.write(palabra+"\n")

sobreescribir("ClasesArturo/Ficheros/Archivos/palabras.txt")

def add(ruta):
    with open(ruta, 'a', encoding='utf-8') as f:
        for i in range(5):
            palabra = input(f"Dime la palabra nº{i+1}: ")
            f.write(palabra+"\n")

add("ClasesArturo/Ficheros/Archivos/palabras.txt")