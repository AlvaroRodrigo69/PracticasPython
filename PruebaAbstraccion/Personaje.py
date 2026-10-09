from abc import ABC, abstractmethod 
class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre=nombre
        self.nivel=0
        self.inventario=[]
        self.vida=100

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def estado(self):
        print("el personaje: ",self.nombre,"esta en el nivel:",self.nivel)

    def subirNivel(self):
        self.nivel+=1

    def verInventario(self):
        print(f"inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre=nombre
        self.inteligencia=100
        self.inventario=["Pocion de mana","Libro de hechizos"]
        self.vida=120
    def estado(self):
        print(f"Clase Mago")
        #seguir luego