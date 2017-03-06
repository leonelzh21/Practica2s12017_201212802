from NodoMatriz import NodoM
from graphviz import Digraph

class MatrizDispersa(object):
	def __init__(self):
		self.primero = None
		self.fin_dominio = None
		self.fin_abc = None
		self.index = 0

	def vacia(self):
		if self.primero == None:
			return True

	#Metodo que va ingresar los dominios y los nombre a la matriz y los clasificara por letra
	def ingresar(self,nombre,dominio):
		if self.vacia() == True:
			#Aqui creamos el ancla para unir las cabeceras de las letras con los dominios, este seria el nodo primero
			nuevo = NodoM("Raiz","Raiz","Raiz",self.index)
			self.index = self.index + 1
			self.primero = nuevo
			self.fin_dominio = nuevo
			self.fin_abc = nuevo

		self.crear_dominio(dominio)
		self.crear_abc(nombre[0])
		temp1 = self.dominio(dominio)
		temp2 = self.abc(nombre[0])
		anterior = ""
		siguiente = ""
		if(temp1.siguiente != None):#Aqui obtenemos el dominido del siguieente nodo si es que existe 
			siguiente = temp1.siguiente.dominio

		if(temp1.anterior != None):#Aqui obtenemo el dominio del  anterior nodo si es que existe
			anterior = temp1.anterior.dominio

		correo = nombre + dominio #Concatenamos los parametros para formar el correo que se esta creando
		
		if(temp1.abajo == None and temp2.siguiente == None):#Esta revision solo se hace cuando se crear el primero elemento de toda la matiz y solo existe el nodo primero que seria el ancla y las primero dos cabeceras
			nuevo = NodoM(correo,nombre[0],dominio,self.index)# se crea el nodo que contendra la informancion
			self.index = self.index + 1
			print("Se ingreso el correo " + correo)
			# aqui se direccionan los punteros del las cabeceras de los dominios y de las letras
			temp1.abajo = nuevo 
			nuevo.arriba = nuevo
			temp2.siguiente = nuevo
			nuevo.anterior = nuevo
		else:
			temp_dominio = temp1
			nuevo = NodoM(correo,nombre[0],dominio,self.index)
			self.index = self.index + 1
			print("Se ingreso el correo " + correo)
			validar = True
			if self.posicion(dominio,nombre[0]) != True:#Aqui revisamos si el nodo que vamos a insertar sera en el medio
				while temp_dominio != None:
					if temp_dominio.abajo != None:
						if nuevo.letra < temp_dominio.abajo.letra:#Aqui revisamos el orden de las letras para sabaer si lo insertamos en medio de dos letras
							nuevo.arriba = temp_dominio
							nuevo.abajo = temp_dominio.abajo
							temp_dominio.abajo.arriba = nuevo
							temp_dominio.abajo = nuevo
							temp_dominio = None
						else:
							temp_dominio = temp_dominio.abajo
					elif temp_dominio.abajo == None:# Esta es para poner el nodo hasta la ultima letra que es donde le corresponde
						nuevo.arriba = temp_dominio
						temp_dominio.abajo = nuevo
						temp_dominio = None
					else:
						temp_dominio = temp_dominio.abajo
				self.nodo_medio(temp2, nuevo , anterior , siguiente , temp1.anterior, temp1.siguiente)
			else:# Aqui ingresamos el usuario a un mismo domino y una letra ya creados y lo ponemos en la profundidad
				temp3 = self.nodo(dominio,nombre[0])
				if temp3.profundidad == None:
					temp3.profundidad = nuevo
				else:
					while temp3 != None:
						if temp3.profundidad == None:
							temp3.profundidad = nuevo
						else:
							temp3 = temp3.siguiente
			return "Usuario Ingresado" 

	# Este metodo crea las cabeceras de los dominios si lo que se ingresa es un nuevo dominio de lo contrario no crea nada
	def crear_dominio(self,dominio):
		# Aqui creamos la primera cabecera para los dominios
		if(self.primero.siguiente == None):
			nuevo = NodoM("Raiz","Raiz",dominio,self.index)
			self.index = self.index + 1
			nuevo.anterior = self.fin_dominio
			self.fin_dominio.siguiente = nuevo
			self.fin_dominio = nuevo
		else:
			temp = self.primero
			validar = False
			while temp != None:# aqui vamos a recorrer las cabeceras de los dominios para saber si el doiminio ingresado ya existe
			    if temp.dominio == dominio:
			    	validar = True
			    	temp = None
			    else:
			    	temp = temp.siguiente
			if validar != True:# aqui creamos la una nueva cabecera para el nuevo dominio ya que no fue creado previamente
				nuevo = NodoM("Raiz", "Raiz", dominio,self.index)
				self.index = self.index + 1
				nuevo.anterior = self.fin_dominio
				self.fin_dominio.siguiente = nuevo
				self.fin_dominio = nuevo

    # Ese metodo crea las cabeceras de las letras si lo que se ingresa es una nueva letra de lo contrario no crea nada
	def crear_abc(self,letra):
		if self.primero.abajo == None:# aqui creamos la primera cabecera de las letras
			nuevo = NodoM("Raiz", letra, "Raiz",self.index)
			self.index = self.index + 1
			nuevo.arriba = self.fin_abc
			self.fin_abc.abajo = nuevo
			self.fin_abc = nuevo
		else:
			temp = self.primero
			validar = False
			while temp != None:# aqui recorremos las cabeceras de las  letras para sber si la letra ingresada y existe
				if temp.letra == letra:
					validar = True
					temp = None
				else:
					temp = temp.abajo
			if validar != True :# aqui creamos la nueva cabecera para la nueva letra ya que no fue creada perviamente
				nuevo = NodoM("Raiz", letra, "Raiz",self.index)
				self.index = self.index + 1
				temp = self.primero
				while temp != None:
					if temp.abajo != None:
						if letra < temp.abajo.letra: #aqui revisamos en que que letra es para ordenar alfabeticamente las cabeceras
							temp2 = temp.abajo
							nuevo.arriba = temp
							temp.abajo = nuevo
							nuevo.abajo = temp2
							temp2.arriba = nuevo
							temp = None
						else:
							temp = temp.abajo
					elif temp.abajo == None: # aqui creamos la cabecera de la letra hasta al final ya que ahi corresponde alfabeticamente
						nuevo.arriba = self.fin_abc
						self.fin_abc.abajo = nuevo
						self.fin_abc = nuevo
						temp = None
					else:
						temp = temp.abajo

	def dominio(self,dominio):# Metodo que devuelve la cabecera del dominido al que pertenece el nuevo usuario que ingresamos
		temp = self.primero
		validar = True
		Nodo = None
		while temp != None and validar != False:
			if temp.dominio == dominio:
				validar = False
				Nodo = temp
			else:
				temp = temp.siguiente
				validar = True
		return Nodo


	def abc(self,letra):# Metodo que devuelve la cabecera de la letra a la que pertence el nuevo usuario que ingresamos
		temp = self.primero
		validar = True
		Nodo = None
		while temp != None and validar != False:
			if(temp.letra == letra):
				validar = False
				Nodo = temp
			else:
				temp = temp.abajo
				validar = True
		return Nodo


	def posicion(self,dominio,letra): # Este metodo verifica si la posision en la que debe ir el nodo del nuevo usuario es en el medio o no
		temp = self.primero.siguiente
		validar = False
		while temp != None:
			if temp.dominio == dominio:
				temp2 = temp
				while temp2 != None:
					if temp2.letra == letra:
						temp2 = None
						validar = True
					else:
						temp2 = temp2.abajo
				temp = None
			else:
				temp = temp.siguiente
		return validar


	def nodo(self,dominio,letra):# metodo que que busca si ya existe un usuario previamente creado en la letra correspondiente y lo retorna para agreagarlo a esa lista de usuario del dominio y de la letra
		temp = self.primero
		Nodo = None
		while temp != None:
			if temp.dominio == dominio:
				temp2 = temp
				while temp2 != None:
					if temp2.letra == letra:
						Nodo = temp2
						return Nodo
						temp2 = None
					else:
						temp2= temp2.abajo
				temp = None
			else:
				temp = temp.siguiente


	def nodo_medio(self,temp_abc,nuevo,anterior,siguiente,auxA,auxS):# Meotodo que agreaga en el medio el nuevo usuario correspondiente 
		temp2 = temp_abc
		validar = False
		while temp2!=None:
			if(temp2.dominio == anterior and temp2.siguiente == None):
				temp2.siguiente = nuevo
				nuevo.anterior = temp2
				print("Nodo_medio "+nuevo.correo)
				temp2 = None
				validar = True
			elif temp2.dominio == anterior and temp2.siguiente != None:
				nuevo.siguiente = temp2.siguiente
				temp2.siguiente.anterior = nuevo
				nuevo.anterior = temp2
				temp2.siguiente = nuevo
				print("Nodo_medio "+nuevo.correo)
				temp2 = None
				validar = True
			elif temp2.dominio == siguiente:
				nuevo.siguiente = temp2
				temp2.anterior.aiguiente = nuevo
				nuevo.anterior = temp2.anterior
				temp2.anterior = nuevo
				print("Nodo_medio "+nuevo.correo)
				temp2 = None
				validar = True
			else:
				temp2 = temp2.siguiente

		if(validar != True):
			anterior = ""
			siguiente = ""
			if(auxA.anterior != None):
				anterior = auxA.anterior.getDominio()
			if(auxS.siguiente != None):
				siguiente = auxS.siguiente.getDominio()

			if(auxA != None or auxS ==None):
				self.nodo_medio(temp_abc, nuevo, anterior, siguiente, auxA.anterior, None);
			elif(auxA == None or auxS != None):
				self.nodo_medio(temp_abc, nuevo, anterior, siguiente, None, auxS.siguiente);
			elif(auxS.siguiente != None and auxA.anterior != None):
				self.nodo_medio(temp_abc, nuevo, anterior, siguiente, auxA.anterior, auxS.siguiente);
			else:
				self.nodo_medio(temp_abc, nuevo, anterior, siguiente, None, None);
	
	def imprimir(self):
		print(self.primero.correo)

	def imprimir_dominios(self):
		temp = self.primero.siguiente
		while(temp!=None):
			temp2 = temp
			while(temp2 != None):
				print(temp2.dominio+"  "+temp2.correo)
				temp2 = temp2.abajo
			temp = temp.siguiente

	def imprimir_abecedario(self):
		temp = self.primero.abajo
		while(temp!=None):
			temp2= temp
			while(temp2 != None):
				print(temp2.letra+"  "+temp2.correo)
				temp2 = temp2.siguiente
			temp=temp.abajo


	def graficar(self):
		temp = self.primero
		dot = Digraph(comment='GraficaListaSimple')
		dot  #doctest: +ELLIPSIS      
		while(temp != None):
			temp_d = temp
			while(temp_d != None):
				if(temp_d.abajo != None and temp_d == temp):
					dot.node(str(temp_d.indice),str(temp_d.letra))
					dot.node(str(temp_d.abajo.indice),str(temp_d.abajo.letra))
					dot.edge(str(temp_d.indice),str(temp.abajo.indice),constraint='true')     
					temp_d = temp_d.abajo
				elif temp_d.abajo != None and temp_d != temp:
					dot.node(str(temp_d.indice),str(temp_d.correo))
					dot.node(str(temp_d.abajo.indice),str(temp_d.abajo.correo))
					dot.edge(str(temp_d.indice),str(temp.abajo.indice),constraint='true')     
					temp_d = temp_d.abajo
				else:
					temp_d = temp_d.abajo
			temp = temp.siguiente

		temp2 = self.primero
		while(temp2 != None):
			temp_a = temp2
			while(temp_a != None):
				if(temp_a.siguiente != None):
					dot.node(str(temp_a.dominio),str(temp_a.dominio))
					dot.node(str(temp_a.siguiente.dominio),str(temp_a.siguiente.correo))
					dot.edge(str(temp_a.indice),str(temp_a.siguiente.indice),constraint='true')     
					temp_a = temp_a.siguiente
				else:
					temp_a = temp_a.siguiente
			temp2 = temp2.abajo

		temp3 = self.primero

		while(temp3 != None):
			temp4 = temp3
			while(temp4 != None):
				temp_p = temp4
				while(temp_p != None):
					if(temp_p.profundidad != None):
						dot.node(str(temp_p.dominio),temp_p.correo)
						dot.node(str(temp_p.profundidad.dominio),temp_p.profundidad.correo)
						dot.edge(str(temp_p.indice),str(temp_p.profundidad.indice),constraint='true')
						temp_p = temp_p.profundidad
					else:
						temp_p = temp_p.siguiente
				temp4 = temp4.siguiente
			temp3 = temp3.abajo

		print(dot.source)
		dot.render('Graficas/imgMatriz.dot', view=False)




"""matriznueva = MatrizDispersa()
matriznueva.ingresar("leonel","@gmail.com")
matriznueva.ingresar("andrea","@gmail.com")
matriznueva.ingresar("alejandro","@yahoo.com")
matriznueva.ingresar("emma","@outlook.com")
matriznueva.ingresar("mynor","@yahoo.com")
matriznueva.imprimir()
matriznueva.imprimir_dominios()
matriznueva.imprimir_abecedario()
matriznueva.graficar()"""
