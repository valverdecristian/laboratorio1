import pygame
from constantes import *

class Personaje:
    # Constructor
    def __init__(self, tamaño:tuple, origen:tuple, path) -> None:
        self.superficie = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.sonido_colision = pygame.mixer.Sound(r"clase_16_1c/recursos/acierto.wav")
        self.sonido_colision.set_volume(0.3)
    # Atributos
        self.rect = self.superficie.get_rect()
        self.rect.center = origen

    # Metodos (comportamiento)
    def mover_imagen(self, sentido:str, desplazamiento:int, tamaño_pantalla:tuple):
        if sentido == "vertical":
            self.rect.y += desplazamiento
            if self.rect.top > tamaño_pantalla[1]:
                self.rect.bottom = 0
        elif sentido == "horizontal":
            self.rect.x += desplazamiento
            if self.rect.left > tamaño_pantalla[0]:
                self.rect.right = 0
    
    def colision(self,otra_imagen):
        if self.rect.colliderect(otra_imagen.rect):
            self.sonido_colision.play()