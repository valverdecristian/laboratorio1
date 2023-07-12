'''
Clase 10: 2 de Mayo, 2023
Tema: EXPRESIONES REGULARES
'''
import re

'''
() -> sirven para agrupar/delimitar toda una expresion regular
[] -> define un conjunto, vamos a decir que contiene adentro. por ejemplo vocales [aeiou]
{} -> delimitamos cuantas veces.
{3,6} -> el limite seria entre 3 y 6. sirve para caracteres.
+ -> toma todas las repeticiones
* -> ninguna o mas ocurrencias
? -> cero o una ocurrencias
| -> una o la otra "hola|chau" "[\|]{2}|[#]{1}"
^ -> empieza con...
$ -> termina con...
\d ---> todos los digitos
\w ---> alfa numerico
\s ---> todos los separadores
\b -> secuencia de escape que representa un limite de palabras, util para buscar palabras
especificas completas y no una subcadena que forme parte de otra palabra
algunos caracteres necesitan ser escapados, con la contra barra
por ejemplo: - , | , 

sub -> genera un nuevo string
'''

'''
donde podriamos estar usando expReg? - en la busqueda de archivos
re -> regular expresion. cuenta con un conjunto de metodos que permiten
comprobar...#falta
'''

# METODOS
# split() -> retorna una lista que contiene la cadena dividida por el
# numero de ocurrencias del patron
texto = "hola . mundo . cruel"
print(re.split('\. ', texto))

texto = "hola . mundo .. cruel"
print(re.split('\.{1,2} ', texto))

texto = "hola .. mundo .... cruel"
print(re.split('\.+ ', texto)) # ['hola ', 'mundo ', 'cruel']

texto = "uno 1 dos 2 tres 3 cuatro"
print(re.split('[0-9]+', texto)) # ['uno ', ' dos ', ' tres ', ' cuatro']

print(re.split('[a-z ]+', texto)) # ['', '1', '2', '3', '']

# sub() -> nos permite buscar y reemplazar 
nombre = "Marina anabe11a Cardozo"
print(re.sub('[0-9]','*',nombre))

#usando el findall
fecha = "hoy es 2023/04/29 y son las 10:45:15"
print(re.findall(r'[0-9]{4}', fecha))
print(re.findall(r'/[0-9]{2}/', fecha))
print(re.findall(r'[0-9]{4}/[0-9]{2}/[0-9]{2}', fecha))
#encontrar la hora
print(re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', fecha))

fecha = "2023/05/02 10:45:15"
print(re.findall(r'([0-9]{4}/[0-9]{2}/[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})', fecha))
#devuelve una tupla porque esta entre ()

#match -> Devuelve Matched o None, pero lo podes usar en un if, ej:
coincide = re.match(r'([0-9]{4}/[0-9]{2}/[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})', fecha)
if coincide: 
    print(coincide) # <re.Match object; span=(0, 19), match='2023/05/02 10:45:15'>
else:
    print(coincide) # None
    
# search() -> devuelve un objeto y nos dice si es objeto o None

texto = 'QUEVEDO || BZRP Music Sessions #52'

# importante tener en cuenta los () que es lo que va a devolver en el print
print(re.findall(r"[a-zA-Z ]{2,}[|]{2}([a-zA-Z ]{2,})#([0-9]+)",texto))

# -------------------------------------------------------

def validar_entero(cadena):
    patron = r'^\d+$'
    if re.match(patron, cadena):
        return True
    else:
        return False

def validar_decimal(cadena):
    patron = r'^\d+\.\d+$'
    if re.match(patron, cadena):
        return True
    else:
        return False

def validar_palabra_especifica(cadena, palabra):
    patron = r'\b' + re.escape(palabra) + r'\b'
    if re.search(patron, cadena):
        return True
    else:
        return False

def validar_letra_especifica(cadena, letra):
    patron = r'^' + re.escape(letra) + r'$'
    if re.match(patron, cadena):
        return True
    else:
        return False