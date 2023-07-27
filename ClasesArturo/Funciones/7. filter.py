numeros = (23, 14, 67, 9, 8, 10, 11)

pares = tuple(filter(lambda n: n%2==0, numeros))
print(pares)

pares2 = [n for n in numeros if n%2==0]
print(pares2)