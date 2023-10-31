#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP9

#EJERCICIO 3

class Triangulo:
    
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def max_range(self):
        aux = []
        max_lado = 0
        aux.append(self.lado1)
        aux.append(self.lado2)
        aux.append(self.lado3)
        for value in aux:
            if value > max_lado:
                max_lado = value
        return (f"El lado del triangulo mas largo es de: {max_lado}")
    def what_triangle(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return (f"El triangulo es un equilatero con sus tres lados iguales: {self.lado1}")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return (f"El triangulo es un isóceles con dos de sus lados iguales {self.lado1}, {self.lado2}, {self.lado3}")
        else: 
            return (f"El triangulo es un escaleno con todos sus lados distintos {self.lado1}, {self.lado2}, {self.lado3}")


def programa_principal():
    lado1 = float(input("Ingrese el primer lado del triangulo: "))
    lado2 = float(input("Ingrese el segundo lado del triangulo: "))
    lado3 = float(input("Ingrese el tercero lado del triangulo: "))
    trinagulo_random = Triangulo(lado1, lado2, lado3)
    return (f"{trinagulo_random.max_range()}\n{trinagulo_random.what_triangle()}")

print(programa_principal())