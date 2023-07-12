import pygame, sys

WIDTH = 500 # ancho
HEIGHT = 500 # alto

pygame.init()

# setmode recibe una tupla -> el ancho y alto de la pantalla
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()