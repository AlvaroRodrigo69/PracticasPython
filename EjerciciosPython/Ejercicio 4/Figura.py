class Figura():
    def __init__(self):
        pass
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio=radio
    def calcular_area(self):
        return 3.14*self.radio**2
    
class Rectangulo(Figura):
    def __init__(self, ancho, largo):
        super().__init__()
        self.ancho=ancho
        self.largo=largo
    def calcular_area(self):
        return self.ancho*self.largo