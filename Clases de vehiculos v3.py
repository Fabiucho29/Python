class Seller:
    def __init__(self, vendedor, lugar=None):
        self.vendedor = vendedor
        self.lugar = lugar

    def __str__(self):
        return f"El vehículo lo vende {self.vendedor} en {self.lugar}"

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Marca: {self.brand} -- Año: {self.year}"
    
class Car:
    def __init__(self, brand, model, color, year, vendedor, lugar):
        Vehicle.__init__(self, brand, year)
        Seller.__init__(self, vendedor, lugar)
        self.model = model
        self.color = color

    def __str__(self):
        return f"""Marca: {self.brand} -- Modelo: {self.model}
Color: {self.color} -- Año: {self.year}
Vendedor: {self.vendedor} -- Lugar: {self.lugar}"""
    
class Barco: 
    def __init__(self, brand, tipo, year, vendedor):
        Vehicle.__init__(self, brand, year)
        Seller.__init__(self, vendedor)
        self.tipo = tipo
        self.vendedor = vendedor

    def __str__(self):
        return f"Marca: {self.brand} -- Tipo: {self.tipo} -- Año: {self.year} -- Vendedor: {self.vendedor}"
    
class Avion: 
    def __init__(self, brand, tipo, largo, year, vendedor):
        Vehicle.__init__(self, brand, year)
        Seller.__init__(self, vendedor)
        self.tipo = tipo
        self.largo = largo
        self.vendedor = vendedor

    def __str__(self):
        return f"Marca: {self.brand} -- Tipo: {self.tipo} -- Largo: {self.largo} -- Año: {self.year} -- Vendedor: {self.vendedor}"
    
    
def main():
    print("Carro 1")
    carro_1 = Car("Toyota", "Corola", "Blanco", 2005, "Ferrari", "Mercedes")
    print(carro_1)
    print("Carro 2")
    carro_2 = Car("Nissan", "GT", "Negro", 2010, "Nissan", "Tokyo")
    print(carro_2)

    print("Lancha")
    lancha = Barco("Barracuda", "Lancha", 2000, "TodoLanchas")
    print(lancha)
    print("Yate")
    yate = Barco("Oceanco", "Yate", 1997, "Yatch Club")
    print(yate)

    print("Avión 1")
    avion_1 = Avion("Airbus", "Airbus 320", "38 metros", 2005, "Airbus SA")
    print(avion_1)
    print("Avión 2")
    avion_2 = Avion("Boeing", "Boeing 777", "74 metros", 2010, "Boeing USA")
    print(avion_2)


def prueba(x, y):
    registro = Seller(x, y)
    return registro

main()

x = input("Cuál es el concecionario del vehículo? ")
y = input("Dónde queda el concecionario? ")
print(prueba(x,y))