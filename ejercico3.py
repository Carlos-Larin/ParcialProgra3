""""
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa

"""
class Habitacion:
    def _init_(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class Hotel:
    def _init_(self):
        self.habitaciones = []
        self.servicios_extra = {
            'piscina': 20,
            'cancha de golf': 50
        }

    def agregar_habitacion(self, tipo, precio):
        nueva_habitacion = Habitacion(tipo, precio)
        self.habitaciones.append(nueva_habitacion)

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones):
            print(f"{i + 1}. Tipo: {habitacion.tipo}, Precio: ${habitacion.precio}")

    def reservar_habitacion(self, eleccion, noches, servicios_seleccionados):
        habitacion = self.habitaciones[eleccion - 1]
        total = habitacion.precio * noches
        total_servicios = sum(self.servicios_extra[servicio] for servicio in servicios_seleccionados)
        total_final = total + total_servicios
        
        print(f"Factura detallada:")
        print(f"Habitación: {habitacion.tipo} - ${habitacion.precio} x {noches} noches")
        for servicio in servicios_seleccionados:
            print(f"Servicio extra: {servicio} - ${self.servicios_extra[servicio]}")
        print(f"Total a pagar: ${total_final}")


hotel = Hotel()
hotel.agregar_habitacion("Suite", 150)
hotel.agregar_habitacion("Doble", 100)
hotel.mostrar_habitaciones()


eleccion = int(input("Elige el número de habitación: "))
noches = int(input("Número de noches: "))
servicios = input("Servicios extra (separados por coma, ej. piscina, cancha de golf): ").split(", ")
hotel.reservar_habitacion(eleccion, noches, servicios)