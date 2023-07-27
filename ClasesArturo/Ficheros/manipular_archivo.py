from pathlib import Path

dir = Path("ClasesArturo", "Ficheros", "Archivos")
if not dir.exists():
    dir.mkdir()

file = dir.joinpath("archivo.txt")
print(file)
print(file.absolute())
with open(file, "w") as f:
    f.write("Hola")