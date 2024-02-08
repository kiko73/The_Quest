import pygame as pg
from .utils import*
import random as ra


class Nave:
    def __init__(self, pos_x,pos_y,color=COLOR_NAVE,w=80,h=60,vx=1,vy=3):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
        self.nave_original = pg.image.load("questapp/images/nave.png")
        self.nave = self.nave_original
        self.angulo = 0
        
   
    def dibujar(self,surface):
        surface.blit(self.nave,(self.pos_x-(self.w//2 - 40),self.pos_y-(self.h//2)))

    def mover(self,teclado_arriba,teclado_abajo):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0<=(self.h):
            self.pos_y -= 2
        
        if estado_teclado[teclado_abajo] == True and self.pos_y <= 700-(self.h):
            self.pos_y += 2

    def rotar(self,grados_por_paso):
        self.angulo = grados_por_paso
        if self.angulo <= 180:
            self.angulo = 180
            self.rotacion_completa = True
        self.nave = pg.transform.rotate(self.nave_original,self.angulo)

    @property
    def derecha(self):
        return self.pos_x + self.w//2
    
    @property
    def izquierda(self):
        return self.pos_x - self.w//2
    
    @property
    def arriba(self):
        return self.pos_y - self.h//2
    
    @property
    def abajo(self):
        return self.pos_y + self.h//2
        
        

class Asteroide:
    def __init__(self,pos_x,pos_y,color=COLOR_BLANCO,w=20,h=20,radio=5,vx=2):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx
        self.asteroide = pg.image.load("questapp/images/asteroide.png")
        self.asteroide2 = pg.image.load("questapp/images/asteroide2.png")
        
        

    def dibujarAsteroide(self,surface):
        surface.blit(self.asteroide,(self.pos_x ,self.pos_y + 100))
        surface.blit(self.asteroide2,(self.pos_x,self.pos_y))

    def mover(self, X_MAX=1300):
        self.pos_x -= self.vx

        if self.pos_x >= X_MAX + (self.radio) or self.pos_x <=0:
            self.pos_x =ANCHO
            self.vx *=-1 
        

    @property
    def derecha(self):
        return self.pos_x + self.radio
    
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    
    @property
    def arriba(self):
        return self.pos_y - self.radio
    
    @property
    def abajo(self):
        return self.pos_y + self.radio
    
    """
    def comprobar_choque(self,nave):
        
        if self.izquierda <= nave.derecha and\
            self.derecha >= nave.izquierda and\
            self.abajo >= nave.arriba and\
            self.arriba <= nave.abajo:
                pg.mixer.Sound.play(self.sonido)
                self.vx*= 0
    """
    
            

class Planeta():
    def __init__(self,pos_x,pos_y,color=COLOR_AMARILLO,w=300,h=300,radio=300,vx=1):
        self.pos_x = pos_x + 300
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx
        #self.planeta = pg.image.load("questapp/images/planeta.png")
        

    def dibujarPlaneta(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)
        #surface.blit(self.planeta,(self.pos_x,self.pos_y))
    
    def mover(self):
        self.pos_x -= self.vx
        if self.pos_x == self.pos_x:
            self.vx = 0
        
        
            
    


    

     





        
        

        
    
        
    