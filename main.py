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

lista_asteroides1=[]
lista_asteroides2=[]
for i in range(1,6):
   lista_asteroides1.append(Asteroide(ra.randint(0,1200),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(10,40)))
for i in range(1,6):
   lista_asteroides2.append(Asteroide(ra.randint(0,1200),ra.randint(0,600),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),w=ra.randint(20,60),h=ra.randint(20,60)))

while game_over:

   valor_tasa = tasa_refresco.tick(350)
  

   for evento in pg.event.get():
      if evento.type == pg.QUIT:
         game_over = False


   pantalla_principal.fill((25, 27, 18 ))

   for asteroides in lista_asteroides1:
      asteroides.mover()
      asteroides.dibujarAsteroide1(pantalla_principal)

   for asteroides2 in lista_asteroides2:
      asteroides2.mover()
      asteroides2.dibujarAsteroide2(pantalla_principal)
   
   nave.mover(pg.K_UP,pg.K_DOWN)
   
   nave.dibujar(pantalla_principal)
   
   pg.display.flip()
   
         

pg.quit()