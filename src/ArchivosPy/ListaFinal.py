from ListaEnlazada import Nodo
from ColaFinal import Cola
from PilaFinal import Pila
from graphviz import Digraph
from flask import Flask,request,Response

app = Flask('Practica2')
class Lista(object):
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.ind = 0

	#Metodo que insertar al final de la lista
	def insertarFinal(self,text):
		nuevo = Nodo(text,self.ind)
		self.ind = self.ind + 1
		if self.inicio == None:
			self.inicio = nuevo
			self.fin = nuevo 
		else:
			self.fin.siguiente = nuevo
			self.fin = nuevo

	#Metodo que imprime todos los elementos de la lista
	def imprimitLista(self):
		if self.inicio == None:
			print("Lista Vacia")
		else:
			val = True
			temp = self.inicio
			while(val):
				print(temp.getTexto())
				if temp == self.fin:
					val = False
				else:
					temp = temp.siguiente

	#metodo que busca un elemento determinado en lal ista
	def buscar(self,elemntobuscado):
		temp = self.inicio
		validar = True 
		while (validar):
			if temp.getTexto() == elemntobuscado:
				validar = False
				print("Se econtro el elemento en el indice" + str(temp.indice))
				return "Se econtro el elemento en el indice" + str(temp.indice)
			elif temp == self.fin and temp.getTexto() != elemntobuscado:
				print("No se encontro el elemento")
				return "Nose Encotro el Elemento"
				validar = False
			else:
				temp = temp.siguiente

	#Metodo para elminar de la lista en un indice especifico
	def eleminar(self,index):
		contador = 0
		index2 = int(index)
		temp = self.inicio
		if index2 == 0:
			self.inicio = self.inicio.siguiente
		else:
			while contador < index2-1:
				temp = temp.siguiente
				contador = contador + 1
			temp.siguiente = temp.siguiente.siguiente

	def graphLista(self):
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
			dot.render('Graficas/imgLista.dot', view=False)


#AQUI EMPIEZAN LOS METODOS DE LA LISTA
listanueva = Lista()
@app.route('/insertarenLista',methods = ['POST'])
def insertarenLista():
	elemento = str(request.form['dato'])
	listanueva.insertarFinal(str(elemento))
	listanueva.graphLista()
	listanueva.imprimitLista()
	return "si"

@app.route('/eliminarenLista',methods = ['POST'])
def eliminarenLista():
	elemento = str(request.form['dato'])
	listanueva.eliminar(elemento)
	listanueva.graphLista()
	return "Eliminado"

@app.route('/buscarenLista',methods = ['POST'])
def buscarenLista():
	elemento = str(request.form['dato'])
	encontrado = listanueva.buscar(elemento)
	return encontrado

#AQUI TERMINAN LOS METODOS DE LA LISTA

#AQUI EMPIEZAN LOS METODOS DE LA COLA
colanueva = Cola()
@app.route('/queueCola',methods = ['POST'])
def queueCola():
	elemento = str(request.form['dato'])
	colanueva.queue(elemento)
	colanueva.graphCola()
	return "si"

@app.route('/dqueueCola',methods = ['POST'])
def dqueueCola():
	elemento = str(request.form['dato'])
	extraido = colanueva.dqueue()
	colanueva.graphCola()
	return extraido

#AQUI TERMINA LOS METODOS DE LA COLA

#AQUI EMPIEZAN LOS METODOS DE LA PILA
pilanueva = Pila()
@app.route('/pushPila',methods = ['POST'])
def pushPila():
	elemento = str(request.form['dato'])
	pilanueva.push(elemento)
	pilanueva.graphPila()
	return "si"

@app.route('/popPila',methods = ['POST'])
def popPila():
	elemento = str(request.form['POST'])
	extraido = pilanueva.pop()
	pilanueva.graphPila()
	return extraido



if __name__ ==  "__main__":
	app.run(debug = True,  host = '0.0.0.0')