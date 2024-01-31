import pygame as pg
from questapp.figura_class import Asteroide,Nave,Planeta
import random as ra
from questapp.utils import*


class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("The Quest")
        self.tasa_refresco = pg.time.Clock()

        self.nave = Nave(10, ALTO//2 - (60//2))
        self.planeta = Planeta(ANCHO,ALTO//2)
        self.asteroides = []
        
        for i in range(1,12):
            self.asteroides.append(Asteroide(ra.randint(100,1300),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(20,40)))

        self.fuente = pg.font.Font("questapp/fonts/Orbitron.ttf",30)
        self.contadorTiempo = 0
        self.contadorPuntos = 0
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        
        

    def bucle_fotograma(self):

        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(150)
            self.temporizador = self.temporizador - self.valor_tasa
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.game_over = False

            self.puntuacion()
            self.velocidad_juego()
            self.fin_de_juego()
                
            self.pantalla_principal.fill( COLOR_FONDO)
            self.nave.dibujar(self.pantalla_principal)
            self.planeta.dibujarPlaneta(self.pantalla_principal)
            self.mostrar_juego()

            if self.temporizador >0:
                for asteroides in (self.asteroides):
                    asteroides.mover()
                    asteroides.dibujarAsteroide(self.pantalla_principal)
                    
                    if asteroides.izquierda <= self.nave.derecha and\
                        asteroides.derecha >= self.nave.izquierda and\
                        asteroides.abajo >= self.nave.arriba and\
                        asteroides.arriba <= self.nave.abajo:
                            self.game_over = False
                            asteroides.vx*= 0

            if self.temporizador <= 0:
                self.planeta.pos_x = ANCHO
                self.planeta.pos_y = ra.randint(0,ALTO)
                    

            
            asteroides.comprobar_choque(self.nave)
            self.mostrar_marcador()
            self.nave.mover(pg.K_UP,pg.K_DOWN)
            self.planeta.mover()

            
            
            pg.display.flip()
   
         

        pg.quit()

    def mostrar_juego(self):
        tiempo = self.fuente.render("Tiempo",True,(COLOR_MORADO))
        punto = self.fuente.render("Puntos",True,(COLOR_MORADO))
        self.pantalla_principal.blit(tiempo,(20,20))
        self.pantalla_principal.blit(punto,(170,20))
        

    def mostrar_marcador(self):
        marcador1 = self.fuente.render(str(int(self.temporizador/1000)),True,(COLOR_BLANCO))
        marcador2 = self.fuente.render(str(int(self.contadorPuntos/100)),True,(COLOR_BLANCO))
        self.pantalla_principal.blit(marcador1,(60,60))
        self.pantalla_principal.blit(marcador2,(210,60))

    

    def fin_de_juego(self):
        if self.temporizador <= 0 - 10000:
            self.game_over = False

    
    def velocidad_juego(self):
        if self.temporizador <=30000:
            self.valor_tasa = self.valor_tasa + self.valor_tasa

    def puntuacion(self):
        if self.temporizador >= -1000:
            self.contadorPuntos += 1

        if self.temporizador <=30000:
            self.contadorPuntos += 1*2

        if self.temporizador <=15000:
            self.contadorPuntos += 1*4

        if self.temporizador < 0:
            self.contadorPuntos += 1*10

    
         
        
            

        

        



        


    
                

        
    
    
    





    

