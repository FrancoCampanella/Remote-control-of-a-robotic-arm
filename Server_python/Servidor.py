from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread 
#from Servidor_cmd import CLI
import socket
class XmlRpcServer(object):
	server=None
	RPC_port=8891
	def __init__(self, objeto,puerto = RPC_port):
		self.objeto_vinculado = objeto
		self.puerto_usado = puerto
		while True:
			try:
				self.server = SimpleXMLRPCServer(("localhost",self.puerto_usado),logRequests=None, allow_none=True)
				if self.puerto_usado != puerto:
					print("Servidor RPC ubicado en puerto no estandar [%d]" % self.puerto_usado)
				break
			except socket.error as e:
				if e.errno ==98:
					self.puerto_usado+=1
					continue
				else:
					print("El servidor RPC no puede ser iniciado")
					raise

		self.server.register_function(self.encender,'encender')
		self.server.register_function(self.apagar,'apagar')
		self.server.register_function(self.set_posicion ,'set_posicion')
		self.server.register_function(self.set_pinza, 'set_pinza')
		self.server.register_function(self.homing, 'homing')
		self.server.register_function(self.get_info, 'get_info')
		self.server.register_function(self.set_modo, 'modo')
		self.server.register_function(self.borrar_archivo, 'borrar_archivo')
		self.server.register_function(self.set_velocidad, 'velocidad')

		#Lanzo el servidor
		self.Hilo1 = Thread(target = self.run_server, daemon=True) 
		self.Hilo1.start()
		print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))

	def run_server(self):
		self.server.serve_forever()
	def shutdown(self):
		self.server.shutdown()
		#self.Hilo1.join()
		print("Servidor finalizado")
	def encender(self):
		return self.objeto_vinculado.encender()
	def apagar(self):
		return self.objeto_vinculado.apagar()
	def set_posicion(self,vect):    
		return self.objeto_vinculado.set_posicion(vect)
	def set_velocidad(self,v):
		return self.objeto_vinculado.set_velocidad(v)
	def set_pinza(self,e):    
		return self.objeto_vinculado.set_pinza(e)
	def homing(self):
		return self.objeto_vinculado.homing()
	def get_info(self):
		return self.objeto_vinculado.get_info()
	def set_modo(self,modo):
		return self.objeto_vinculado.set_modo(modo)
	def borrar_archivo(self):
		return self.objeto_vinculado.borrar_archivo()

