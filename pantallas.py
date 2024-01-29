import pygame as pg
from questapp.figura_class import Asteroide,Nave,Planeta
import random as ra
from questapp.utils import*

ANCHO = 1300
ALTO = 700
COLOR_NAVE = (255,255,255)
COLOR_FONDO = (25, 27, 18 )
COLOR_BLANCO = (255,255,255)


class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("The Quest")
        self.tasa_refresco = pg.time.Clock()

        self.nave = Nave(10, ALTO//2 - (60//2))
        self.planeta = Planeta(ANCHO,ALTO//2)
        self.fuente = pg.font.Font(None,30)
        self.contadorTiempo = 0
        self.contadorVidas = 0
        self.lista_asteroides=[]

        for i in range(1,12):
            self.lista_asteroides.append(Asteroide(ra.randint(0,1200),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(20,40)))
    
    def bucle_fotograma(self):
        game_over = True
        while game_over:
            self.valor_tasa = self.tasa_refresco.tick(350)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False

            self.pantalla_principal.fill( COLOR_FONDO)
            self.nave.dibujar(self.pantalla_principal)
            self.planeta.dibujarPlaneta(self.pantalla_principal)
            self.mostrar_juego()

            
            
            for asteroides in (self.lista_asteroides):
                asteroides.mover()
                asteroides.dibujarAsteroide(self.pantalla_principal)
                
                if asteroides.izquierda <= self.nave.derecha and\
                    asteroides.derecha >= self.nave.izquierda and\
                    asteroides.abajo >= self.nave.arriba and\
                    asteroides.arriba <= self.nave.abajo:
                        asteroides.vx*= 0
                    

            
            asteroides.comprobar_choque(self.nave)
            asteroides.mostrar_marcador(self.pantalla_principal)

            self.nave.mover(pg.K_UP,pg.K_DOWN)

            
            
            pg.display.flip()
   
         

        pg.quit()

    def mostrar_juego(self):
        tiempo = self.fuente.render("Tiempo",True,(135, 19, 238))
        punto = self.fuente.render("Puntos",True,(135, 19, 238))
        self.pantalla_principal.blit(tiempo,(20,20))
        self.pantalla_principal.blit(punto,(170,20))

    def mostrar_marcador(self):
        self.fuente = pg.font.Font(None,30)
        marcador1 = self.fuente.render(str(self.contadorTiempo),True,(149, 14, 3))
        marcador2 = self.fuente.render(str(self.contadorVidas),True,(149, 14, 3))
        self.pantalla_principal.blit(marcador1,(50,50))
        self.pantalla_principal.blit(marcador2,(200,50))

    

