'''
1.Crea una clase Animal con los atributos nombre y peso. Esta clase tendrá además el método comer que incrementará el
peso en un 5% cada vez que se llame.
    ◦Crea además las clases Mamifero y Ave que heredan de animal. El mamífero tendrá también un booleano que indicará
    si es carnívoro o no. El ave tendrá un atributo booleano indicando si puede volar.
    ◦Implementa los respectivos métodos __repr__ para mostrar la información por pantalla (o usa dataclasses en su
    lugar si quieres)
2.Sobrescribe el método comer en la clase Mamifero. Hará lo mismo que cualquier animal, pero además imprimirá si ha
comido carne (carnívoro) o hierba (herbívoro)
    ◦Implementa además el método poner_huevos en Ave. Pondrá un número aleatorio entre 1 y 6 huevos, perdiendo 0.05 kg
    por cada huevo puesto. Imprime por consola los huevos que ha puesto.
3.Haz que la clase Animal sea abstracta. Además implementa un método abstracto llamado tipo_animal que devolverá un
string indicando el tipo de animal ◦Los mamíferos devolverán "Mamifero" y las aves "Ave"
4.Crea una clase Zoo con un nombre y una lista de Animales. Implementa los siguientes métodos:
    ◦add_animales o add_animal: Para añadir animales al zoo
    ◦print_animales: mostrará por la consola la lista de animales. Además del nombre y el peso, mostrará la siguiente
    información por animal:
        ▪Si el animal es mamífero indica si es un mamífero hervíboro o carnívoro
        ▪Si el animal es ave, indica si puede volar o no
    ◦num_animales (propiedad): devuelve la cantidad de animales que hay en el zoo
    ◦get_cantidad(tipo_animal): devuelve la cantidad de animales que hay de un tipo (coincidirá con lo que devuelve
    el método tipo_animal en las respectivas clases).
'''
from mamifero_class import Mamifero
from ave_class import Ave
from zoo_class import Zoo

animal1 = Mamifero("Conejo", 5, False)
animal2 = Mamifero("Lobo", 48, True)
animal3 = Ave("Búho", 2.5, True)
animal4 = Ave("Pingüino", 32.5, False)
print(f"{animal1} ({animal1.tipo_animal()})")
print(f"{animal2} ({animal2.tipo_animal()})")
print(f"{animal3} ({animal3.tipo_animal()})")
print(f"{animal4} ({animal4.tipo_animal()})")

animal1.comer()
print(f"Nuevo peso: {animal1.peso} kg")
animal2.comer()
print(f"Nuevo peso: {animal2.peso} kg")
animal3.poner_huevos()
print(f"Nuevo peso: {animal3.peso} kg")
animal4.poner_huevos()
print(f"Nuevo peso: {animal4.peso} kg")

zoo = Zoo("Terra Natura")
zoo.add_animales(animal1, animal2, animal3, animal4)
zoo.print_animales()
print(f"Número de animales: {zoo.num_animales}")
print(f"Cantidad de aves: {zoo.get_cantidad('Ave')}")
