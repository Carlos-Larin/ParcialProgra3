class Prestamo:
    def __init__(self):
        self.nombrePersona = ""
        self.Identificcion = ""
        self.NombreLibro = ""
        self.CodigoLibro = ""
        self.fechaPedido = ""
        self.FechaMAx = ""
        self.DiasDespues = 0
        self.EstadoLibro = ""
        self.Sancion = ""

    def pedirDatos(self):
        self.nombrePersona = input("Nombre del prestador: ")
        self.Identificcion = input("Codigo de su tarjeta: ")
        self.NombreLibro = input("Nombre del libro en prestacion: ")
        self.CodigoLibro = input("El codigo del libro: ")
        self.fechaPedido = input("Fecha que se ha solicitado: ")
        self.FechaMAx = input("Fecha hasta que se devolvera el libro: ")

    def sancion(self):
        if self.DiasDespues <= 5:
            print("La sancion sera de 6 dias sin prestamos.")
        elif self.DiasDespues <= 10:
            print("La sancion sera de 15 dias sin prestamos.")
        else:
            print("Tu sancion sera de un mes sin prestamos.")

    def estadoPrestamo(self):
        self.EstadoLibro = input("Va a prestar o devolver un libro?: (Devolver=D/Prestar=P) ").lower()
        if self.EstadoLibro == "p" or self.EstadoLibro == "prestar":
            self.pedirDatos()
        elif self.EstadoLibro == "d" or self.EstadoLibro == "devolver":
            estado = input("¿Se pasó de la cantidad de días para entregar? (s/n) ").lower()
            if estado == "s":
                self.DiasDespues = int(input("¿Cuántos días se pasó de la fecha?: "))
                self.sancion()
            else:
                print("Gracias por ser puntual :D")
        else:
            print("Opción no válida.")


libro = Prestamo()
libro.estadoPrestamo()
