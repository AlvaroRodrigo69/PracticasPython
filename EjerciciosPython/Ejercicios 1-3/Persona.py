class Persona():

    #Ejercicio 1
    def __init__(self, nombre, edad, altura):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
    
    def __str__(self):
        return f"{self.nombre},{self.edad},{self.altura}"

    #Ejercicio 2
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

