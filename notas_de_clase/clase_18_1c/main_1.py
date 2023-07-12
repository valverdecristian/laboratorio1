import pygame
import sys
from constantes import *
from configuraciones import *

######## FUNCIONES DE MOVIMIENTO #################################
def mover_personaje():
    pass


def animar_personaje(pantalla, rect_personaje, accion_personaje):
    # no se puede inicializar porque ya tiene un valor
    global contador_pasos
    
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
        
    pantalla.blit(accion_personaje[contador_pasos],rect_personaje)
    contador_pasos +=1
    
    
# actualizar pantalla
def actualizar_pantalla(pantalla, que_hace, velocidad):
    
    # animar el personaje y moverlo
    match que_hace:
        case "Derecha":
            pass
            #animar
            #mover
        case "Quieto":
            pass
        # animar

##################################################################

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# fondo
fondo = pygame.image.load(r"clase_18_1c\recursos\fondo_space.png")
fondo = pygame.transform.scale(fondo, (SCREEN_SIZE))

# personaje
x_inicial = HEIGHT/2 - 400
y_inicial = 750
contador_pasos = 0
velocidad = 10

rect_personaje = lista_personaje_camina[0].get_rect()
# darle ubicacion al rectangulo / posicionarlo
rect_personaje.x = x_inicial
rect_personaje.y = y_inicial

# definir donde esta posicionado
posicion_actual_x = 0
que_hace = "Quieto"



while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # teclas presionadas
    keys = pygame.key.get_pressed()
    if keys(pygame.K_RIGHT):
        que_hace = "Derecho"
    else:
        que_hace = "Quieto"
            
    SCREEN.blit(fondo, (0,0))
    
    
    
    pygame.display.flip()