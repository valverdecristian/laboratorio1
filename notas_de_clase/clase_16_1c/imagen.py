import pygame
from constantes import *

class Imagen:
    # Constructor
    def __init__(self, tamaño:tuple, colores:tuple, origen:tuple) -> None:
        self.superficie = pygame.Surface(tamaño)
        self.color_inicial = colores[0]
        self.color_colision = colores[1]
        self.superficie.fill(self.color_inicial)
    # Atributos (setters y getters)
        self.rect = self.superficie.get_rect()
        self.rect.center = origen
        
    # Metodos (comportamiento)
    def mover_imagen(self, sentido:str, desplazamiento:int, tamaño_pantalla:tuple):
        if sentido == "vertical":
            self.rect.y += desplazamiento
            if self.rect.top > tamaño_pantalla[1]: # tam_pantalla recibe una tupla
                self.rect.bottom = 0
        elif sentido == "horizontal":
            self.rect.x += desplazamiento
            if self.rect.left > tamaño_pantalla[0]:
                self.rect.right = 0
    
    def colision(self,otra_imagen):
        if self.rect.colliderect(otra_imagen.rect):
            self.superficie.fill(self.color_colision)
            otra_imagen.superficie.fill(otra_imagen.color_colision)
        else:
            self.superficie.fill(self.color_inicial)
            otra_imagen.superficie.fill(otra_imagen.color_inicial)
            