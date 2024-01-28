import pygame as pg
from figura_class import Asteroide,Nave,Planeta
import random as ra

ANCHO = 1300
ALTO = 700
class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("The Quest")
        self.tasa_refresco = pg.time.Clock()

        self.nave = Nave(10, 350 - (60//2))
        self.planeta = Planeta(1300,350)
        
        self.lista_asteroides=[]

        for i in range(1,12):
            self.lista_asteroides.append(Asteroide(ra.randint(0,1200),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(20,40)))