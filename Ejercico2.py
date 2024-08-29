#Hola
class Prestamo():
    nombrePersona=""
    Identificcion=""
    NombreLibro=""
    CodigoLibro=""
    fechaPedido=""
    FechaMAx=""
    DiasDespues=0
    EstadoLibro=""
    Sancion=""


    def pedirDatos(self):
        self.nombrePersona=input("Nombre del prestador: ")
        self.Identificcion=input("Codigo de su tarjeta: ")
        self.NombreLibro=input("Nombre del libro en prestacion: ")
        self.CodigoLibro=input("El codigo del libro: ")
        self.fechaPedido=input("Fecha que se ha solicitado: ")
        self.FechaMAx=input("Fecha hasta que se devolvera el libro: ")

    def sancion(self):
        if(self.DiasDespues<=5):
            print("La sancion sera de 6 dias sin prestamos")
        elif(self.DiasDespues<=10):
            print("La sancion sera de 15 dias sin prestamos")
        else:
            print("Tu sansion sera de un mes por burro")

    def estadoPrestamo(self):
        self.estadoPrestamo=input("Va a prestar o devolver un libro?: (Devolver=D/Prestar=p)").lower()
        if(self.estadoPrestamo=="p" or "prestar"):
            self.pedirDatos()
        else:
            self.estadoPrestamo=input("se paso de la cantidad de Dias a entregar? (s/n)")
            if(self.estadoPrestamo=="s" or "devolver"):
                self.DiasDespues=int(input("Cuantos Dias se paso de la fecha?: "))
                self.sancion()
            else:
                print("Gracias por ser puntual :D")

    
libro=Prestamo()
libro.estadoPrestamo()





