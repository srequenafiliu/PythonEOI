def suma(*numeros): # Parámetro con ‘*’: Agrupa en una tupla todos los valores recibidos
    print('Suma:', sum(numeros))
    
suma(3, 4, 5, 2, 7)
suma(3, 4, 5)
suma(6)
suma()

def info_persona(nombre, *aficiones):
    print(f"Las aficiones de {nombre} son: {', '.join(aficiones)}")
    
info_persona("Pedro", "Viajar", "Tenis", "Dormir")

def agrupa1(**valores):
    print(valores)

agrupa1(nombre = "Pepito", edad = 46, correo = "pepito@gmail.com")

def agrupa2(*posicionales, **nominales):
    print(f"Posicionales: {posicionales}, nominales: {nominales}")

agrupa2(34, 65, 100, edad = 24, nombre = "Juan")