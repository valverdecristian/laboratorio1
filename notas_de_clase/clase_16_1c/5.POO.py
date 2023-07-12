import pygame, sys
from constantes import *
from imagen import Imagen

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(NEGRO)

clock = pygame.time.Clock()

im_vertical = Imagen((100,100), (VERDE,BLANCO), (WIDTH/2, HEIGHT/2))
im_horizontal = Imagen((100,100), (AZUL,ROJO), (WIDTH-100, HEIGHT/2))

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.fill(NEGRO)
    SCREEN.blit(im_vertical.superficie, im_vertical.rect)
    SCREEN.blit(im_horizontal.superficie, im_horizontal.rect)
    
    # movimiento
    im_horizontal.mover_imagen("horizontal", 20, (WIDTH,HEIGHT))
    im_vertical.mover_imagen("vertical", 10, (WIDTH,HEIGHT))
    
    # colision
    im_vertical.colision(im_horizontal)
    
    pygame.display.flip()