class Jugador:
    def __init__(self, nombre, edad, sueldo) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__sueldo = sueldo
    def __repr__(self) -> str:
        return f"{self.__nombre}\n· Edad: {self.__edad}\n· Sueldo: {self.__sueldo}"

class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = list()
    def add_jugadores(self, *jugadores):
        self.__jugadores.extend(jugadores)
    def __repr__(self) -> str:
        return f"{self.__nombre}\n"+'\n'.join([str(j) for j in self.__jugadores]) # join() para una lista de objetos
        ''' 
        s = f"{self.__nombre}"
        for j in self.__jugadores:
            s += j
        return s
        '''
    @property
    def num_jugadores(self):
        return len(self.__jugadores)

e = Equipo("Patata CF")
e.add_jugadores(Jugador("Juan", 43, 24000), Jugador("Fran", 45, 26000), Jugador("Carlos", 46, 18000), Jugador("Miguel", 37, 50000))
print(e)
print("Número de jugadores:", e.num_jugadores)
e.add_jugadores(Jugador("Pepito", 38, 30000))
print("Número de jugadores:", e.num_jugadores)