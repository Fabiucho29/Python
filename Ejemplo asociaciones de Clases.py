estudiantes = [{"nombre": "Juan", "apellido": "García", "edad": "19 años", "carrera": "Derecho"},
{"nombre": "Carlos", "apellido": "Fernandez", "edad": "21 años", "carrera": "Psicología"}
]

class Student:
    def __init__(self, name, apellido, age, career):
        self.name = name
        self.apellido = apellido
        self.age = age
        self.career = career

    def show(self):
        return f"Me llamo {self.name}, Mi apellido es {self.apellido}, tengo {self.age} años y estudio {self.career}"
        
class Clase:
    
    def __init__ (self, inicio, final, materia, profesor, student_1, student_2):
        self.inicio = inicio
        self.final = final
        self.materia = materia
        self.profesor = profesor
        self.student_1 = student_1
        self.student_2 = student_2

    def show(self):
        return f"""La clase inicia a las {self.inicio} y termina a las {self.final}. Es de {self.materia} y la da {self.profesor}"""

    def participantes(self):
        return f"""Están los alumnos:
        {student_1.show()}
        {student_2.show()}"""

student_1 = Student(estudiantes[0]["nombre"], estudiantes[0]["apellido"], estudiantes[0]["edad"], estudiantes[0]["carrera"])
student_2 = Student(estudiantes[1]["nombre"], estudiantes[1]["apellido"], estudiantes[1]["edad"], estudiantes[1]["carrera"])

clase = Clase("7 am", "8:30 am", "Ingeniería", "Juan Carlos", student_1, student_2)

print(clase.show())
print(clase.participantes())