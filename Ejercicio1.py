"""
Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.

 En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código.

"""

class theGoodDoctor():
    Doctor1="Dr. Chapatin, Especialidad Huesos"
    Doctor2="Dr. Lorenxo, Especialidad Corazon"
    Doctor3="Dr. Arthur Morgan, Especialidad Alergias"
    Doctor4="Dr. Willyrex, Especialidad Mewing"
    ConQuien=""
    PrecioXConsulta=0
    NombreDelPaciente=""
    Encargado=""
    Receta=""
    NunFon=""
    total=0
    Edad=0
    cuadro=""
    MotivoDConsulta=""
    UltimaConsulta=""
    FechaPrxConsulta=""

    def __init__(self):
        self.PrecioXConsulta=0
        self.NombreDelPaciente=""
        self.Encargado=""
        self.Receta=""
        self.total=0
        self.Edad=0
        self.MotivoDConsulta=""
        self.UltimaConsulta=""
    
    def DatosNuevo(self):
        self.RegistroConsulta()
        self.NombreDelPaciente=input("Nombre del paciente: ")
        self.NunFon=input("Numero de telefono: ")
        self.Encargado=input("Nombre del encargado o acompañante: ")
        self.Edad=int(input("Edad del Paciente: "))
        self.MotivoDConsulta=input("Cual es el motivo de su consulta: ")
        

    def RegistroConsulta(self):
        print(f"Doctores en este consultorio: \n"
              f"{self.Doctor1} Marque Opcion= 1\n"
              f"{self.Doctor2} Marque Opcion= 2\n"
              f"{self.Doctor3} Marque Opcion= 3\n"
              f"{self.Doctor4} Marque Opcion= 4\n"
              )
        self.ConQuien=int(input("Opcion seleccionada: (Numero)= "))
        if(self.ConQuien==1):
            print(f"El paciente {self.NombreDelPaciente} pasara con el {self.Doctor1}")
            self.PrecioXConsulta=float(input("Precio de la consulta: "))
        elif(self.ConQuien==2):
            print(f"El paciente {self.NombreDelPaciente} pasara con el {self.Doctor2}")
            self.PrecioXConsulta=float(input("Precio de la consulta: "))
        elif(self.ConQuien==3):
            print(f"El paciente {self.NombreDelPaciente} pasara con el {self.Doctor3}")
            self.PrecioXConsulta=float(input("Precio de la consulta: "))
        elif(self.ConQuien==4):
            print(f"El paciente {self.NombreDelPaciente} pasara con el {self.Doctor4}")
            self.PrecioXConsulta=float(input("Precio de la consulta: "))
    print("____________________________________________________")

    def HacerRegistro(self):
        self.cuadro=input("Ya habia pasado antes?: (S/N)").lower()
        if(self.cuadro=="s"):
            print("Pase a la Sala de espera en un momento se le atendera...")
            self.FechaPrxConsulta=input("Cuando sera su proxima consulta?: ")
            print("____________________________________________________")
        else:
            self.DatosNuevo()
            print("Pase a la Sala de espera en un momento se le atendera...")
            self.FechaPrxConsulta=input("Cuando sera su proxima consulta?: ")
            paciente.MostrarCuadro()
            print("____________________________________________________")
    print("____________________________________________________")

    def MostrarCuadro(self):
        print(f"Nombre del Paciente: {self.NombreDelPaciente}")
        print(f"Nombre del encargado: {self.Encargado}")
        print(f"edad del paciente: {self.Edad}")
        print(f"numero de telefono: {self.NunFon}\n"
              f"Motivo de su consult {self.MotivoDConsulta}")
        print(f"fue atendido por: {self.ConQuien} y su proxima consulta sera {self.FechaPrxConsulta}")
        print(f"El precio a pagar es de: {self.PrecioXConsulta}")


paciente=theGoodDoctor()
paciente.HacerRegistro()
print("____________________________________________________")
print("__________Gracias por su preferencia________________")