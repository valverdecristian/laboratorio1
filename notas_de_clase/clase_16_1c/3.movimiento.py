import pygame, sys
from constantes import *

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(NEGRO)

clock = pygame.time.Clock()

# crea una superficie -> Surface((ancho,alto))
imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)

# obtener el rect de la superficie
rect_vertical = imagen_vertical.get_rect()
rect_vertical.center = (WIDTH/2, HEIGHT/2)

while True:
    # velocidad del bucle
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # pinto de negro en cada iteracion
    SCREEN.fill(NEGRO)
    
    # blitear imagen
    SCREEN.blit(imagen_vertical, rect_vertical)
    rect_vertical.y += 5
    # rect_vertical.x += 10
    if rect_vertical.top> HEIGHT:
        # cuando desaparece de la pantalla, aparece arriba
        rect_vertical.bottom = 0
    
    # flip: actualiza toda la pantalla        
    pygame.display.flip()