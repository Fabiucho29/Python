students = [{"name": "Harry", "age": 18, "house": "Gryffindor"}, 
{"name": "Germione", "age": 17, "house": "Slytherin"}]

usuario = {}

usuario["name"] = input("name: ")
usuario["age"] = input("edad: ")
usuario["house"] = input("casa: ")

students.append(usuario)

for student in students:
    print(student["name"])

for student in students:
    print(student)