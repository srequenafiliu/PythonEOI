def mod_num():
    n=10
    print(f"Función: n vale {n}")
n=24
mod_num()
print(f"Main: n vale {n}")

def mod_num2(n):
    n+=5
    print(f"Función: n vale {n}")
mod_num2(n)
print(f"Main: n vale {n}")

def mod_lista(lista):
    # lista = [*lista] # Alternativa a lista = lista.copy(). Esto modifica la lista dentro de la función pero no dentro
    lista[0] = 99
    print(f"Función: Lista -> {lista}")

lista = [1,2,3,4]
mod_lista(lista)
print(f"Main: Lista -> {lista}")