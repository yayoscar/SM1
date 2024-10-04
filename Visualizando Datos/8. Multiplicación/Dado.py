from random import randint

class Dado:
    def __init__(self,caras = 6):
        self.caras = caras

    def lanzar(self):
        return randint(1,self.caras)
