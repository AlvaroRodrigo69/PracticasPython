class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.arranca=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.arranca=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        return f"la marca es {self.marca}, el modelo es {self.modelo}, arranca {self.arranca}, acelera {self.acelera}, frena {self.frena}"
    def moverse(self):
        print("me muevo con 4 ruedas")
    
class Camion(Vehiculo):
    def __init__(self, marca, modelo, descargando):
        super().__init__(marca, modelo)
        self.descargando=descargando
    def descargar(self):
        self.descargando="regular lo que estoy cargando"
    def estado(self):
        return f"{super().estado()}, descarga: {self.descargando}"
    def moverse(self):
        print("me muevo con muchas ruedas")
class v_electrico():
    def __init__(self):
        self.autonomia=500
    def moverse(self):
        print("me muevo con 4 ruedas")
class bici_electrica(Vehiculo, v_electrico):
    def moverse(self):
        print("me muevo con 2 ruedas")
mibici=bici_electrica('volvo','c4')#aunque no tiene ni super ni constructor necesita los atributos de cada cclase que extinde en la que se requieran parametros
#print(isinstance(mibici,v_electrico))
miCamion=Camion('volksvaguen', 'c7','regular lo que estoy cargando')
miCamion.descargar()

def moverVehiculo(miVehiculo):
    miVehiculo.moverse()
moverVehiculo(miCamion)
#print(miCamion.estado())
#isinstance(miCamion, Camion)
#isinstance(miCamion, Vehiculo)