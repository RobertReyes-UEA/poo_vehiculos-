# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__velocidad = 0  # Encapsulación (atributo privado)

    def acelerar(self, incremento):
        self.__velocidad += incremento

    def obtener_velocidad(self):
        return self.__velocidad

    # Método para polimorfismo
    def describir(self):
        return f"Vehículo {self.marca} modelo {self.modelo}"
