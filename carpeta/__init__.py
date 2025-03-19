class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"
    
    def __name__(self):
        return self.__class__.__name__
    
    def catalogar(vehiculo):
        for vehiculo in vehiculo:
            print(type(vehiculo).__name__, vehiculo)