#Clase que contiene los atributos de los ingredientess

class ingrediente:
	precio=0
	acronimo =""
	nombre =""

#Metodo utilizado para devolver la inicializacion de los ingredientes en una lista que tiene 
#dentro objetos de tipo ingredientes 
#esta funcion no recibe ningun parametro
#y devuelve una lista con elementos de tipo ingrediente
def iniciar():
	ingredientesNombre =["Jamón", "Champiñones", "Pimentón", "Doble Queso", "Aceitunas" ,"Pepperoni" ,"Salchichón"]
	ingredientSufivos = ["ja","ch","pi","dq","ac","pp","sa"]
	ingredientesPrecios = [40,35,30,40,58,38.5,62.5]
	i=0
	listaDeIngredientes=[]
	while i<len(ingredientesNombre):
		ingre = ingrediente()
		ingre.precio = ingredientesPrecios[i]
		ingre.nombre=ingredientesNombre[i]
		ingre.acronimo = ingredientSufivos[i]
		listaDeIngredientes.append(ingre)
		i+=1	
	return listaDeIngredientes