from constantes import *
import pygame
import random
from donas import *

flag = True

score = 0

pygame.init()
reloj = pygame.time.Clock()

# genero un evento propio
tick = pygame.USEREVENT + 0 # evento propio
pygame.time.set_timer(tick, 100) # que se dispara cada 100 miliseg

# CONFIGURACIONES --------------------------------------------
# PANTALLA
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Homero Donas")

# FONDO
fondo = pygame.image.load(r"clase_17_1c\HOMERO\recursos\fondo1.png")
fondo = pygame.transform.scale(fondo, SCREEN_SIZE)
SCREEN.blit(fondo,(0,0))

# # musica
# pygame.mixer.music.load(r"clase_17_1c\HOMERO\recursos\fondo.wav")
# pygame.mixer.music.play()
# pygame.mixer.music.set_volume(0.2)

# FUENTE
fuente = pygame.font.SysFont("helvetica",50)

#--------------------------------------------------------------
# HOMERO (deberia estar en homero.py)

w_homero = 200
h_homero = 200

# superficie (asociar con un rect)
imagen_homero = pygame.image.load(r"clase_17_1c\HOMERO\recursos\01r.png")
imagen_homero = pygame.transform.scale(imagen_homero, (w_homero,h_homero))
rect_homero = imagen_homero.get_rect()
# ubicacion del homero
rect_homero.x = 400
rect_homero.y = 600 # height - tamaño

# constantes de la boca de homero
x = 500
y = 700
z = 50
# corregir como come homero y las colisiones
# crear un rect a la altura de la boca
rect_boca = pygame.Rect(x,y,z,z)

# lo metemos en un dict
personaje = {
    "superficie": imagen_homero,
    "rectangulo": rect_homero,
    "rect_boca": rect_boca,
    "puntaje": score
}

# DONAS
lista_donas = crear_lista_donas(20)

while flag:
    reloj.tick(FPS)
    
    # EVENTOS que puedo capturar en general
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        # evento disparado por el usuario (ejemplo muerte del personaje)
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                update(lista_donas)
                
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT]:
        imagen_homero = pygame.image.load(r"clase_17_1c\HOMERO\recursos\01r.png")
        imagen_homero = pygame.transform.scale(imagen_homero, (w_homero,h_homero))
        SCREEN.blit(imagen_homero, rect_homero)
        nueva_x = rect_homero.x -10
        
        # para que no salga de cuadro:
        if nueva_x > 0:
            rect_homero.x = rect_homero.x -10
            rect_boca.x = rect_boca.x -10
            
    elif lista_teclas[pygame.K_RIGHT]:
        imagen_homero = pygame.image.load(r"clase_17_1c\HOMERO\recursos\01r.png")
        imagen_homero = pygame.transform.scale(imagen_homero, (w_homero,h_homero))
        SCREEN.blit(imagen_homero, rect_homero)
        nueva_x = rect_homero.x +10
        if nueva_x > 0:
            rect_homero.x = rect_homero.x +10
            rect_boca.x = rect_boca.x +10
            
    SCREEN.blit(fondo,(0,0))
    SCREEN.blit(imagen_homero, rect_homero)
    
    for dona in lista_donas:
        SCREEN.blit(dona["superficie"], dona["rectangulo"])
    
    actualizar_pantalla(lista_donas, personaje, SCREEN)
    
    # score
    puntaje = fuente.render("SCORE: {0}".format(personaje["puntaje"]), True, ROJO)
    SCREEN.blit(puntaje,(0,0))
    
    # bordes del rectangulo
    pygame.draw.rect(SCREEN, ROJO, rect_homero, 2)
    pygame.draw.rect(SCREEN, ROJO, rect_boca, 2)
    
    pygame.display.flip()