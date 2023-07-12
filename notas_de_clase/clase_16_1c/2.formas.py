import pygame, sys
from constantes import *

pygame.init()

# setmode recibe una tupla -> el ancho y alto de la pantalla
# la pantalla va por fuera del bucle
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(NEGRO)

'''RECTANGULO'''
x = 100 # mayor valor = hacia derecha
y = 300 # mayor valor = hacia abajo
w_rec = 300
h_rec = 100
# si le agrego un parametro mas es el grosor del rect
rectangulo = pygame.draw.rect(SCREEN,VERDE,(x,y,w_rec,h_rec))

'''LINEA'''
principio = (100,100)
fin = (300,300)
grosor = 10
linea = pygame.draw.line(SCREEN,ROJO,principio,fin,grosor)

'''CIRCULO'''
ubicacion = (400,600)
radio = 50
pygame.draw.circle(SCREEN, AZUL, ubicacion, radio)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    # update: actualiza partes especificas de la pantalla
    # flip: actualiza toda la pantalla
    pygame.display.update()