from FiguraGeometrica import FiguraGeometrica

class Ciculo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio=radio
    def calcular_area(self):
        total=3.14*(self.radio**2)
        return total

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, largo):
        super().__init__()
        self.ancho=ancho
        self.largo=largo
    def calcular_area(self):
        total=self.ancho*self.largo
        return total