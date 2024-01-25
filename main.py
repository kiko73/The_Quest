import pygame as pg
from figura_class import Asteroide,Nave
import random as ra

pg.init()
X_MAX = 1300
Y_MAX = 700

pantalla_principal = pg.display.set_mode((X_MAX,Y_MAX))
pg.display.set_caption("The Quest")

tasa_refresco = pg.time.Clock()

nave = Nave(10, 350 - (60//2))

game_over = True


lista_asteroides=[]

for i in range(1,12):
   lista_asteroides.append(Asteroide(ra.randint(0,1200),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(10,40)))


while game_over:

   valor_tasa = tasa_refresco.tick(350)
  

   for evento in pg.event.get():
      if evento.type == pg.QUIT:
         game_over = False
    

   pantalla_principal.fill((25, 27, 18 ))
   nave.dibujar(pantalla_principal)

   
   
   for asteroides in (lista_asteroides):
      asteroides.mover()
      asteroides.dibujarAsteroide(pantalla_principal)
      
      if asteroides.izquierda <= nave.derecha and\
         asteroides.derecha >= nave.izquierda and\
         asteroides.abajo >= nave.arriba and\
         asteroides.arriba <= nave.abajo:
            asteroides.vx*= 0
        

   
   asteroides.comprobar_choque(nave)
   asteroides.mostrar_marcador(pantalla_principal)

   nave.mover(pg.K_UP,pg.K_DOWN)

   
   
   pg.display.flip()
   
         

pg.quit()