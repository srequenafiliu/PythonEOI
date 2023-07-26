def notas(alumno, *notas):
    print(f'La media de {alumno} es {sum(notas)/len(notas):.2f}')
notas('Jorge', 6.5, 8.3, 7)

def notas_dict(alumno, **notas):
    print(f"Matemáticas: {notas['Matemáticas']:.2f}")
    print(f"Castellano: {notas['Castellano']:.2f}")
    print(f"Inglés: {notas['Inglés']:.2f}")
    print(f'La media de {alumno} es {sum(notas.values())/len(notas):.2f}')
notas_dict('Jorge', Matemáticas=6.5, Castellano=8.3, Inglés=7)