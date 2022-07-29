# Utilización de tipo de datos básicos

# - En este tópico vamos a conocer y usar lo diferentes tipos de datos que tenemos.
# - En la primera aprenderás a utilizar los números y las diferentes operaciones aritméticas
# - La segunda aprenderás a utilizar de forma básica las cadenas de texto
# - La tercera aprenderás a utilizas diferentes colecciones de datos 
# - La cuarta aprenderás los tipos de datos booleanos y las diferentes operaciones lógicas
# - La quinta aprenderás a utilizar de forma avanzada las cadenas de texto.

#------
# CONCEPTOS TEORICOS:

# Tipos de datos:
# - La información no es otra cosa que una secuencia de ceros y unos que se estructuran en bloques para facilitar el manejo de ésta.
# - Toda la información que existe se encuentra tipificada por el tipo de información que es (tipo de dato). No es lo mismo una cadena 
# de texto que un número entero, o decimal.
# - Las variables en Python pueden ser de los siguientes tipos de datos:
#   ENTEROS: Número sin decimales, tanto positivo como negativo, incluyendo el 0.
#   REAL: Número con decimales, tanto positivo como negativo, incluyendo el 0.
#   COMPLEJO: Número con parte imaginaria.
#   CADENAS DE TEXTO: Texto.
#   BOOLEANOS: Pueden tener dos valores: True o False.
#   CONJUNTOS: Colección de elementos no ordenados y no repetidos.
#   LISTAS: Vector de elementos que pueden ser de diferentes tipos de datos.
#   TUPLAS: Lista inmutable de elementos.
#   DICCIONARIOS: Lista de elementos que contienen claves y valores.
# - Las variables no tienen un tipo concreto en Python, puedes utilizar una variable para almacenar un número en una parte de tu 
# programa y posteriormente puedes utilizarla para almacenar una lista de elementos.

#-----
# OPERADORES:
# - Hay una serie de operadores que también existen en los diferentes lenguajes de programación. 
# Los operadores se agrupan según la función que realizan: 
#   - Operadores de asignación.  
#   - Operadores aritméticos.  
#   - Operadores relacionales.  
#   - Operadores lógicos.

# Operadores de asignación:
# - El operador de asignación ‘=’ sirve para asignar un valor a una variable, lo que esté en la parte derecha del operador será asignado (almacenado) 
# en la variable de la parte izquierda.
# Ejemplo:
# 1. asignación de valor:
manzana = 20
# 2. asignación de cadena de texto
mascota = 'perro'

# Operadores aritméticos:
# - Son aquellos operadores que nos van a permitir realizar operaciones aritméticas con los datos.
# - Una buena práctica a la hora de utilizar operadores aritméticos es la utilización de paréntesis para establecer el orden concreto de resolución de 
# las operaciones, ya que cada lenguaje de programación establece la resolución de forma diferente y puedes encontrar resultados erróneos.
# Ejemplo:
multiplicacion = 9*6
suma = 10+10
costos = (3*1000)
# Los datos de esas operaciones son almacenados en esas variables

# Operadores relacionales:
# - Son aquellos que van a permitirte realizar comparaciones entre dos elementos. Son los siguientes:
# < menor que
# > mayor que
# <= menor o igual que 
# >= mayor o igual que 
# == igual que 
# != distinto que 

# - El resultado de una operación relacional puede ser únicamente dos valores: 
#   - true: la comparación se cumple.  
#   - false: la comparación no se cumple.
# Ejemplos 
7>8
90==90
#Si ejecutamos estos ejemplos de a uno por uno nos daría en el primero false y en el segundo True 

# Operadores lógicos:
# - Los operadores lógicos permiten combinar las operaciones relacionales del punto anterior o valores booleanos independientes para obtener un único resultado. 
# - Los operadores lógicos que puedes utilizar son los siguientes: 
#   - AND(Conjuntivo): operador lógico que realiza la operación lógica ‘Y’ entre dos elementos. El resultado será true si ambos elementos son true, en caso contrario será false. 
#       # A continuación escribiré los ejemplos principales en una tabla comparativa entre posibles situaciones lógicas AND. 
#           FALSO ​​AND​​ FALSO = ​​FALSO 
#           FALSO ​​AND ​​VERDADERO = ​​FALSO 
#           VERDADERO ​AND ​​FALSO = ​​FALSO 
#           VERDADERO ​AND ​​VERDADERO = ​​VERDADERO
#   - OR(Disyuntivo): operador lógico que realiza la operación lógica ‘O’ entre dos elementos. El resultado será true si uno de los dos elementos es true, en caso contrario será false.
#       # A continuación escribiré los ejemplos principales en una tabla comparativa entre posibles situaciones lógicas OR. 
#           FALSO ​​OR ​​FALSO = ​​FALSO 
#           FALSO ​​OR ​​VERDADERO = ​​VERDADERO 
#           VERDADERO ​OR ​​FALSO = ​​VERDADERO 
#           VERDADERO​ OR ​​VERDADERO = ​​VERDADERO  
#   - NOT: operador lógico que realiza la operación lógica ‘NO’. El resultado será true si el elemento es false, y será false si es true.  
# - Los operadores lógicos pueden utilizarse en expresiones combinadas, para ello, tal y como te hemos explicado en los operadores aritméticos te aconsejamos que utilices 
# paréntesis para separar las diferentes expresiones.
# Ejemplos
(7==7) and (8>3)
(8!=7) or (3>7)
# En ambos ejemplos ambas son True por que cumplen los criterios para verdadera.

