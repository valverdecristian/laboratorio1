'''
Clase 11: 4 de Mayo, 2023
Tema: ARCHIVOS
'''
import json
'''
ARCHIVO DE TEXTO: contienen caracteres legibles, es posible no solo
leer dicho contenido sino tambien modificarlo usando un editor de texto.

ARCHIVO BINARIO: no se puede interpretar con un editor de texto.
no se puede interpretar: una imagen (jpg), un sonido (mp4)
o incluso un archivo comprimido.

MODOS DE APERTURA
MODO       DESCRIPCION
r          abre un archivo de texto solo para lectura.
rb         abre un archivo binario solo para lectura
r+         abre un archivo de texto para escritura y lectura
w          abre un arch de txt solo para escritura (si existe lo sobreescribe)
wb         abre un arch solo para escritura (si existe lo sobreescribe)
w+         abre un arch de txt para escritura y lectura (si existe lo sobreescribe)
a(open)    abre un arch para anexar información. El puntero del archivo esta
            al final del archivo si este existe. -es decir, el archivo esta en modo
            anexo, si el archivo no existe, crea un nuevo archivo para escritura.

ABRIR Y CERRAR
para abrir un archivo usamos la funcion open.

    archivo = open(nombre_archivo. modo)

archivo: objeto file, el cual sera utilizado para llamar a otros metodos
asociados con el archivo.

nombre_archivo: string que contiene el nombre del archivo al que
queremos acceder

modo: string que contiene el modo de apertura del archivo.

cerrar un archivo: close

    archivo.close()
    
archivo: objeto file que fue obtenido con el metodo open.

EL OBJETO FILE

    archivo = open(nombre_archivo, modo)

LEER: read
el metodo read permite extraer un string que contenga todos los caracteres
del archivo.
Es posible limitar al metodo read a que lea cierta cantidad de bytes read(cantidad)

-> APERTURA - LECTURA - CIERRE

ESCRIBIR

CSV
el CSV es un tipo de documento que representa los datos de forma parecida a una
tabla, es decir, organizando la informacion en filas y columnas.
Las columnas son separadas, por un signo de puntuacion (,;.)... continua

JSON
es un formato para intercambio de datos basado en texto. Por lo que es facil
de leer tanto... continua
para nosotros termina siendo un diccionario para nosotros.

'''
# abrimos el archivo en modo lectura y escritura
# open recibe 2 parametros (1: la ruta, 2: modo de apertura (como yo lo quiero abrir))
# por convencion los archivos se abren en forma de texto:
# para leer(r/r+), escribir(w/w+) o añadir info(a)
# archivo = open('archivo.txt', 'r+')
# texto = archivo.read(10)
# print("el contenido del archivo es: " + texto)
# # cerramos el archivo
# archivo.close()

# leer por lineas: readlines (como un archivo csv)
# archivo = open('archivo.txt', 'r+')
# lista_lineas = archivo.readlines() # lee la linea del archivo y lo pone en una lista
# for linea in lista_lineas:
#     print(linea, end="")
# # cerramos el archivo
# archivo.close()

# LEER UN ARCHIVO: FILE
# no tiene la necesidad de levantar el archivo en disco
# si solamente requerimos recorrer el archivo linea por linea, el objeto file es iterable
# archivo = open('archivo.txt', 'r+')
# for linea in archivo: # tengo en memoria de una linea a la vez
#     print(linea, end="")
# # cerramos el archivo
# archivo.close()

# metodo seek: mover el puntero. mueve por bytes

# administrador de contexto: with
# podemos usar la sentencia with para abrir archivos en python y dejar
# que el interprete se encargue de cerrar el mismo.
# with open('archiv.txt', 'r+') as archivo:
#     for linea in archivo:
#         print(linea, end="")


'''
funciones parser

# definimos la funcion leer csv: abrir, leerlo y devolver info(list)
'''
ruta = "C:\\Users\\crizt\\OneDrive\\Documentos\\programacion 2023\\1er cuatrimestre\\Laboratorio y Programacion I\\SABADOS\\para trabajar archivos\\usuarios.csv"
rutaJSON = "C:\\Users\\crizt\\OneDrive\\Documentos\\programacion 2023\\1er cuatrimestre\\Laboratorio y Programacion I\\SABADOS\\para trabajar archivos\\usuarios2.json"


def leer_csv(ruta: str) -> list:
    lista_retorno = []
    # with trabaja comoa adm de contexto: abre y luego lo cierra
    # archivo: objeto file -> iterable
    with open(ruta, 'r') as archivo:
        for usuario in archivo:
            # deberia traer los datos de ese usuario y guardarlo en una variable
            # despues meterlo en la lista que quiero retornar
            lista_aux = usuario.split(',')
            lista_retorno.append(lista_aux)

    return lista_retorno


def guardar_csv(ruta: str, lista_usuarios: list):
    with open(ruta, 'w') as archivo:
        for usuario in lista_usuarios:
            archivo.write(",".join(usuario) + '\n')


def leer_json(ruta: str) -> list:

    with open(ruta, 'r') as archivo:
        diccionario_usuarios = json.load(archivo)
    return diccionario_usuarios["usuarios"]


print(leer_json(rutaJSON))


# lista_usuarios = leer_csv(ruta)
# guardar_csv("prueba.csv", lista_usuarios)
# print(lista_usuarios, end="")
