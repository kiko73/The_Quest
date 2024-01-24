import pygame as pg

class Nave:
    def __init__(self, pos_x,pos_y,color=(255,255,255),w=60,h=60,vx=1,vy=1):
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

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0+(self.h//2):
            self.pos_y -= 1
        
        if estado_teclado[teclado_abajo] == True and self.pos_y <= 700-(self.h//2):
            self.pos_y += 1
        
        

class Asteroide:
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=20,radio=5,vx=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx

    def dibujarAsteroide1(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)

    def dibujarAsteroide2(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))


    def mover(self, X_MAX=1300):
        self.pos_x -= self.vx

        if self.pos_x >= X_MAX + (2*self.radio) or self.pos_x <=0:
            self.pos_x = 1300
            self.vx *=-1


        
        

        
    
        
    