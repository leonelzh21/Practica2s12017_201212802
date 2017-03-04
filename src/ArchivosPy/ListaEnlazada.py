class Nodo(object):
	def __init__(self,elemnt,i):
		#variable que gurada la informacion
		self.texto = elemnt
		#Este es el indice 
		self.indice = i
		#puntero
		self.siguiente = None

	def getTexto(self):#metodo con el cual obtendremos la informacion
		return self.texto
