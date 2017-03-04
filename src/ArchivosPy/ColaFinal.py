from ListaEnlazada import Nodo

class Cola(object):
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.indice = 0


	def queue(self, numero):
		nuevo = Nodo(numero,self.indice)
		self.indice = self.indice + 1
		if self.inicio == None:
			self.inicio = nuevo
			self.fin = nuevo
		else:
			self.fin.siguiente = nuevo
			self.fin = nuevo

	#Metodo que saca elementos de la cola
	def dqueue(self):
		numero = self.inicio.getTexto()
		inicio = self.inicio.siguiente
		if self.inicio == None:
			self.fin = None

		return str(numero) 

	def imprimitCola(self):
		if self.inicio == None:
			print("La Cola esta Vacia")
		else: 
			val = True
			temp = self.inicio
			while val:
				print(temp.getTexto())
				if temp == self.fin:
					val = False
				else:
					temp = temp.siguiente
					