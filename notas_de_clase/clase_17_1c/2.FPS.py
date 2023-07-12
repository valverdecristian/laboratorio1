# cuantos cuadros por seg veo

import pygame, sys
from constantes import *
import random

# escribir texto en una superficie
screen_size = (WIDTH,HEIGHT)

pygame.init()
SCREEN = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Prueba FPS")

# superficie texto
fuente = pygame.font.SysFont("consolas", 60)
texto = fuente.render("contador/vidas", False, ROJO)

# lista de circulos / coordenadas aleatorias
circulos = list()
for i in range(50):
    x = random.randint(1, WIDTH -1)
    y = random.randint(1, HEIGHT -1)
    circulos.append([x,y])

# medir cuanto tiempo paso
reloj = pygame.time.Clock()

flag = True
while flag:
    # manejo del tiempo (mayor numero = mas lento)
    tiempo = reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            
    SCREEN.fill(NEGRO)
    
    # movimiento de circulos
    for circulo in circulos:
        circulo[0] +=1
        circulo[1] +=2
        if circulo[0] > WIDTH:
            circulo[0] = 0
        if circulo[1] > HEIGHT:
            circulo[1] = 0
    
    for circulo in circulos:
        pygame.draw.circle(SCREEN, ROJO, (circulo[0],circulo[1]), 5, 10)

    pygame.display.flip()
    
    # mejor usar FPS
    # pygame.time.delay(10)
    
pygame.quit()