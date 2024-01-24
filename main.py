import pygame as pg
from figura_class import Asteroide,Nave
import random as ra

pg.init()

pantalla_principal = pg.display.set_mode((1300,700))
pg.display.set_caption("The Quest")

tasa_refresco = pg.time.Clock()
"""
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
"""
nave = Nave(10, 350 - (60//2))

game_over = True

lista_asteroides=[]
for i in range(1,10):
   lista_asteroides.append(Asteroide(ra.randit(0,1200),ra.randint(0,600),(ra.randit(0,255),ra.randit(0,255),ra.randit(0,255)),radio=ra.randint=(10.100)))
   



while game_over:

   valor_tasa = tasa_refresco.tick(350)
  
   

   for evento in pg.event.get():
      if evento.type == pg.QUIT:
         game_over = False


   pantalla_principal.fill((25, 27, 18 ))
   
   nave.mover(pg.K_UP,pg.K_DOWN)
   """
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
   """
   nave.dibujar(pantalla_principal)
   
   pg.display.flip()
   
         

pg.quit()