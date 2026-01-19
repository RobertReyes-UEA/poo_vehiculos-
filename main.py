from modelos.auto import Auto
from servicios.servicio_vehiculo import ServicioVehiculo

# Crear objeto Auto
auto = Auto("Toyota", "Corolla", 4)

# Usar métodos
auto.acelerar(60)

# Servicio
servicio = ServicioVehiculo()
servicio.mostrar_info(auto)
