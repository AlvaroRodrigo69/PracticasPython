class Perro():
    def __init__(self, raza, color, peso, edad, sexo):
        self.raza=raza
        self.color=color
        self.peso=peso
        self.edad=edad
        self.sexo=sexo

    #Este metodo tiene sentido que sea de objeto ya que cruza al perro que lo llama con el que recibe por parametros
    def cruzar(self, perro2):
        cachorro=None
        if(self.sexo!=perro2.sexo):
            if(self.sexo=='hembra'):
                cachorro=Perro(self.raza, self.color, 1,0, self.sexo)
            else:
                cachorro=Perro(perro2.raza, perro2.color, 1,0, perro2.sexo)
        return cachorro

    #Este metodo tiene sentido que sea estatico, ya que si fuese de objeto no tendria sentido llamar a un perro para cruzar a otros dos perros distintos
    @staticmethod
    def cruzar2(perro, perro2):
            cachorro=None
            if(perro.sexo!=perro2.sexo):
                if(perro.sexo=='hembra'):
                    cachorro=Perro(perro.raza, perro.color, 1,0, perro.sexo)
                else:
                    cachorro=Perro(perro2.raza, perro2.color, 1,0, perro2.sexo)
            return cachorro

    #Este metodo tiene sentido que sea estatico 
    #ya que no tendria sentido necesitar a un perro suelto para
    #que me devuelva una lista creada a partir de dos listas que se pasan por parametros
    @staticmethod
    def obtenerHembras(li, li2):
        listaCompleta=li+li2
        listaHembras=[]
        for perro in listaCompleta:
            if(perro.sexo=='hembra'):
                listaHembras.append(perro)
        return listaHembras

    #Este metodo debe ser de objeto ya qu se pide que se busque al perro mas afin para el perro desde el que se llama
    def obtenerParejaMasAfin(self, li):
        listaAfines=[]
        for perro in li:
            if(perro.sexo!=self.sexo):
                if(self.peso==perro.peso or perro.peso>=(self.peso-2) and perro.peso<=(self.peso+2)):
                    listaAfines.append(perro)
        perroAfin=None
        if(listaAfines):
            perroAfin=listaAfines[0]
        return perroAfin
    
    #metodo para ver los datos del objeto en forma de string
    def __str__(self):
        return f"{self.raza},{self.color},{self.peso},{self.edad},{self.sexo}"