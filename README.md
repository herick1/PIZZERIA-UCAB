# PIZZERIA-UCAB
proyecto para comenzar a aprender de python
 Objetivo del programa:    Es un programa capaz de atender a una persona en la compra de una pizza 
 
Desarrollo del Programa:  
 
 El programa principal consta de 8 funciones y 2 variables globales para su ejecución correcta, y un módulo ingrediente con una clase y una función. 
 
 
* Modulo ingrediente: En este módulo consta de una clase llamada ingrediente que tiene tres atributos como son el precio, el nombre y el acrónimo del nombre (que es utilizado como clave) o Función iniciar(): encargada de devolver la lista inicial de los ingredientes adicionales. o Clase ingrediente: es una clase para poder crear un objeto de tipo ingrediente con su nombre, acrónimo y precio. 

* Variables Globales:  o Variable “tamaño” allí se aplica el uso de un diccionario con una clave que son los tipos de tamaño (p, m, g), ya que no va hacer cambiable el tamaño, por eso elegimos este uso de los diccionarios, dentro de ella hay una lista con el nombre completo de la clave (Personal, Mediana, Grande) y como segundo parámetro en la lista tenemos el precio, esto lo hicimos así para poder cambiar el precio en una función adicional. o Variable “listaDeIngredientes”: es una lista que tiene los ingredientes adicionales esta es llamada a través de la función iniciar del módulo ingrediente. 

* Función Menú() : Esta es la encargada del ciclo del sistema, en ella se cargan todas las opciones del programa, además es la responsable de controlar el precio de cada pizza y el total de todas las pizzas, además desde esta función se puede salir del programa, esta función no recibe ningún parámetro, y no devuelve ningún parámetro 

* Función Cabecera() : En ella hay una serie de impresiones por pantalla, las cuales  hacen el logo de inicio de la pizzería, esta función no recibe ningún parámetro , y no devuelve ningún parámetro 
 
* Función tamañoMenu(): Se encarga de devolver el tamaño correcto de una pizza ingresada por pantalla, hay un ciclo que si no se selecciona la opción correcta, no te permite continuar hasta que selecciones una opción correcta, esta función no recibe ningún parámetro, pero si devuelve el precio según un tamaño y un String con el nombre del tamaño de la pizza.

* Función IngredientesMenu(priceaux, size): Esta función lo primero que hace es llenar en pantalla los ingredientes adicionales recorriendo la lista de los ingredientes(variables globales), después de eso hay un ciclo donde se ingresa por pantalla un acrónimo, si ese acrónimo existe como parte de un índice en la lista de ingredientes entonces sale del ciclo, si es un enter se sale también del ciclo pero sin ningún ingrediente adicional, sino se muestra un error, en este ciclo se van concatenando los string de los nombres de los ingredientes adicionales que se hallan seleccionado , además de hacer la suma matemática de los precios de esos mismos ingredientes seleccionados, al final se muestra en pantalla los ingredientes seleccionados, esta función devuelve la suma de los precios de los ingredientes seleccionados para esa pizza   

* Funcionalidades Adicionales:  
	* Función adicionales(): Este es un submenú encargado de desviar el flujo normal del sistema para las funcionalidades adicionales en él se le dan 4 opciones al usuario y dependiendo de lo que seleccione si irá a una cierta opción adicional o al flujo normal del sistema, esta función no recibe ningún parámetro, y no devuelve ningún parámetro 

	* Función CambiarPrecioPizza():  esta función es la primera funcionalidad adicional, aquí se cambia el precio a una pizza, para ello se le pide al usuario que ingrese por pantalla una clave de un tamaño de una pizza (p, m, g), si el usuario no ingrese un tamaño correcto se le pide que lo vuelva a ingresar, después de seleccionar una opción correcta, el sistema pide que ingrese un nuevo precio numérico, de no ser un dato numérico el sistema muestra un error, no cambia el precio y se regresa al menú de “adicionales” , de ser un dato correcto cambiamos el segundo parámetro de la lista que está adentro del diccionario que corresponde al precio del tamaño de la pizza 

	* Función AgregarIngrediente(): esta función es la segunda funcionalidad adicional , esta sirve para agregar un ingrediente adicional, para ello se le pide al usuario que ingrese por pantalla un nombre del ingrediente, un acrónimo, y un precio, de no ser un dato numérico el precio el sistema muestra un error, no agrega el ingrediente y se regresa al menú de “adicionales” , pero si es un dato correcto se agrega a lista de ingredientes adicionales 
 	
 	* Función ActualizarPrecioIngrediente ():  esta función es la tercera funcionalidad adicional, en ella se cambia el precio a un ingrediente, para ello se pintan los ingredientes que está en la lista por pantalla, y se le pide al usuario que seleccione uno. El sistema busca si esta existe, si es una opción incorrecta se le muestra un mensaje de error al usuario, en caso de que sea una opción correcta el usuario podrá ingresar un nuevo precio numérico, después de cambiarlo se saldrá de esta funcionalidad cambiando el precio, de no ser numérico el dato, entonces se le mostrara un mensaje de error y no se le cambiara el precio 
 
 