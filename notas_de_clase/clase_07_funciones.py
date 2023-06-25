'''
clase 7: 20 de Abril, 2023
FUNCIONES
'''

# creo un diccionario vacio
diccionario = dict()

# asignarle claves y valores
diccionario["nombre"] = "Cristian"
diccionario["apellido"] = "Valverde"

# mostrar diccionario
print(diccionario)

# con IN pregunto si esa clave esta o no esta en el diccionario

# EJERCICIO 15:
'''
Crear una función que recibe una lista de diccionarios con información de películas
(título, género, director) y devuelve un diccionario con la cantidad de películas por género.
'''


def contar_peliculas_por_genero(lista_dict_peliculas: list):
    # creamos un diccionario vacio
    peliculas_por_genero = dict()

    # recorremos la lista de peliculas y analizamos el "genero"
    for pelicula in lista_dict_peliculas:
        texto_genero = pelicula["genero"]
        texto_titulo = pelicula["titulo"]

        if texto_genero in peliculas_por_genero:
            auxliliar_lista = peliculas_por_genero[texto_genero]
            auxliliar_lista.append(texto_titulo)

        else:
            auxliliar_lista = list()
            auxliliar_lista.append(texto_titulo)
            peliculas_por_genero[texto_genero] = auxliliar_lista

    return peliculas_por_genero


dict_peliculas = [{"titulo": "El padrino", "genero": "drama", "director": "Francis Ford Coppola"},
                  {"titulo": "El señor de los anillos",
                      "genero": "fantasía", "director": "Peter Jackson"},
                  {"titulo": "Star Wars: Una nueva esperanza",
                      "genero": "ficción", "director": "George Lucas"},
                  {"titulo": "Matrix", "genero": "ficción",
                      "director": "Lana y Lilly Wachowski"},
                  {"titulo": "El club de la pelea", "genero": "drama", "director": "David Fincher"}]

resultado = contar_peliculas_por_genero(dict_peliculas)

print(resultado)
