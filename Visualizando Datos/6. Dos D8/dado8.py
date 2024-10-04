from random import randint

class Dado:
    def __init__(self,lados=8):
        self.lados = lados  
        
    def lanzar(self):
        return randint(1,self.lados)
        