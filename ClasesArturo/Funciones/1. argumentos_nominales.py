def info_punto(x=1, y=2):
    print(f'Coordenadas {x=} {y=}')

info_punto()
info_punto(5)
info_punto(y=5)
info_punto(3, 2)

def info_punto_3d(x, y, z):
    print(f"Coordenadas {x=}, {y=}, {z=}")

punto = {"x": 4, "y": 7, "z": 4}
info_punto_3d(**punto) # Se pueden mandar valores en forma de diccionario de esta manera (desempaquetado de argumentos)
info_punto_3d(punto['x'], punto['y'], punto["z"])