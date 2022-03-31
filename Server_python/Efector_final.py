import math

class Efector_final:

    def __init__(self, estado,a1,l1,a2,l2,a3,l3):
        self.estado=estado
        self.posx=(l2*math.cos(math.radians(a2))+l3*math.cos(math.radians(a3)))*math.cos(math.radians(a1))
        self.posx=round(self.posx,2)
        self.posy=(l2*math.cos(math.radians(a2))+l3*math.cos(math.radians(a3)))*math.sin(math.radians(a1))
        self.posy=round(self.posy,2)
        self.posz=l1+l2*math.sin(math.radians(a2))+l3*math.sin(math.radians(a3))
        self.posz=round(self.posz,2)
        self.pos=[self.posx,self.posy,self.posz]



    def set_estado(self,e):
        self.estado
        return self.estado



    def set_posicion(self,a1,l1,a2,l2,a3,l3):
        self.posx=(l2*math.cos(math.radians(a2))+l3*math.cos(math.radians(a3)))*math.cos(math.radians(a1))
        self.posx=round(self.posx,2)
        self.posy=(l2*math.cos(math.radians(a2))+l3*math.cos(math.radians(a3)))*math.sin(math.radians(a1))
        self.posy=round(self.posy,2)
        self.posz=l1+l2*math.sin(math.radians(a2))+l3*math.sin(math.radians(a3))
        self.posz=round(self.posz,2)
        self.pos=[self.posx,self.posy,self.posz]
        return self.pos
