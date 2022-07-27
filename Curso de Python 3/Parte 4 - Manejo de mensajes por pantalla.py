# MANEJO DE MENSAJES POR PANTALLA
# - La primera meta es aprender a manejar la entrada y salida de información a través de la pantalla.
# - Mostrar información por pantalla y leer información de los usuarios son operaciones necesarias para 
# conseguir una interactividad alta con las aplicaciones que desarrolles por parte de los usuarios de éstas.
# - La primera fase aprenderás a mostrar información a los usuarios y 
# en la segunda aprenderás a leer información proveniente de los usuarios.

# Conceptos teóricos:\
# - Se explicaran 2 comandos muy útiles en la programación en Python: print e input

# print:
# - Te va a permitir mostrar información al usuario de la aplicación
# - El comando se puede utilizar con varias cadenas a mostrar de una sola vez, separadas por comas. De esta forma simplifica el no tener que escribir 
# una sentencia por cada mensaje que queramos mostrar por pantalla de forma secuencial. Por defecto, se introduce siempre un carácter de separación 
# entre las diferentes cadenas: el espacio en blanco.

# - Es posible utilizar los siguientes parámetros con el comando print: 
#   - end: permite añadir una cadena de texto como elemento final del conjunto de cadenas de texto que se han enviado para mostrar por pantalla.  
#   - sep: permite añadir una cadena de texto al final de cada cadena enviada para mostrar por pantalla y sustituir el espacio en blanco que se introduce 
#   por defecto entre las diferentes cadenas de texto que son enviadas para mostrarse por pantalla. 

# Ejemplo print
print('Hello, World!')

#--------
# input
# - Te va a permitir leer información introducida por los usuarios de la aplicación mediante el teclado. 
# - El texto introducido por los usuarios es retornado por el comando como una cadena de texto simple. 
# - En el caso de necesitar un tipo de dato diferente tendrás que transformar la cadena de texto al tipo de dato que necesites. 
# Es necesario que el usuario de la aplicación presione la tecla Enter para que se realice la lectura del texto introducido. 

# Ejemplo input (Se va a ejecutar mejor este ejemplo en su IDE, en mi caso VSC preferiblemente que en Jupyter)
nombre = input('Cúal es tu nombre? ')
print('Tu nombres es',nombre)
#Esto lo explico mejor más adelante

#--------
# Variables: 
# - Las variables son datos que necesitas almacenar y utilizar en los programas y que residen en la memoria del ordenador. 
# - Tienen las siguientes características: 
#   - Nombre: identificador dentro del código fuente que utilizamos para usarlas.  
#   - Tipo: tipo de dato que almacena la variable.  
#   - Valor: valor que almacenan. Al declarar una variable tienes que indicarle un valor inicial, que puede verse modificado 
#   a medida que se va ejecutando el programa y según vayas necesitando, de ahí que se llamen variables.

# - En Python las variables se definen utilizando las letras de la A a la Z, tanto en mayúsculas como en minúsculas, los números del 0 al 9 
# (excepto en el primer carácter del nombre) y utilizando el carácter “_”. 
# - El lenguaje Python tiene palabras reservadas que no pueden ser utilizadas como nombres de variables.(Las voy a dejar para lo último)

# Nombre de las variables.
# - Las variables no pueden comenzar con un número.  
# - Las variables no pueden contener símbolos especiales.
# - Las variables no pueden contener espacios
# - Para simular un espacio, es recomendable usar un subrayado bajo(notacion snake_case), ejemplo:
mi_primer_variable_en_python = 'Hello, World!'

# Hay otros tipos de notación de variables. Les voy a explicar
# snake_case: es el ejemplo anterior. La ideal para usar en Python a mi gusto personal me gusta la camelCase.
# PascualCase: La primer letra en mayuscular Ejem: PrimerVariable
# camelCase: La primera en minuscula y la segunda en mayuscular Ejem: primerVariable NOTA la usan mucho en lenguaje Swift 
# skewer-case: toda en minuscula y las palabras separadas por un guión Ejem: primer-variable.

# - En Python no se establece el tipo de dato a la hora de declarar una variable, realmente no existe una declaración propiamente 
# dicha como existe en otros lenguajes, simplemente escribes el nombre que quieres que tenga y le asignas el valor correspondiente.

# Reglas de la variables\
# 1. Legible: nombre de la variable es relevante según su contenido
# 2. Unidad: no existen espacios (puedes incorporar guiones bajos)
# 3. Hispanismos: omitir signos específicos del idioma español, como tildes o la letra ñ
# 4. Números: los nombres de las variables no deben empezar por números (aunque pueden contenerlos al final)
# 5. Signos/símbolos:nosedebenincluir:"',<>/?|\()!@# $%^&*~-+
# 6. Palabras clave: no utilizamos palabras reservadas por Python

#------
# Fase 1: Mostrar información por la pantalla
# - El aprendizaje del uso del comando print mediante una serie de ejercicios que te permitirán mostrar información por pantalla a los usuarios.
# Ejemplo 
print('Hello, World!')
print('Mis primeras líneas de código en Python')

