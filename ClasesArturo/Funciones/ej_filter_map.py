'''
Crea una lista de nombres. Crea otra lista con los nombres de la anterior que empiezan por 'A' en mayúsculas.
Intenta hacerlo de las 2 maneras, funcional y con listas por comprensión
'''

nombres = ['Pepe', 'Ana', 'Juan', 'Marta', 'Antonio', 'Pedro', 'Alejandro', 'Helena']
nombres_a = list(map(lambda n: n.upper(), filter(lambda n: n.startswith('A'), nombres)))
print(nombres_a)
nombres_a_2 = [n.upper() for n in nombres if n.startswith('A')]
print(nombres_a_2)