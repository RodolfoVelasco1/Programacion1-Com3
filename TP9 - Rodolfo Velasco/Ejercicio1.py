#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP9

#EJERCICIO 1

class Persona:
    def __init__(self, name, age, DNI):
        self.name = name
        self.age = age
        self.dni = DNI
    #Getters
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_dni(self):
        return self.dni
    

    #Setters
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres")
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age < 120 and new_age >= 0:
            self.age = new_age
        else:
            raise ValueError("La edad no puede superar los 120 años, y tiene que ser un numero entero")
    def set_dni(self, new_dni):
        if isinstance(new_dni, int) and len(new_dni) <= 8:
            self.dni = new_dni
        else:
            raise ValueError("El dni debe ser un numero entero y tener menos de 8 numeros")

    #Mostrar datos
    def show_persona(self):
        print(f"Nombre: {self.name}, Edad: {self.age}, DNI: {self.dni}")
    #Verificar edad
    def mayorDeEdad(self):
        return self.age >= 18



# Ejemplo de uso:
persona = Persona("Juan", 25, "12345678X")

# Mostrar los datos de la persona
persona.show_persona()

# Comprobar si es mayor de edad
if persona.mayorDeEdad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")