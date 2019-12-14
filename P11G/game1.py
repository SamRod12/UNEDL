import pygame
from pygame.locals import *
import os
import sys

#constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#clases y funciones que utilizamos


#funcion principal del juego

def main():
    pygame.init()
    #crear la ventana indicar el titulo que tendra
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    pygame.display.set_caption("Basico PYGAME")

    #cargar el fondo de la ventana y la imagen del pengu ( crea objetos del tipo surface)

    fondo = pygame.image.load("/Users/kiuub/PycharmProjects/Parcial 2/P11G/img/fondo.jpeg").convert()
    tux = pygame.image.load("/Users/kiuub/PycharmProjects/Parcial 2/P11G/img/tux.png").convert_alpha()

    #posicion del tux
    tux_posX = 550
    tux_posY = 200

    screen.blit(fondo, (0,0))
    screen.blit(tux , (tux_posX , tux_posY))

    #muestra los cambios en la pantalla
    clock = pygame.time.Clock()
    pygame.display.flip()

    while True:
        #restar uno a la cordenada x de tux y comprobar  que no alcance el borde de la pantalla
        tux_posX = tux_posX -1
        if tux_posX < 1:
            tux_posX = 550
        clock.tick(60)
        #indicamos la posicion de las surface sobre la ventana
        screen.blit(fondo, (0, 0))
        screen.blit(tux, (tux_posX , tux_posY))

        pygame.display.flip()
        #posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()