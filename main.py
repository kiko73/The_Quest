import pygame as pg
from figura_class import Asteroide,Nave

pg.init()

pantalla_principal = pg.display.set_mode((1300,700))
pg.display.set_caption("The Quest")

asteroide = Asteroide(1250,350,(218, 99, 35),50)
asteroide1 = Asteroide(600,600,(195, 238, 19),60)
asteroide2 = Asteroide(800,200,(135, 19, 238),40)
asteroide3 = Asteroide(1000,100,(19, 238, 125),20)
asteroide4 = Asteroide(300,150,(182, 238, 19),15)
asteroide5 = Asteroide(1100,500,(46, 19, 238),30)
asteroide6 = Asteroide(650,300,(238, 42, 19),70)
asteroide7 = Asteroide(400,550,(49, 19, 238),20)
asteroide8 = Asteroide(200,600,(238, 19, 49),20)
asteroide9 = Asteroide(800,650,(221, 19, 238),50)

nave = Nave(0, 350 - 30,(255,255,255),60,60)

game_over = True

while game_over:
   

   for evento in pg.event.get():
      if evento.type == pg.QUIT:
         game_over = False

   pantalla_principal.fill((25, 27, 18 ))
   
   asteroide.dibujar(pantalla_principal)
   asteroide1.dibujar(pantalla_principal)
   asteroide2.dibujar(pantalla_principal)
   asteroide3.dibujar(pantalla_principal)
   asteroide4.dibujar(pantalla_principal)
   asteroide5.dibujar(pantalla_principal)
   asteroide6.dibujar(pantalla_principal)
   asteroide7.dibujar(pantalla_principal)
   asteroide8.dibujar(pantalla_principal)
   asteroide9.dibujar(pantalla_principal)

   nave.dibujar(pantalla_principal)
   
   pg.display.flip()
   
         

pg.quit()