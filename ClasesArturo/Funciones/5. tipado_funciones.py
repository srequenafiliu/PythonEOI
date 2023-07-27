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