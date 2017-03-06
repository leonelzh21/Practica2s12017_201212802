class NodoM(object):
	def __init__(self,correo,letra,dominio,indice):
		self.correo = correo
		self.letra = letra
		self.dominio = dominio
		self.indice = indice
		self.siguiente = None
		self.anterior = None
		self.arriba = None
		self.abajo = None
		self.profundidad = None

	def getCorreo(self):
		return self.correo

	def getLetra(self):
		return self.letra

	def getDominio(self):
		return self.dominio