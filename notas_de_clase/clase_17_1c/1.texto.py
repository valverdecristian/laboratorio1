import pygame, sys
from constantes import *

# escribir texto en una superficie
screen_size = (WIDTH,HEIGHT)

pygame.init()
SCREEN = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Prueba texto")

# superficie texto
fuente = pygame.font.SysFont("consolas", 60)
texto = fuente.render("contador/vidas", False, ROJO)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            
    SCREEN.blit(texto, (0,0))

    pygame.display.update()
    
pygame.quit()