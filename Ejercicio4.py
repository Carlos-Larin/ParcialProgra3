
"""
Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.
 Implementa la funcionalidad de rentar los vehículos disponibles
tomando en cuenta los datos del cliente.
"""

class Vehiculo:
    def _init_(self, tipo, marca, modelo, costo_por_dia):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.costo_por_dia = costo_por_dia
        self.disponible = True

    def mostrar_informacion(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"{self.tipo} - {self.marca} {self.modelo}: ${self.costo_por_dia} por día ({disponibilidad})")


class EmpresaRenta:
    def _init_(self):
        self.vehiculos = []
        self.datos_cliente = {}
        self.total_renta = 0

    def registrar_vehiculo(self, tipo, marca, modelo, costo_por_dia):
        vehiculo = Vehiculo(tipo, marca, modelo, costo_por_dia)
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos_disponibles(self):
        print("\nVehículos disponibles para rentar:")
        disponibles = [vehiculo for vehiculo in self.vehiculos if vehiculo.disponible]
        if disponibles:
            for vehiculo in disponibles:
                vehiculo.mostrar_informacion()
        else:
            print("No tenemos vehículos disponibles en este momento.")

    def seleccionar_vehiculo(self):
        self.mostrar_vehiculos_disponibles()
        eleccion = input("\nIngrese el tipo de vehículo que desea rentar: ").strip().lower()

        for vehiculo in self.vehiculos:
            if vehiculo.tipo.lower() == eleccion and vehiculo.disponible:
                vehiculo.disponible = False
                self.datos_cliente["vehiculo"] = vehiculo
                print(f"Has seleccionado el {vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo}.")
                return

        print("Vehículo no disponible o no encontrado.")
        self.seleccionar_vehiculo()

    def solicitar_datos_cliente(self):
        self.datos_cliente["nombre"] = input("\nNombre del cliente: ").strip()
        self.datos_cliente["dias_renta"] = int(input("Número de días de renta: "))
        self.total_renta = self.datos_cliente["vehiculo"].costo_por_dia * self.datos_cliente["dias_renta"]

    def generar_factura(self):
        print("\nFactura detallada:")
        print(f"Cliente: {self.datos_cliente['nombre']}")
        vehiculo = self.datos_cliente["vehiculo"]
        print(f"Vehículo rentado: {vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo}")
        print(f"Días de renta: {self.datos_cliente['dias_renta']}")
        print(f"Costo total: ${self.total_renta}")

    def ejecutar(self):
        if not any(vehiculo.disponible for vehiculo in self.vehiculos):
            print("Lo sentimos, no hay vehículos disponibles  en este momento.")
            return

        self.seleccionar_vehiculo()
        self.solicitar_datos_cliente()
        self.generar_factura()



empresa = EmpresaRenta()


empresa.registrar_vehiculo("SUV", "Toyota", "RAV4", 50)
empresa.registrar_vehiculo("Sedan", "Honda", "Civic", 40)
empresa.registrar_vehiculo("Camioneta", "Ford", "F-150", 70)


empresa.ejecutar()