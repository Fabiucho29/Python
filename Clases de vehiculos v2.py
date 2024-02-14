class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Marca: {self.brand} -- Año: {self.year}"
    
class Car:
    def __init__(self, brand, model, color, year):
        Vehicle.__init__(self, brand, year)
        self.model = model
        self.color = color

    def __str__(self):
        return f"""Marca: {self.brand} -- Modelo: {self.model}
Color: {self.color} -- Año: {self.year}"""
    
class Barco: 
    def __init__(self, brand, tipo, year):
        Vehicle.__init__(self, brand, year)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.brand} -- Tipo: {self.tipo} -- Año: {self.year}"
    
class Avion: 
    def __init__(self, brand, tipo, largo, year):
        Vehicle.__init__(self, brand, year)
        self.tipo = tipo
        self.largo = largo

    def __str__(self):
        return f"Marca: {self.brand} -- Tipo: {self.tipo} -- Largo: {self.largo} -- Año: {self.year}"
    
    
def main():
    print("Carro 1")
    carro_1 = Car("Toyota", "Corola", "Blanco", 2005)
    print(carro_1)
    print("Carro 2")
    carro_2 = Car("Nissan", "GT", "Negro", 2010)
    print(carro_2)

    print("Lancha")
    lancha = Barco("Barracuda", "Lancha", 2000)
    print(lancha)
    print("Yate")
    yate = Barco("Oceanco", "Yate", 1997)
    print(yate)

    print("Avión 1")
    avion_1 = Avion("Airbus", "Airbus 320", "38 metros", 2005)
    print(avion_1)
    print("Avión 2")
    avion_2 = Avion("Boeing", "Boeing 777", "74 metros", 2010)
    print(avion_2)

main()