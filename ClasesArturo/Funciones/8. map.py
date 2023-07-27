numeros = (23, 14, 67, 9, 8, 10, 11)

transformados = list(map(lambda n: n*2, numeros))
print(transformados)

transformados2 = [n*2 for n in numeros]
print(transformados2)

transformados3 = list(map(lambda n: int(n/2), filter(lambda n: n%2==0, numeros)))
print(transformados3)

transformados4 = [int(n / 2) for n in numeros if n % 2 == 0]
print(transformados4)