import pygame as pg
from .utils import*

class Nave:
    def __init__(self, pos_x,pos_y,color=COLOR_NAVE,w=60,h=60,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
        

    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))

    def mover(self,teclado_arriba,teclado_abajo):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0<=(self.h):
            self.pos_y -= 1
        
        if estado_teclado[teclado_abajo] == True and self.pos_y <= 700-(self.h):
            self.pos_y += 1
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
    def __init__(self,pos_x,pos_y,color=COLOR_BLANCO,w=20,h=20,radio=5,vx=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx
        

    def dibujarAsteroide(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)


    def mover(self, X_MAX=1300):
        self.pos_x -= self.vx

        if self.pos_x >= X_MAX + (10*self.radio) or self.pos_x <=0:
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
    

    def comprobar_choque(self,nave):
        
        if self.izquierda <= nave.derecha and\
            self.derecha >= nave.izquierda and\
            self.abajo >= nave.arriba and\
            self.arriba <= nave.abajo:
                self.vx*= 0

    
            

class Planeta():
    def __init__(self,pos_x,pos_y,color=COLOR_BLANCO,w=20,h=20,radio=300,vx=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx

    def dibujarPlaneta(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self, X_MAX=1300):
        self.pos_x -= self.vx

        if self.pos_x >= X_MAX + (10*self.radio) or self.pos_x <=0:
            self.pos_x =ANCHO
            self.vx *=-1
    


    

     





        
        

        
    
        
    