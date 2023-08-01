'''
1.Crea una clase llamada Examen que contenga 2 atributos (asignatura y nota). Crea un método constructor para inicializar
los parámetros y define el método __repr__ para representarla como string

2.Establece los atributos como privados (__ delante) y crea propiedades para acceder a ellos desde fuera de la clase.
La asignatura será de solo lectura, mientras que la nota se podrá cambiar pero nunca a un valor que no esté en el rango de 0 a 10

3.Crea una clase llamada Alumno con 3 atributos: nombre, curso (string), y exámenes. El último atributo será una lista de
exámenes que inicializaremos vacía en el constructor. Los atributos serán privados, crea propiedades de solo lectura para
el nombre, lectura/escritura para el curso (no puede estar vacío) y un método para añadir un examen.

4.Implementa el método __repr__ en Alumno donde muestres el nombre, curso y la lista de exámenes, así como una propiedad
computada llamada media, que te devuelva la media de los exámenes del alumno

5.Crea un método llamado print_media_asignaturas que muestre por pantalla, a partir de los exámenes de un alumno, cada
asignatura y la nota media de los exámenes de dicha asignatura que tenga el alumno

6.Pasa las clases Examen y Alumno a formato dataclass. Borra el constructor y el método __repr__ en ambas, ya que están
implícitos. Comprueba que todo funciona igual

7.Crea un atributo de clase en la clase Examen. Este atributo se llamará aprobado y tendrá un valor de 5. Crea un método
(normal, de instancia) llamado esta_aprobado, que devuelva True o False si la nota del examen es aprobado o no. En una
clase tipo dataclass, cuando le damos valor por defecto al atributo, se considera atributo de clase.
    · Crea un método en el alumno llamado print_eficiencia, que imprimacuantos exámenes están aprobados, cuantos suspensos,
    y cual es el porcentaje de aprobados
    
8.Crea un método de clase o estático llamado crear_novato que reciba el nombre de un alumno, y te devuelva un objeto Alumno
que pertenezca al curso '1ESO'.
'''

from examen_class import Examen
from alumno_class import Alumno

mates = Examen("Matemáticas", 8.4)
print(mates)
try:
    mates.nota = 14
except ValueError as e:
    print(e)
try:
    mates.nota = 8.75
except ValueError as e:
    print(e)
print(mates)

alumno1 = Alumno("Jorge", "3ESO")
print(alumno1)
try:
    alumno1.curso = ""
except ValueError as e:
    print(e)
alumno1.add_examenes(mates, Examen("Inglés", 6.25), Examen("Matemáticas", 7.5), Examen("Valenciano", 4))
print(alumno1)

print(f"Media de los exámenes: {alumno1.media:.2f}")
alumno1.print_media_asignaturas()
# alumno1.print_media_asignaturas_2()
alumno1.print_eficiencia()

alumno2 = Alumno.crear_novato("María")
print(alumno2)