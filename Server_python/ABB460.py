from Articulacion import Articulacion
from Efector_final import Efector_final 
from os import remove
from datetime import date
from datetime import datetime
from Reporte import Reporte
import time
import math

class ABB460:
	def __init__(self):
		self.encendido=0 		#0=robot apagado

		self.velocidad=2       	#[rad/seg]
		self.Articulaciones=[Articulacion(122,self.velocidad,1,0),Articulacion(120,self.velocidad,2,90),Articulacion(120,self.velocidad,3,90)]
		self.pinza=Efector_final(0,self.Articulaciones[0].angulo,self.Articulaciones[0].longitud,self.Articulaciones[1].angulo,self.Articulaciones[1].longitud,self.Articulaciones[2].angulo,self.Articulaciones[2].longitud)
		self.i=3 			#Tres articulaciones del robot
		self.modo=0
		self.archivo=None
		self.elemento=-1

	def encender(self):
		if self.encendido==0:
			self.ti=datetime.now()
			time.sleep(2)
			self.encendido=1
			t=datetime.now()
			duracion=self.tiempo(self.ti,t)
			print(f"{self.ti.day}/{self.ti.month}/{self.ti.year} {self.ti.hour}:{self.ti.minute}:{self.ti.second}\nPower on\nTiempo de encendido:\n{duracion} seg")
			return f"{self.ti.day}/{self.ti.month}/{self.ti.year} {self.ti.hour}:{self.ti.minute}:{self.ti.second}\nPower on\nTiempo de encendido:\n{duracion} seg"
		else:
			print("El robot ya esta encendido")
			return "El robot ya esta encendido"

	def apagar(self):
		if self.encendido==1:
			self.tf=datetime.now()
			self.encendido=0
			duracion=self.tiempo(self.ti,self.tf)
			print(f"{self.tf.day}/{self.tf.month}/{self.tf.year} {self.tf.hour}:{self.tf.minute}:{self.tf.second}\nPower off\nTiempo de ejecución total:\n{duracion}")
			return f"{self.tf.day}/{self.tf.month}/{self.tf.year} {self.tf.hour}:{self.tf.minute}:{self.tf.second}\nPower off\nTiempo de ejecución total:\n{duracion}"
		else:
			print("El robot ya esta apagado")
			return "El robot ya esta apagado"
	def set_velocidad(self,v):
		if self.encendido==1:
			if v>0:
				self.velocidad=v
				self.Articulaciones[0].set_velocidad_A(self.velocidad)
				self.Articulaciones[1].set_velocidad_A(self.velocidad)
				self.Articulaciones[2].set_velocidad_A(self.velocidad)
				print("Velocidad seteada exitosamente\n")
				return "Velocidad seteada exitosamente\n"
			else:
				print("Error: la velocidad no puede ser negativa\n")
				return "Error: la velocidad no puede ser negativa\n"
		else:
			print("Debe encender el robot previamente")
			return "Debe encender el robot previamente"

	def set_posicion(self,vect):
		if self.encendido==1:
			if self.modo==0:
				ti=datetime.now()
				A=float(vect.split(',')[0])
				B=float(vect.split(',')[1])
				C=float(vect.split(',')[2])
				angulos=[A,B,C]
				for i in range (0,3):
					time.sleep(2)
					print(f"La posicion de la articulacion {i+1} es: {self.Articulaciones[i].set_posicion_A(angulos[i])}º")
				self.archivo=open('Posiciones.txt','a')
				self.archivo.write(f"{self.velocidad}\n{A}\n{B}\n{C}\n{self.pinza.estado}\n")
				self.archivo.close()
				print(f"La posicion del efector final es: {self.pinza.set_posicion(self.Articulaciones[0].angulo,self.Articulaciones[0].longitud,self.Articulaciones[1].angulo,self.Articulaciones[1].longitud,self.Articulaciones[2].angulo,self.Articulaciones[2].longitud)}")
				tf=datetime.now()
				tiempo=self.tiempo(ti,tf)
				print(f"Tiempo de ejecución del movimiento:\n{tiempo} segundos")
				return f"Articulacion 1: {A}º\nArticulacion 2: {B}º\nArticulacion 3: {C}º\nPosicion de la pinza:{self.pinza.pos} \nTiempo de ejecución del movimiento: {tiempo} segundos"
			else:
				try:
					
					ti=datetime.now()
					self.archivo=open('Posiciones.txt','r')
					lines=self.archivo.readlines()
					if self.elemento < len(lines)-1:
						self.elemento+=1
						self.velocidad=float(lines[self.elemento])
						self.elemento+=1
						A=float(lines[self.elemento])
						self.elemento+=1
						B=float(lines[self.elemento])
						self.elemento+=1
						C=float(lines[self.elemento])
						self.elemento+=1
						e=int(lines[self.elemento])
						mensaje=self.set_pinza(e)
						angulos=[A,B,C]
						for i in range (0,3):
							time.sleep(2)
							print(f"La posicion de la articulacion {i+1} es: {self.Articulaciones[i].set_posicion_A(angulos[i])}º")
						self.archivo.close()
						tf=datetime.now()
						tiempo=self.tiempo(ti,tf)
						print(f"La posicion del efector final es: {self.pinza.set_posicion(self.Articulaciones[0].angulo,self.Articulaciones[0].longitud,self.Articulaciones[1].angulo,self.Articulaciones[1].longitud,self.Articulaciones[2].angulo,self.Articulaciones[2].longitud)}")
						print(f"Tiempo de ejecución del movimiento:\n{tiempo} segundos\n")
						return f"Velocidad: {self.velocidad}\nArticulacion 1: {A}º\nArticulacion 2: {B}º\nArticulacion 3: {C}º\n{mensaje}, en la posicion: {self.pinza.pos}\nTiempo de ejecución del movimiento: {tiempo} segundos"
                
					else:
						self.elemento=-1
						print ("Fin")
						return "Fin"
				except FileNotFoundError:
					print("Error: Archivo no encontrado")
					return "Error: Archivo no encontrado"
		else:
			print("Debe encender el robot previamente")
			return "Debe encender el robot previamente"

	def set_pinza(self,e):
		ti=datetime.now()
		if self.encendido==1:
			time.sleep(2)
			self.pinza.set_estado(e)
			if self.pinza.estado==1:
				print("Pinza cerrada")
				return "La pinza esta cerrada"
			else: 
				print("Pinza abierta")
				return "La pinza esta abierta"
			tf=datetime.now()
			print(f"Tiempo de ejecución:\n{self.tiempo(ti,tf)} segundos")
		else:
			print("Debe encender el robot previamente")

	def homing(self):
		print("Velocidad: ",self.velocidad)
		ti=datetime.now()
		for i in range (0,self.i):
			time.sleep(2)
			if i==0:
				angulo=0
			elif i==1:
				angulo=90
			else: 
				angulo=90
			print(f"La posición de la articulación {i+1} es {self.Articulaciones[i].set_posicion_A(angulo)}º")
		tf=datetime.now()
		t=self.tiempo(ti,tf)
		print(f"El robot se ha movido a la posicion home con exito\nTiempo de ejecucion:\n{t} seg")
		return f"El robot se ha movido a la posicion home con exito\nArticulacion 1: {self.Articulaciones[0].get_angulo()}º\nArticulacion 2: {self.Articulaciones[1].get_angulo()}º\nArticulacion 3: {self.Articulaciones[2].get_angulo()}º\nTiempo de ejecucion:\n{t} seg"

	def set_modo(self,modo): 
		if self.encendido==1:
			if modo==0:  #modo manual=0, modo automatico=1
				self.modo=modo
				print("Robot en modo manual")
				return "Robot en modo manual"
			elif modo==1:
				self.modo=modo
				print("Robot en modo automatico")
				return "Robot en modo automatico"
			else:
				print("Error: modo no existente, elija 0 o 1")
				return "Error: modo no existente, elija 0 o 1"
		else:
			print("Debe encender el robot previamente")

	def borrar_archivo(self):
		if self.encendido==1:
			try:
				remove("Posiciones.txt")
				print("Archivo borrado con exito")
				return "Archivo borrado con exito"
			except FileNotFoundError:
				print("Error: Archivo no existente")
				return "Error: Archivo no existente"
		else:
			print("Debe encender el robot previamente")
	
	def get_info(self):
		t=datetime.now()
		self.duracion=self.tiempo(self.ti,t)
		reporte=Reporte(self.encendido,self.Articulaciones[0].angulo,self.Articulaciones[1].angulo,self.Articulaciones[2].angulo, self.pinza.estado,self.pinza.pos, self.velocidad, self.duracion)
		return str(reporte.get_reporte())

	def tiempo(self,ti,tf):
		tiempo=[int(ti.hour),int(ti.minute),int(ti.second)]
		tiempo=[int(tf.hour)-tiempo[0],int(tf.minute)-tiempo[1],int(tf.second)-tiempo[2]]
		aux=tiempo[0]*3600 + tiempo[1]*60 + tiempo[2]
		return aux


