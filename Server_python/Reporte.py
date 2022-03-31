class Reporte:
	def __init__(self, encendido,articulacion0,articulacion1,articulacion2,pinza,pos_pinza,velocidad,duracion):
		self.encendido=encendido
		self.articulacion0=articulacion0
		self.articulacion1=articulacion1
		self.articulacion2=articulacion2
		self.pinza=pinza
		self.pos_pinza=pos_pinza
		self.velocidad=velocidad
		self.duracion=duracion

	def get_reporte(self):
		if self.encendido == 1:
			self.encendido="encendido"
		else:
			self.encendido="apagado"
		if self.pinza == 1:
			mensaje="cerrada"
		elif self.pinza == 0:
			mensaje="abierta"

		return str("-El robot se encuentra " + str(self.encendido) + "\n-Sus articulaciones estan en los angulos:\n1) " + str(self.articulacion0) + "°\n2) " + str(self.articulacion1) + "°\n3) " + str(self.articulacion2) + "°\n-La pinza esta " +  mensaje + " ,en la posicion: "+str(self.pos_pinza) + "\n-La velocidad de operacion es " + str(self.velocidad) + "\n-Tiempo de operacion " + str(self.duracion) + " segundos")

