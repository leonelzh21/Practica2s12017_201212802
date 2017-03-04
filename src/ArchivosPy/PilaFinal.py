from ListaEnlazada import Nodo
from graphviz import Digraph

class Pila(object):
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.index = 0

	#Metodo que inserta al inicio de la pila cada elemento
	def push(self,numero):
		nuevo = Nodo(numero,self.index)
		self.index = self.index + 1
		if self.inicio == None:
			self.inicio = nuevo
			self.fin = nuevo
		else:
			nuevo.siguiente = self.inicio
			self.inicio = nuevo

	def pop(self):
		num = self.inicio.getTexto()
		self.inicio = self.inicio.siguiente
		if self.inicio == None:
			self.fin = None

		return str(num)

	def imprimiPila(self):
		if self.inicio == None:
			print("ups no hay nada la lista esta vacia")
		else:
			val = True
			temp = self.inicio
			while val:
				print(temp.getTexto())
				if temp == self.fin:
					val = False
				else:
					temp = temp.siguiente

	def graphPila(self):
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
			dot.render('Graficas/imgPila.dot', view=False)