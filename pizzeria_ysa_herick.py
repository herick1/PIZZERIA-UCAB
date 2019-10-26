#Pizzeria UCAB
#Autores Ysabel Ardila y Herick Navarro

# Importando al modulo ingrediente para que el mismo nos devuelva a los ingredientes iniciales en una lista
# Los objetos en esta lista tienen como atributos nombre, acronimo , y precio
import ingrediente 
listaDeIngredientes = ingrediente.iniciar()

#Variables globales iniciales
#Tamaño es un diccionario que tiene una lista adentro, para así obtener el nombre y su valor
tamaño = {"p" : ["Personal",280] , "m": ["Mediana",430], "g" : ["Grande",580]} 

# Cabecera con el logo de inicio 
#Funcion encargada de mostrar la cabecera del inicio
def Cabecera():
	print("\n \n")
	print("#"*58)
	print("#\t \t PIZZERIA UCAB \t \t \t \t #")
	print("#"*58)

#Funcion adicional encargada de cambiarle el precio a una pizza de un tamaño especifico
#Debido a que estamos haciendo un casting es necesario utilizar un try catch , previniendo la existencia de alguna excepcion
def CambiarPrecioPizza():
	size=input("Tamaños: Grande( g ) Mediana ( m ) Personal ( p )  Salir ( s ): ")
	while size is not 'g' and size is not 'm' and  size is not 'p' and  size is not 's' :
		print("Debe seleccionar una opcion correcta \n")
		size=input("Tamaños: Grande( g ) Mediana ( m ) Personal ( p )  Salir ( s ): ")
	if size == "s": print("no se realizara ningun cambio de precio \n")
	else: 
		try:
			precio = int(input("Introduzca un nuevo precio : "))
			tamaño.get(size)[1] = precio
		except ValueError:
			print('No se pudo cambiar el precio ya que no era un numero valido \n')

#Funcion adicional encargada de agregar un ingrediente adicional en las listas para ser utilizada despues
#Debido a que estamos haciendo un casting de un entero , utilizamos un try catch previniendo la existencia de alguna excepcion
def AgregarIngrediente():
	try:
		nuevoIngrediente= ingrediente.ingrediente()
		nuevoIngrediente.nombre = input("Agrege el nombre del elemento : ")
		nuevoIngrediente.acronimo = input("Agrege  una abreviacion de dos letras para el elemento : ")
		nuevoIngrediente.precio = int(input("Agrege el precio del nuevo elemento : \n"))
		listaDeIngredientes.append(nuevoIngrediente)	
	except ValueError:
		print('Error: No se pudo agregar el ingrediente\n')


full_name = lambda ingrediente: f'{ingrediente.nombre}\t({ingrediente.acronimo})'
#Funcion adicional encargada de cambiarle el precio a un ingrediente especifico por pantalla
#Al cambiarlo y hacer un casting de un entero se hace un try catch previniendo la existencia de alguna excepcion
def ActualizarPrecioIngrediente():
	print("\nIngredientes: ")
	#Imprime los ingredientes
	for ingredient in listaDeIngredientes:
		print(full_name(ingredient))
	#Busca el ingrediente que se ingresa por pantalla o en el caso de que introduzca "s" termina el ciclo
	while ingredient is not "":
		ingredient = input("Indique el Ingrediente (\"s\" para terminar):")
		if ingredient == "s":
			print(" Opcion de salida de este menu \n")
			break
		nuevoPrecio=0
		for ingrediente in listaDeIngredientes:
			if ingredient==ingrediente.acronimo: 
				try:
					ingrediente.precio = int(input("Introduzca un nuevo precio : "))
					nuevoPrecio=1
				except ValueError:
					print('No se pudo cambiar el precio ya que no era un numero valido')
				break
		if not nuevoPrecio: print("\t\t\tIngrediente Inválido \n")


