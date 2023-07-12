import pygame
from constantes import *

screen_size = (WIDTH,HEIGHT)

pygame.init()
SCREEN = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Prueba eventos")

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False
            
        # sirve para areas de un boton
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            
    SCREEN.fill(NEGRO)
    
    pygame.display.flip()
    
pygame.quit()