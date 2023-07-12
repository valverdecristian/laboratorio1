'''
15 Jun, 2023
¿Que es la POO?
POO: Paradigma Orientado a Objetos
El paradigma orientado a objetos responde a una
forma de encarar un proyecto de desarrollo de
software.

¿Que son los objetivos?
Un objeto podria representar a una persona con
caracteristicas como nombre, edad y direccion y
comportamientos como caminar, hablar, respirar, etc.

Los objetos se empiezan a relacionar y comunicar

Los objetos tienen una parte estatica y una dinamica:
    estatica -> caracteristicas (son los atributos de la clase)
    dinamica -> comportamientos (son los metodos de la clase)

Hasta el momento veniamos trabajando con un paradigma estructurado
creabamos una funcion y a esa funcion le pasabamos el diccionario
por parametro -> esto responde a un "paradigma estructurado"

¿Se puede evitar usar la POO?
    Las estructuras de datos primitivas, como numeros,
    cadenas, diccionarios y listas, estan diseñadas
    para representar informacion simple.

    * para evitar usarlas usamos variables para
    las diferentes caracteristicas
    * tambien usar una lista
    * otra forma es representar un personaje a traves
    de un diccionario (esto hasta el momento era lo que usamos)
    pero se vuelve tedioso si quiero hacer lo mismo
    para cada personaje.

CLASE:
    -> define caracteristicas y acciones
    Podemos definirla como un molde que DEFINIRÁ las
    caracteristicas y acciones que tendrá un objeto.
    componentes estaticos -> son los atributos de la clase
    componentes dinamicos -> son los metodos de la clase

Atributos:
    A las caracteristicas de un objeto las vamos a llamar
    propiedades o atributos. Estos atributos los tendran
    todos los objetos de tipo Personaje. Los mismos se
    definiran en un metodo llamado __init__(Constructor de la clase).

Atributos de clase:
    * __init__ -> constructor de la clase
    * SELF -> representa la instancia actual, es la direccion de memoria
    del objeto con el cual yo estoy trabajando

Crear una instancia:
    La creacion de un nuevo objeto a partir de una clase se
    denomina instancia de un objeto (se crea un objeto en memoria)
    Se puede instanciar un nuevo Personaje escribiendo el nombre de
    la clase, seguido de parentesis de apertura y cierre

Metodos:
    * son los componentes dinamicos de un objeto
    * son funciones que se definen dentro de una clase
    y solo se pueden llamar desde una instancia de esa clase.

<< IMPORTANTE >>
el primer paramero de un metodo de instancia siempre es self

EXISTEN CUATRO PILARES EN LA POO:
    1) ABSTRACCIÓN
    2) HERENCIA
    3) POLIMORFISMO
    4) ENCAPSULACIÓN -> importante por ahora
    ejemplo: un control remoto tiene varios botones: prender la tele, bajar y subir volumen, etc
    * yo como persona no se como el control manda esa señal a la tele (eso es encapsular)
    * por lo general los atributos de una clase se tienen que encapsular

CLASES:
    Atributos publicos (+ publico): 
        * Los atributos de una clase por default son publicos    
        * Lo publico signifca que lo puede ver desde cualquier lugar
    
    Atributos protegidos:

    Atributos privados (- privado):
    * por lo general lo defino con dos gion bajo -> self.__atributo
    * todo atributo que yo defina como privado dentro de una clase, no se
    puede ver desde ningun otro lugar que no sea la clase
    * se acceden a traves de unos metodos especiales: geters y seters
    * en definitiva, podria definir los metodos de forma publica ya qye luego
    lo muestro, pero no seria una buena practica, ya que no se puede modificar
    o no se deberia (encapzular el atributo a traves de la clase)

Property:

Metodos dunder:


'''

#definiendo una clase:
# las clases se escriben en CapitalizedWords
class Personaje:
    '''atributos adoptados por todos los objetos
    * Cada uno de estos atributos se van a definir dentro de
    un metodo, que se llama metodo constructor.
    Las acciones que definen una clase y que va a implementar
    un objeto a partir de ahora se va a llamar METODO.
    '''
    def __init__(self, id, nombre, nano, vuela) -> None: #constructor de la clase (def __init__ self)
        #self representa el objeto en si mismo (representa al personaje)
        self.id = id #self.id -> define un atributo que se llama id, le asigno lo que recibo por parametro
        self.__nombre = nombre # (- privado)
        self.usa_nanotecnologia = nano
        self.puede_volar = vuela
        
    # al ser __nombre un atributo privado lo que hago es setearlo
    def set_nombre(self, nombre): #seter para poder asignar un valor
        self.__nombre = nombre
        
    '''si defino solo el get es de solo lectura'''
    def get_nombre(self): #geter para que se vea desde afuera
        return self.__nombre
    
    # METODOS    
    def retornar_descripcion(self) -> str:
        descripcion = "{0} - {1} - {2} - {3}".format(self.id, self.__nombre, self.puede_volar, self.usa_nanotecnologia)
        return descripcion
        
personaje_a = Personaje(1, "IronMan", "No", "Si")
personaje_b = Personaje(2, "IronSpider", "Si", "No")

# el personaje sabe describirse
# print(personaje_b.retornar_descripcion())

print(personaje_a.get_nombre()) # muestra IronMan

#proxima clase
#cargar una imagen
#fundir