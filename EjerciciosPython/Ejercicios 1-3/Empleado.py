from Persona import Persona

class Empleado(Persona):

    #Ejercicio 4
    def __init__(self, nombre, edad, altura, salario):
        super().__init__(nombre, edad, altura)
        self.salario=salario

    def __str__(self):
        return super().__str__()+f"{self.salario}"