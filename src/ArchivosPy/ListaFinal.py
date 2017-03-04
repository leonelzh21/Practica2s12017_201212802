from ListaEnlazada import Nodo
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
			elif temp == self.fin and temp.getTexto() != elemntobuscado:
				print("No se encontro el elemento")
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


listanueva = Lista()
@app.route('/insertarenLista',methods = ['POST'])
def insertarenLista():
	elemento = str(request.form['dato'])
	listanueva.insertarFinal(str(elemento))
	listanueva.imprimitLista()
	return "si"

if __name__ ==  "__main__":
	app.run(debug = True,  host = '0.0.0.0')