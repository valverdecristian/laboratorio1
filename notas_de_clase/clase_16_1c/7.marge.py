import pygame, sys
from constantes import *
# from imagen import Imagen
from personaje import Personaje

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

homero = Personaje((200,200), (WIDTH/2,HEIGHT/2), r"clase_16_1c\recursos\01.png")
dona = Personaje((100,100), (WIDTH/2, HEIGHT/2), r"clase_16_1c\recursos\00.png")

fondo = pygame.image.load(r"clase_16_1c\recursos\fondo.jpg")
fondo = pygame.transform.scale(fondo, SCREEN_SIZE)

# musica
pygame.mixer.music.load(r"clase_16_1c\recursos\fondo.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.blit(fondo, (0,0))
    SCREEN.blit(dona.superficie, dona.rect)
    SCREEN.blit(homero.superficie, homero.rect)
    
    # movimiento
    homero.mover_imagen("horizontal", 20, (WIDTH,HEIGHT))
    dona.mover_imagen("vertical", 10, (WIDTH,HEIGHT))
    
    # colision
    dona.colision(homero)
    
    pygame.display.flip()