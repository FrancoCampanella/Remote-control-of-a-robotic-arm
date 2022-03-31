class Articulacion:
	def __init__(self,longitud,v,nombre,angulo):
		self.nombre=nombre
		self.velocidad=v
		self.longitud=longitud
		self.angulo=angulo

	def set_posicion_A(self,angulo):
		self.angulo=angulo
		return self.angulo

	def set_velocidad_A(self,v):
		self.velocidad=v

	def get_angulo(self):
		V=self.angulo
		return V


