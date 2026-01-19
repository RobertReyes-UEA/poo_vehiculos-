# Clase de servicio (lógica del sistema)
class ServicioVehiculo:
    def mostrar_info(self, vehiculo):
        print(vehiculo.describir())
        print("Velocidad actual:", vehiculo.obtener_velocidad(), "km/h")
