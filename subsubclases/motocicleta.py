from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo,velocidad,cilindrada)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__(self) + ",{} km/h, {} cc".format(self.velocidad,self.cilindrada)
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{(vehiculo).__class__.__name__}:, {vehiculo}")