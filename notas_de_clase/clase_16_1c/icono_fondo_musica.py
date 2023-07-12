import pygame, sys
from constantes import *

screen_size = (WIDTH,HEIGHT)

pygame.init()

# setmode recibe una tupla -> el ancho y alto de la pantalla
SCREEN = pygame.display.set_mode(screen_size)

# icono
icono = pygame.image.load(r"clase_16_1c\recursos\01.png")
pygame.display.set_icon(icono)

# fondo
fondo = pygame.image.load(r"clase_16_1c\recursos\fondo.jpg")
fondo = pygame.transform.scale(fondo, screen_size)
SCREEN.blit(fondo, (0,0))

# musica
pygame.mixer.music.load(r"clase_16_1c\recursos\fondo.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()