'''
clase 8: 25 de Abril, 2023
STRING
'''
declaracion = list()
# las cadenas en python o strings son un tipo inmutable
# que permite almacenar secuencias de caracteres.
# Para crear una, es necesario incluir el
# texto...
# puedo arrancar un str con comillas simples o dobles
# adentro puedo utilizar la otra comilla dentro del str
# -> lo mas normal: comillas dobles

caracteres_especiales = list()
# \n -> representa un salto de linea


metodos = list()
# un metodo es una funcion especial, que existe para 
# un tipo de dato particular.
# Para trabajar con cadenas de texto, se emplean una 
# serie de metodos a las variables del tipo str
'''
CADENA -> significa que la variable va en el parametro del metodo
'''

texto = "hola Cristian ¿Como estas?"

# len(CADENA) -> devuelve la longitud de la cadena (cuenta los espacios tmb)
print(len(texto))

# lower() -> devuelve en minusculas la cadena
print(texto.lower())

# upper() -> devuelve en mayusculas la cadena
print(texto.upper())

# capitalize() -> convertira a la primera letra en mayuscula
print("capitalize ->",texto.capitalize())

# strip() -> devuelve la cadena sin espacios en blanco al principio ni al final
print("strip ->",texto.strip())

# split(separador) -> divide el texto y genera una lista con elementos
# si no le paso nada en el parametro, por defecto separa por espacio
print("split(vacio) ->",texto.split())

texto2 = "hola . capo . como . estas"
separador = " . "
print("split('.') ->",texto2.split("."))

# join() -> devuelve la union de los elementos de una lista en una cadena de texto,
# separado por el elemento especifico (separador)
lista = ["hola","mundo","!"]
separador = "\n"
print("join ->",separador.join(lista))

# replace(vieja_cad,nueva_cad) -> reemplazara un conjunto de caracteres por otro.
print("replace ->",texto.replace("Cristian","Ariel"))

# find(subcadena) -> devuelve el índice de la primera ocurrencia de la subcadena en
# la cadena, o -1 si no se encuentra
print("find ->",texto.find("tian")) #devuelve 9 xq la t esta en el i9

# isalpha() -> devuelve True si todos los caracteres son alfabetico,
# False de lo contrario. el espacio es un caracter especial.
print("isalpha() ->", texto.isalpha())

# isalnum() -> devuelve True si todos los caracteres son alfanumericos,
# False de lo contrario.
print("isalnum() ->", texto.isalnum())

# isdigit() -> devuelve True o False, es mas restrictivo, ya que solo
# verifica si los caracteres son digitos
print("isdigit() ->", texto.isdigit())

# count("ocurrencias") -> devuelve la cantidad de ocurrencias que se encuentran en la cadena
print("count letra 'o' ->", texto.count("o"))

# zfill() -> nos permite agragar ceros a un str. lo que le pase en el parametro sera
# la longitud de la cadena. ejemplo si tengo 44 y le paso por parametro (5) devolvera "00044"
cadena = "44"
print("zfill(5) ->", cadena.zfill(5))

# .formart(variable/s) busca que reemplazar dentro de las llaves con las variables.

# f-strings -> las cadenas literales o f-strings, permite incrustar expresiones dentro de cadenas.
# dentro de las llaves van el nombre de la variable.

'''SLICE'''
# cuando se crea una SLICE (rebanada), el primer numero es donde comienza (inclusivo)
#[inicio:fin:paso]

nombre = "cristian valverde"
#si quiero mostrar el 1er caracter
print("slice[0] ->", nombre[0])

#si quiero mostrar desde el 1er caracter hasta el 5to
print("slice[:6] ->", nombre[:6])

#si quiero mostrar desde el 1er caracter hasta el 5to de 2 en 2
print("slice[:8:2] ->", nombre[:6:2])

#si quiero mostrar los ultimos 4 caracteres
print("slice[-4:] ->", nombre[-4:])