#Menu de funciones adicionales
def adicionales():
	keep = ""
	while keep is not "0":
		print("1 - Cambiar precio de las pizzas ")	
		print("2 - Agregar ingrediente adicional a la lista")
		print("3 - Actualizar precio de algun ingrediente")
		print("0 - Ciclo Normal")
		keep= input()
		if keep == "0" : break		
		elif keep == "1" : CambiarPrecioPizza()
		elif keep == "2" : AgregarIngrediente()
		elif keep == "3" : ActualizarPrecioIngrediente()
		else: print("Opción Inválida")

#Funcion encargada de devolver el tamaño correcto de una pizza por pantalla
#Si no se selecciona la opcion correcta, seguirá preguntando hasta que la opción sea válida
#Devuelve el tamaño y el precio
def tamañoMenu():
	size=input("Tamaños: Grande( g ) Mediana ( m ) Personal ( p ): ")
	#Validando CASO 1----------------- (Que ingrese valores correctos en tamano)
	while size is not 'g' and size is not 'm' and  size is not 'p':
		print("Debe seleccionar el Tamaño correcto")
		size=input("Tamaños: Grande( g ) Mediana ( m ) Personal ( p ): ")

	priceaux = tamaño.get(size)[1]
	size = tamaño.get(size)[0]
	print("Tamano seleccionado: ",size)
	return size, priceaux

#Menu de los ingredientes para ser seleccionados
#Recibe el precio auxliar para ser llenado, y el tamaño de la pizza
#Devuelve el precio auxliar  
def IngredientesMenu(priceaux, size):
	ingredient="s"
	ing_acum=''
	# Mostrar ingredientes por pantalla
	print("\nIngredientes: ")
	for ingredient in listaDeIngredientes:
		print(full_name(ingredient))
	#Validando CASO 2----------------------------------------------------------
	#se calcula la suma de los ingredientes al precio , y se hace un string con los ingredientes selecionados
	while ingredient is not "":
		ingredient = input("Indique el Ingrediente (Enter para terminar ):")
		if ingredient == "":
			break
		#Busca el indice del elemento para ver si existe en la lista
		# si es así, se suma el precio
		index = 0
		for ingrediente in listaDeIngredientes:
			if ingredient==ingrediente.acronimo: 
				priceaux = priceaux + ingrediente.precio
				ing_acum += ' ' + ingrediente.nombre
				index=1
				break
		if not index: print("\t\t\tIngrediente Inválido")

	if ing_acum == "":
		print("Usted seleccionó una pizza",size,"Margarita")
	else:
		print("Usted seleccionó una pizza",size, "con:",ing_acum)
	return priceaux

#Funcion que ejecuta el programa principal
def menu():
	
	KeepSalida = 'S'
	while(KeepSalida == 'S'):
		Cabecera()
		adicionales()
		keep= 'S'
		cont=1
		price=0 	
		while(keep == 'S'):
			priceaux=0
			print("-"*20, "Menu","-"*32)
			print("Pizza número", cont)
			print("Opciones: ")
			size, priceaux = tamañoMenu()
			priceaux = IngredientesMenu(priceaux, size)
			print("\nSubtotal a pagar por una pizza ", size, ": ", priceaux)
			print("#"*58)
			cont= cont+1
			#Validando CASO 3--------------------------------------------------------
			price= price + priceaux
			keep = input("\nDesea otra pizza? [S/N]").upper()
			while keep != 'S'  and keep !='N':
				print("Debe seleccionar una opcion correcta")
				keep = input("\nDesea otra pizza? [S/N] ").upper()

		print("El pedido tiene un total de ",cont-1, "pizza(s) por un monto de ", price)
		print("Gracias por su compra, regrese pronto\n\n")
		KeepSalida = input("\nDesea seguir en el programa? [S/N]").upper()
		while KeepSalida != 'S'  and KeepSalida !='N':
			print("Debe seleccionar una opcion valida")
			KeepSalida = input("\nDesea seguir en el programa?  [S/N] ").upper()
	print("Gracias por su compra! Hasta luego! \n\n")

menu();