class Coche():
    def __init__(self):
        self.__largoCarroceria=400#atributos privados#para pruebas quita el private
        self.__anchoCarroceria=200
        self.__ruedas=4
        self.__color='blanco'
        self.__enMarcha=False

    def arrancar(self):
        self.enMarcha=True
    def estado(self):#si le pones __ se vuelve privado
        if(self.enMarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"

miCoche=Coche()
print(miCoche.largoCarroceria)
print("el coche tiene",miCoche.ruedas,"ruedas")
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())
print(isinstance(miCoche, Coche))