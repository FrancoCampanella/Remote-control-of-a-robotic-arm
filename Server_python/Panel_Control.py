from Servidor import XmlRpcServer
from cmd import Cmd 
from Articulacion import Articulacion 
from Efector_final import Efector_final 
from ABB460 import ABB460

class CLI(Cmd):
	doc_header = "Ayuda de comandos documentados"
	undoc_header = "                   Ayuda de comandos no documentados                   "
	objeto_vinculado=None
	servidor=None
	def do_server(self, args):
		if self.servidor==None:
			if self.objeto_vinculado==None:
				self.objeto_vinculado=ABB460()
				self.servidor = XmlRpcServer(self.objeto_vinculado)
			else:
				self.servidor = XmlRpcServer(self.objeto_vinculado)
		else:
			print("El servidor ya ha sido lanzado")

	def do_shutdown_server(self, args):

		if self.servidor==None:
			print("Error: ejecute el metodo 'server\' previamente")
		else:
			self.servidor.shutdown()
			self.servidor=None
			
	def do_encender(self, args):
		
		if self.objeto_vinculado==None:
			self.objeto_vinculado=ABB460()
			self.objeto_vinculado.encender()
		else:
			self.objeto_vinculado.encender()

	def do_apagar(self, args):
		if self.objeto_vinculado==None:
			self.objeto_vinculado=ABB460()
			self.objeto_vinculado.apagar()
		else:
			self.objeto_vinculado.apagar()
			self.objeto_vinculado=None

	def do_posicion(self, args):
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print("")
		else:
			v=str(input("Ingrese los angulos de rotacion de cada eje separados por \',\':\n"))
			self.objeto_vinculado.set_posicion(v)
			print("")

	def do_pinza(self, args):
		
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print("")
		else:
			e=int(input("Ingrese 0 para abrir la pinza o 1 para cerrarla"))
			print(self.objeto_vinculado.set_pinza(e))

	def do_quit(self, args):
		print("Ejecucion terminada")
		raise SystemExit

	def do_homing(self, args):
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print()
		else:
			self.objeto_vinculado.homing()

	def do_modo(self, args):
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print()
		else:
			mod=int(input("0-Modo manual\n1-Modo automatico\n"))
			if mod==0:
				self.objeto_vinculado.set_modo(mod)
			elif mod==1:
				print("\n====================================================\nIniciando posicionamiento automatico")
				self.objeto_vinculado.set_modo(mod)
				while self.objeto_vinculado.elemento!=-1:
					self.objeto_vinculado.set_modo(mod)
				print("Ejecucion automática finalizada\n====================================================\n")
	
	def do_borrar_archivo(self, args):
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print()
		else:
			self.objeto_vinculado.borrar_archivo()

	def do_set_velo(self, args):
		if self.objeto_vinculado==None:
			print("Por favor encienda el robot ABB460 antes de ejecutar este metodo")
			print()
		else:
			v=float(input("Introduzca la velocidad de operacion en [rad/seg]:\n"))
			self.objeto_vinculado.set_velocidad(v)

	def default(self, args):
		print("Error. El comando \'" + args + "\' no esta disponible")

	def precmd(self, args):
		args = args.lower()
		return(args)   
     
if __name__ == "__main__":
	uncli = CLI()
	uncli.prompt = '- '
	uncli.cmdloop('Iniciando entrada de comandos...')

