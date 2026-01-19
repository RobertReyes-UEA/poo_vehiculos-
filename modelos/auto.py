from modelos.vehiculo import Vehiculo

# Clase derivada Auto (Herencia)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Polimorfismo: método sobrescrito
    def describir(self):
        return f"Auto {self.marca} {self.modelo} con {self.puertas} puertas"
