import pygame as pg
from figura_class import Asteroide

pg.init()

pantalla_principal = pg.display.set_mode((1300,700))
pg.display.set_caption("The Quest")

asteroide = Asteroide(1250,350,(218, 99, 35),20)

game_over = True

while game_over:
   

   for evento in pg.event.get():
      if evento.type == pg.QUIT:
         game_over = False

   pantalla_principal.fill((25, 27, 18 ))
   
   asteroide.dibujar(pantalla_principal)
   pg.display.flip()
   
         

pg.quit()