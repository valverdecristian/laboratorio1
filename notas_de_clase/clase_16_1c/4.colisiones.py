import pygame, sys
from constantes import *

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(NEGRO)

clock = pygame.time.Clock()

# crea una superficie -> Surface((ancho,alto))
im_vertical = pygame.Surface((100,100))
im_vertical.fill(VERDE)

im_horizontal = pygame.Surface((100,100))
im_horizontal.fill(AZUL)

# obtener el rect de la superficie
rect_vertical = im_vertical.get_rect()
rect_vertical.center = (WIDTH/2, HEIGHT/2)

rect_h = im_horizontal.get_rect()
rect_h.center = (WIDTH-100, HEIGHT/2)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.fill(NEGRO)
    SCREEN.blit(im_vertical, rect_vertical)
    SCREEN.blit(im_horizontal, rect_h)
    
    # rect_v
    rect_vertical.y += 15
    if rect_vertical.top> HEIGHT:
        # cuando desaparece de la pantalla, aparece arriba
        rect_vertical.bottom = 0

    # rect_h
    rect_h.x += 5
    if rect_h.left > WIDTH:
        rect_h.right = 0
        
    # colision
    if rect_h.colliderect(rect_vertical):
        im_horizontal.fill(ROJO)
        im_vertical.fill(BLANCO)
    else:
        im_horizontal.fill(AZUL)
        im_vertical.fill(VERDE)
    
    pygame.display.flip()