# - En el siguiente ejercicio seguímos con el comando print pero ahora vamos a usar el parámetro "sep"
print(1,2,3,4,5) #En este primer caso vamos a ver que no se imprime la coma después de cada número.
print(1,2,3,4,5, sep=',') #Ahora con este ejemplo vemos que se le agregó la coma después de cada número.

# En el siguiente ejercicio vamos a usar el parámetro "end"
print(1,2,3,4,5) #En este primer caso vamos a ver que no se imprime el guión después del último número.
print(1,2,3,4,5, end=('-')) #Ya aca observamos que sale el guión al final del último número.

# Se puede combinar los anteriores parámetros.
print(10, 20, 30, 40, 50) #Sin usar ni un parámetro
print(10, 20, 30, 40, 50, sep=('-'), end=('...')) #En este ejemplo lo que hicimos fue 1. sep con un guión y end con puntos suspensivos.

#-----
# Fase 2: Leer información en pantalla
# - El aprendizaje del comando input mediante una serie de ejercicios que te permitirán leer la información que introducen los usuarios de la aplicación.
# - Para el siguiente ejemplo vamos a usar el nombre de una variable la cual le pusimos nombre. Pero comó lo hacemo? Bueno va por partes y usen su IDE o interprete de códigos favorito.
# 1. Crear una variable para así guardar la información que el usuario nos va dar atraves de input.
nombre = input('Cúal es tu nombre? ')
# 2. Ya como usuario no dio su nombre vamos a mostrarselo con una frase (la idea es usar la información administrada, en ocasiones no hay necesidad de mostrarsela al usuario, solamente 
# almacenarla para procesos internos en el caso se la vamos a mostrar. Para esto vamos a usar la función print y con una frase. Si no entiendes mucho no te preocupes que pronto vas a ir entendiendo)
print('Tu nombres es',nombre)
#Bueno que hicimos print nos funciona para mostrar la información al usuario, después se imprime todo lo que esta  en el parentesis la primera parte es una frase 'Tu nombre es' se separa de una coma \
# y posteior ponemos la variable en este caso se llama nombre el resultado.


#Aunque no lo creas ya eres capaz de realizar tus primeras líneas de código, las cuales puedes imprimir por print, ingresarles datos a traves de input y por último y lo más importante
#ya sabes como crear una varibles y sus caracteristicas las cuales vas a poner en practica siempre.


#------
#PALABRAS RESERVADAS DE PYTHON:
# and: representación lógica de Y.  
# as: tiene dos funciones, la primera de ellas es para asignar una excepción a un determinado objeto y la segunda es para renombrar un módulo importado al código.  
# assert: utilizada en la depuración de código para lanzar errores si se cumplen ciertas condiciones.  
# break: sirve para finalizar un bucle.  
# class: utilizada para definir una clase.  
# continue: suspende la iteración de un bucle y salta a la siguiente iteración de éste.  
# def: utilizada para definir funciones.  
# del: tiene dos funciones, la primera de ellas es eliminar la referencia de un objeto concreto y la segunda es para eliminar elementos de una lista.  
# elif: definición de una bifurcación alternativa con condición.  
# else: definición del camino sin condición en una bifurcación.  
# except: utilizada para capturar excepciones ocurridas durante la ejecución del código fuente.  
# False: utilizada para representar el valor booleano 0 / falso.  
# finally: utilizada para definir un bloque de código fuente que se ejecutará al final del procesamiento de las excepciones.  
# for: utilizada para definir bucles for.  
# from: utilizada para importar elementos de módulos externos a nuestro código.  
# global: utilizada para modificar objetos en un ámbito inferior, creando un objeto nuevo y sin alterar el valor del objeto del ámbito superior.  
# if: definición de una bifurcación con condición.  
# import: importa un módulo externo a nuestro código. Se puede utilizar junto a from, pero en ese caso importará elementos en vez del módulo completo.  
# in: determina la existencia de un elemento en una lista, tupla, diccionario o cualquier objeto iterable.  
# is: determina si dos objetos son iguales. No es lo mismo dos objetos con los mismos valores que dos objetos iguales.  
# lambda: utilizada para definir funciones lambda.  None: utilizada para representar la ausencia de valor.  
# nonlocal: permite modificar el valor de un objeto definido en un ámbito anterior.  
# not: representación lógica de NO.  
# or: representación lógica de O.  
# pass: únicamente tiene funciones estéticas para rellenar huecos en el código fuente.  
# print: utilizada para imprimir por pantalla una cadena de texto.  raise: utilizada para lanzar excepciones.  
# return: utilizada para devolver un elemento al finalizar la ejecución de una función.  
# True: utilizada para representar el valor booleano 1 / verdadero.  
# try: utilizada para capturar excepciones ocurridas durante la ejecución del código fuente.  
# while: utilizada para definir bucles while.  
# with: utilizada para encapsular la ejecución de un bloque de código fuente.  
# yield: utilizada para devolver más de un elemento al finalizar la ejecución de una función.