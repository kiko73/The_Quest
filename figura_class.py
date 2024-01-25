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
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=20,radio=5,vx=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio
        self.vx = vx
        self.contadorTiempo = 0
        self.contadorVidas = 0
        

    def dibujarAsteroide(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)


    def mover(self, X_MAX=1300):
        self.pos_x -= self.vx

        if self.pos_x >= X_MAX + (10*self.radio) or self.pos_x <=0:
            self.pos_x = 1300
            self.vx *=-1

    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None,30)
        marcador1 = fuente.render(str(self.contadorTiempo),True,(255,255,255))
        marcador2 = fuente.render(str(self.contadorVidas),True,(255,255,255))
        pantalla.blit(marcador1,(20,20))
        pantalla.blit(marcador2,(50,20))

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

    

     





        
        

        
    
        
    