from ListaEnlazada import Nodo
from graphviz import Digraph

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
		self.inicio = self.inicio.siguiente
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

	def graphCola(self):
		dot = Digraph(comment='GraficaListaSimple')
		dot  #doctest: +ELLIPSIS
		temp = self.inicio
		if self.inicio == None:
			print("la lista esta vacia")
		else:
			while temp.siguiente != None:
				dot.node(str(temp.indice), temp.getTexto())
				dot.node(str(temp.siguiente.indice), temp.siguiente.getTexto())
				dot.edge(str(temp.indice), str(temp.siguiente.indice), constraint='false')
				temp = temp.siguiente
			print(dot.source)
			dot.render('Graficas/imgCola.dot', view=False)
