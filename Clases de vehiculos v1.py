class Vehicle:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_attr(self):
        return f"""Marca: {self.brand} -- Modelo: {self.model}
Color: {self.color} -- Año: {self.year}"""
    
class Barco: 
    def __init__(self, marca, tipo, year):
        self.marca = marca
        self.tipo = tipo
        self.year = year

    def show_attr(self):
        return f"Marca: {self.marca} -- Tipo: {self.tipo} -- Año: {self.year}"
    
class Avion: 
    def __init__(self, tipo, largo, year):
        self.tipo = tipo
        self.largo = largo
        self.year = year

    def show_attr(self):
        return f"Tipo: {self.tipo} -- Largo: {self.largo} -- Año: {self.year}"
    
    
def main():
    print("Carro 1")
    carro_1 = Vehicle("Toyota", "Corola", "Blanco", 2005)
    print(carro_1.show_attr())
    print("Carro 2")
    carro_2 = Vehicle("Nissan", "GT", "Negro", 2010)
    print(carro_2.show_attr())

    print("Lancha")
    lancha = Barco("Barracuda", "Lancha", 2000)
    print(lancha.show_attr())
    print("Yate")
    yate = Barco("Oceanco", "Yate", 1997)
    print(yate.show_attr())

    print("Avión 1")
    avion_1 = Avion("Airbus 320", "38 metros", 2005)
    print(avion_1.show_attr())
    print("Avión 2")
    avion_2 = Avion("Boeing 777", "74 metros", 2010)
    print(avion_2.show_attr())

main()