#-----
# FASE 1: NUMEROS Y OPERADORES ARITMETICOS

# En este aprenderás de la utilización de números y de las operaciones aritméticas.
# Tienes que tener en cuenta que los números enteros se especifican por la palabra int y los números reales por float. 
# En los diferentes ejercicios vas a transformar lo que el usuario introduzca con el comando input a números enteros o reales para realizar las diferentes operaciones matemáticas. 
# Para transformar los valores leídos tienes que hacerlo de la siguiente forma: 
#   Número enteros: int(input(“texto”)).  
#   Número reales: float(input(“text”)).  
# El resultado tienes que asignárselo a una variable para poder utilizarlo posteriormente.
# NOTA: LOS EJEMPLOS QUE SE REALIZEN CON INPUT ES MEJOR REALIZARLOS EN TU IDE (COMO SIEMPRE HASTA LA FECHA YO ME VOY CON VSC).

#SUMA
#Ejemplos de suma con numeros enteros
sumando1 = int(input('Cúal es tu primer número '))
sumando2 = int(input('Cúal es tu segundo número '))
print('El resultado de tu suma es',sumando1+sumando2)
#Estas líneas de código son interesantes primero usamos el nombre de la variable sumando1 posterior al = tenemos int que nos cambia todo lo que se introduzca a int y posterior abrimos 
#parentesis para introducir el input y después agregamos el mensaje para el usuario. En la parte final se encuentra un print con un parentesis que en si tiene 2 partes la primera es el 
#menaje que vamos a devolver al usuario y posterior a esto con la ',' agregamos la suma. 
#Ejemplo de suma con decimales:
decimal_uno = float(input('Cúal es tu primer número '))
decimal_dos = float(input('Cúal es tu segundo número '))
print('El resultado de tu suma es',decimal_uno+decimal_dos)
# NOTA MAS ADELANTE VAMOS A ENSEñAR a redondear.

#RESTA
#Ejemplos de resta con enteros.
minuendo = int(input('Cúal es tu minuendo '))
sustraendo = int(input('Cúal es tu sustraendo '))
print('El resultado de tu resta es',minuendo-sustraendo)
#Ejemplo de resta con float
minuendo = float(input('Cúal es tu minuendo '))
sustraendo = float(input('Cúal es tu sustraendo '))
print('El resultado de tu resta es', minuendo-sustraendo)

#Multiplicación
#Ejemplo con enteros.
multiplicando = int(input('Cúal es tumultiplicando '))
multiplicador = int(input('Cúal es tu multiplicador '))
print('El resultado de tu multiplicación es',multiplicando*multiplicador)
#Ejemplo con float.
multiplicando = float(input('Cúal es tumultiplicando '))
multiplicador = float(input('Cúal es tu multiplicador '))
print('El resultado de tu multiplicación es',multiplicando*multiplicador)

#DIVISION
#Ejemplo con enteros.
dividendo = int(input('Cúal es tu dividendo '))
divisor = int(input('Cúal es tu divisor '))
print('El resultado de tu división es',dividendo/divisor)
#Ejemplo con float.
dividendo = float(input('Cúal es tu dividendo '))
divisor = float(input('Cúal es tu divisor '))
print('El resultado de tu división es',dividendo/divisor)

#REDONDEO DE NUMEROS REALES:
# La instrucción round utiliza dos parámetros para ejecutarse. El primero de ellos es el número real que quieres redondear 
# y el segundo es el número de decimales al que quieres redondear.
#Vamos a tomar el ejemplo anterior de division con float
dividendo = float(input('Cúal es tu dividendo '))
divisor = float(input('Cúal es tu divisor '))
resultado = round(dividendo/divisor,2)
print('El resultado de tu división es',resultado)
#- En este caso lo que hicimos fue crear un paso previo con una variable llamada resultado acá realizamos la operación y le 
#agregamos el round posterior en el parentesis la operacion y por ultimo la coma y el número que quiero redondear en este caso le puse 2
# - Otra variante para la realización de este ejercicio es poner la operación con el round al final así
dividendo = float(input('Cúal es tu dividendo '))
divisor = float(input('Cúal es tu divisor '))
print('El resultado de tu división es',round(dividendo/divisor,2))
#Esto optimiza el código por que son menos líneas, se aprende con el tiempo y con el uso.

#-----
#FASE 2: Cadenas de texto (Básico)

#