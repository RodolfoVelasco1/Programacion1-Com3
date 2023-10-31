#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP9

#EJERCICIO 2

class Cuenta:
    def __init__(self, titular, cantidad=0):
        if titular is not None:
            self.titular = titular
        else:
            raise ValueError("El titular es obligatorio")
        self.cantidad = cantidad
    #Getters
    def get_titular(self):
        return self.titular
    def get_cantidad(self):
        return self.cantidad
    
    #Setters
    def set_titular(self, titular):
        if isinstance(titular, str):
            self.titular = titular
        else:
            raise ValueError("El Titular debe ser una cadena de caracteres")
    #Retiro
    def set_cantidad_retiro(self, cantidad):
        if isinstance(cantidad, float):
                self.cantidad -= cantidad
        else:
            raise ValueError("Ingresa un numero como cantidad")
    #Deposito
    def set_cantidad_deposito(self, cantidad):
        if isinstance(cantidad, float):
            if cantidad >= 0:
                self.cantidad += cantidad
        else:
            raise ValueError("Ingresa un numero como cantidad")
    
    #Mostrar datos
    def show_dates(self):
        print(f"Nombre del titular: {self.titular} y tiene un total de: {self.cantidad} ")


titular = "Juan"
cuenta = Cuenta(titular, 1000.0)

cuenta.show_dates()

cuenta.set_cantidad_deposito(500.0)
cuenta.show_dates()

cuenta.set_cantidad_retiro(300.0)
cuenta.show_dates()




