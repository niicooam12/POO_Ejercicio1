from subclases.coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__(self) + ",{} kg".format(self.carga)
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{(vehiculo).__class__.__name__}:, {vehiculo}")