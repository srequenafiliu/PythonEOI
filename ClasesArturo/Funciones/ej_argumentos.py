'''
Crea una función que reciba el nombre de un alumno y sus notas de forma individual.
Tienes que aprupar las notas (número indeterminado). Muestra el nombre del alumno, sus notas y la media
'''
def notas(alumno, *notas):
    print(f'La media de {alumno} es {sum(notas)/len(notas):.2f}')
notas('Jorge', 6.5, 8.3, 7)

def notas_dict(alumno, **notas):
    print(f"Matemáticas: {notas['Matemáticas']:.2f}")
    print(f"Castellano: {notas['Castellano']:.2f}")
    print(f"Inglés: {notas['Inglés']:.2f}")
    print(f'La media de {alumno} es {sum(notas.values())/len(notas):.2f}')
notas_dict('Jorge', Matemáticas=6.5, Castellano=8.3, Inglés=7)