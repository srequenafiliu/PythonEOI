s = str('Hola')
print(s, type(s))
s = int(23)
print(s, type(s))

def suma(n1: int, n2: int) -> int:
    return n1 + n2

#print(suma('Hola', 'Adiós')) Da error
print(suma(2, 3))

def ordena_mayus(lista: list[str]) -> list[str]:
    lista = [*lista] # Así no se modifica la lista original
    lista = [s.upper() for s in lista]
    lista.sort()
    return lista

nombres = ['Pepe', 'Juan', 'Marta', 'Antonio']
nombres_ordenados = ordena_mayus(nombres)
print('Nombres:', nombres)
print('Nombres ordenados:', nombres_ordenados)

resta = lambda n1, n2: n1 - n2
print(type(suma))
print(type(resta))

print('Suma:', suma(5, 3))
print('Resta:', resta(5, 3))

def operar(f, n1:int, n2:int) -> int:
    return f(n1, n2)

print('Suma:', operar(suma, 4, 5))
print('Resta:', operar(resta, 4, 5))
print('Multiplicación:', operar(lambda n1, n2: n1*n2, 4, 5))

nombres = ["Pepe", "Ana", "Marcos", "Anastasia", "Pedro"]
nombres.sort(key = lambda n: len(n))
print(nombres)

personas = [
    {"Nombre":"Pepe", "Edad": 23},
    {"Nombre":"Ana", "Edad": 65},
    {"Nombre":"María", "Edad": 15},
    {"Nombre":"Alberto", "Edad": 35}
]
personas.sort(key = lambda n: n["Nombre"])
print('Ordenados por nombre:', personas)
personas.sort(key = lambda n: n["Edad"])
print('Ordenados por edad:', personas)