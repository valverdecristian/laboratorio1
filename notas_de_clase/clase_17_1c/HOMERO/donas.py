import pygame
import random
# creamos las donas

# redefinir luego esta funcion en una clase

# caracteristicas de las donas
def crear(x,y,w,h,path:str) -> dict:
    im_dona = pygame.image.load(path)
    im_dona = pygame.transform.scale(im_dona, (w,h))
    rect = im_dona.get_rect()
    rect.x = x
    rect.y = y
    
    dict_dona = dict()
    dict_dona["superficie"] = im_dona
    dict_dona["rectangulo"] = rect
    dict_dona["velocidad"] = random.randrange(10,20,1)
    
    return dict_dona

def crear_lista_donas(cantidad:int) -> list:
    lista_donas = list()
    for i in range(cantidad):
        # generar cooredenadas aleatorias
        x = random.randrange(0,740,60)
        y = random.randrange(-1000,0,60)
        
        # lista de donas
        dicccionario = crear(x,y,60,60, r"clase_17_1c\HOMERO\recursos\00.png")
        lista_donas.append(dicccionario)
        
    return lista_donas
    
    
# permite mover las donas
def update(lista_donas):
    for dona in lista_donas:
        # mover en posicion y
        rect = dona["rectangulo"]
        rect.y += dona["velocidad"]
        
def actualizar_pantalla(lista_donas, personaje, ventana):
    for dona in lista_donas:
        if personaje["rect_boca"].colliderect(dona["rectangulo"]):
            print("colisiono")
            personaje["puntaje"] += 100
            desaparecer_dona(dona)
        elif dona["rectangulo"].y > 800:
            desaparecer_dona(dona)
            
# para que las donas recirculen
def desaparecer_dona(dona):
    dona["rectangulo"].x = random.randrange(0,740,60)
    dona["rectangulo"].y = random.randrange(-1000,0,60)