from abc import ABC , abstractmethod

class FiguraGeometrica():
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def calcular_area(self):
        pass