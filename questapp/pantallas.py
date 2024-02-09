
from questapp.figura_class import Asteroide,Nave,Planeta
import random as ra
from questapp.utils import*
import sqlite3


class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("The Quest")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load("questapp/images/fondo.png")
        self.nave = Nave(10, ALTO//2 - (60//2))
        self.planeta = Planeta(ANCHO,ALTO//2)
        self.sonido_explosion = pg.mixer.Sound("questapp/sounds/destroyer.wav")
        self.asteroides = []
        
        for i in range(1,12):
            self.asteroides.append(Asteroide(ra.randint(10,1300),ra.randint(0,700),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(20,40)))

        self.fuente = pg.font.Font(FUENTE1,30)
        self.fuente2 = pg.font.Font(FUENTE2,20)
        self.fuente3 = pg.font.Font(FUENTE1,80)
        self.contadorTiempo = 0
        self.contadorPuntos = 0
        self.contadorVidas = 3
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.aparecer_planeta = False
        self.explosion1 = pg.image.load("questapp/images/explosion1.png").convert_alpha()
        self.explosion2 = pg.image.load("questapp/images/explosion2.png").convert_alpha()
        self.explosion3 = pg.image.load("questapp/images/explosion3.png").convert_alpha()
        
        
    

    def bucle_fotograma(self):
        self.temporizador = TIEMPO_JUEGO
        self.tasa_refresco.tick()
        

        explosion_offset_x = 0
        explosion_offset_y = 0

        while self.game_over:
          
            self.valor_tasa = self.tasa_refresco.tick(600)
            self.temporizador = self.temporizador - self.valor_tasa
            
            if self.game_over:
                for evento in pg.event.get():
                    if evento.type == pg.QUIT:
                        self.game_over = False
                
            enter = pg.key.get_pressed()
            if enter[pg.K_r]:
                return "menu"
            
            
            
            self.puntuacion()
            self.velocidad_juego()
            self.fin_de_juego()
            self.aterrizaje()  
            self.pantalla_principal.fill( COLOR_FONDO)
            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            self.nave.dibujar(self.pantalla_principal)
            self.planeta.dibujarPlaneta(self.pantalla_principal)
            self.mostrar_marcador()
            self.mostrar_juego()
            self.mostrar_texto(pg)
            
            
                 
            
            for asteroides in (self.asteroides):
                asteroides.mover()
                asteroides.dibujarAsteroide(self.pantalla_principal)

                        
                
                if self.temporizador >0:
                    if asteroides.izquierda <= self.nave.derecha and\
                            asteroides.derecha >= self.nave.izquierda and\
                            asteroides.abajo >= self.nave.arriba and\
                            asteroides.arriba <= self.nave.abajo:
                        
                        self.contadorVidas -= 1
                        
                        
                        asteroides.vx*= 1
                        

                        pg.mixer.Sound.set_volume(self.sonido_explosion,0.05)
                        pg.mixer.Sound.play(self.sonido_explosion)
                            #pg.time.delay(5000)
                            
                        for i in range(3):
                            pos_x = self.nave.pos_x - explosion_offset_x
                            pos_y = self.nave.pos_y - explosion_offset_y
                                
                            self.pantalla_principal.blit(self.explosion1, (pos_x, pos_y))
                            self.pantalla_principal.blit(self.explosion2, (pos_x, pos_y))
                            self.pantalla_principal.blit(self.explosion3, (pos_x, pos_y))
                            pg.display.flip() 
                            self.pantalla_principal.fill(COLOR_FONDO) 
                            pg.display.flip() 
            
            if self.contadorVidas <= 0:
                self.game_over = False               
                      
                           
            if self.aparecer_planeta:
                if self.planeta.pos_x > ANCHO:
                    self.planeta.pos_x -= 0.5

            if self.temporizador <= 0:
                self.aparecer_planeta = True
                                    
            
            
            self.nave.mover(pg.K_UP,pg.K_DOWN)
            self.planeta.mover()

            
            
            pg.display.flip()

         

    def mostrar_marcador(self):

        marcador1 = self.fuente2.render(str(int(self.temporizador/1000)),True,(COLOR_BLANCO))
        marcador2 = self.fuente2.render(str(int(self.contadorPuntos)),True,(COLOR_BLANCO))
        self.pantalla_principal.blit(marcador1,(60,60))
        self.pantalla_principal.blit(marcador2,(210,60))
        marcador3 = self.fuente2.render(str(int(self.contadorVidas)),True,(COLOR_BLANCO))
        self.pantalla_principal.blit(marcador3,(360,60))

        if self.temporizador <= 0 - 10000:
            self.contadorPuntos = False
            

    def mostrar_juego(self):
        tiempo = self.fuente.render("Tiempo",True,(COLOR_MORADO))
        punto = self.fuente.render("Puntos",True,(COLOR_MORADO))
        vidas = self.fuente.render("Vidas",True,(COLOR_MORADO))
        self.pantalla_principal.blit(tiempo,(20,20))
        self.pantalla_principal.blit(punto,(170,20))
        self.pantalla_principal.blit(vidas,(320,20))

    def fin_de_juego(self):
        if self.temporizador <=0 - 15000:
            self.game_over = False
            

    def mostrar_texto(self,pg):
        if self.temporizador <= 0 - 10000:
            texto_continuar = self.fuente3.render("Pulsa r para continuar",True,COLOR_ROJO)
            self.pantalla_principal.blit(texto_continuar,(10,300))
        
            enter = pg.key.get_pressed()
            if enter[pg.K_RETURN]:
                return "menu"
        
            
            
    def velocidad_juego(self):
        if self.temporizador <=30000:
            self.valor_tasa = self.valor_tasa + self.valor_tasa


   
    def puntuacion(self):
        multiplicador = 1
        if self.temporizador <=30000:
            multiplicador = 2
        if self.temporizador <=15000:
            multiplicador = 4
        if self.temporizador < 0:
            multiplicador = 1000

        self.contadorPuntos += multiplicador * 1
    

    def aterrizaje(self):
        if self.temporizador <= 0:
            centro_x = 920
            centro_y = 350
            velocidad_movimiento = 0.1

            if self.nave.pos_x < centro_x:
                self.nave.pos_x += velocidad_movimiento * self.valor_tasa
            elif self.nave.pos_x > centro_x:
                self.nave.pos_x -= velocidad_movimiento * self.valor_tasa

            if self.nave.pos_y < centro_y:
                self.nave.pos_y += velocidad_movimiento * self.valor_tasa
            elif self.nave.pos_y > centro_y:
                self.nave.pos_y -= velocidad_movimiento * self.valor_tasa

            if self.temporizador <= -6000:
                self.nave.rotar(1)
                if self.nave.rotacion_completa:
                    self.aparecer_planeta = True
            


class Menu:
    
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Menu")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo2 = pg.image.load("questapp/images/fondo2.png")
        self.fuente = pg.font.Font(FUENTE2,50)
        self.fuente2 = pg.font.Font(FUENTE1,20)
        self.sonido = pg.mixer.Sound("questapp/sounds/menu.mp3")
        

        self.pos_x_menu = 100
        self.pos_y_menu = 550
        self.pos_x_titulo = 400
        self.pos_y_titulo = 50
        self.pos_x_instrucciones = 300
        self.pos_y_instrucciones = 300
        self.bucle_pantalla()

    def mostrar_texto(self,texto,fuente,color,posicion):
        texto_principio = fuente.render(texto,True,color)
        self.pantalla_principal.blit(texto_principio,posicion)

    def bucle_pantalla(self):
        game_over= True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido,0.05)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False

            enter = pg.key.get_pressed()
            if enter[pg.K_RETURN]:
                #game_over = False
                pg.mixer.Sound.stop(self.sonido)
                return "partida"



            self.pantalla_principal.blit(self.imagenFondo2,(0,0))

            self.mostrar_texto("Pulsa ENTER para jugar",self.fuente,COLOR_ROJO,(self.pos_x_menu,self.pos_y_menu))
            self.mostrar_texto("THE QUEST",self.fuente,COLOR_ROJO,(self.pos_x_titulo,self.pos_y_titulo))
            self.mostrar_texto("En el año 2153, la raza humana debe iniciar la busqueda de nuevos planetas habitables para su supervivencia.",self.fuente2,COLOR_AMARILLO,(10,150))
            self.mostrar_texto("Despues de 10 años de travesía por el espacio, los tripulantes de la nave NEW EXPLORER creen haber encontrado",self.fuente2,COLOR_AMARILLO,(10,180))
            self.mostrar_texto("un planeta adecuado, pero una nube de asteroides se interpone en su camino.",self.fuente2,COLOR_AMARILLO,(10,210))
            self.mostrar_texto("INSTRUCCIONES",self.fuente,COLOR_ROJO,(300,300))
            self.mostrar_texto("Dispones de 60 segundos para esquivar los asteroides y aterrizar en Orion73, cuanto mas tiempo estes en el aire",self.fuente2,COLOR_AMARILLO,(10,360))
            self.mostrar_texto("mas puntos recibiras. Mueve la nave hacia arriba y abajo con el cursor y pasa de nivel, pero ¡cuidado!, porqué por",self.fuente2,COLOR_AMARILLO,(10,390))
            self.mostrar_texto("cada nivel que superes, aumentaran el número de asteroides y su velocidad. Si aterrizas sin percances , recibiras",self.fuente2,COLOR_AMARILLO,(10,420))
            self.mostrar_texto("un extra de puntos. Suerte y recuerda que el futuro de la humanidad depende de ti.",self.fuente2,COLOR_AMARILLO,(10,450))


           

            pg.display.flip()
        

class Record:
    
    def __init__(self):

        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Puntuaciones")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo3 = pg.image.load("questapp/images/fondo3.png")
        self.fuente = pg.font.Font(FUENTE2,20)
        self.fuente2 = pg.font.Font(FUENTE2,50)
        self.bucle_pantalla()
        #self.puntajes()

    def bucle_pantalla(self):
        game_over= True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
            
            enter = pg.key.get_pressed()
            if enter[pg.K_z]:
                return "seguir"
            


            #self.pantalla_principal.fill(self.imagenFondo3,(0,0))
            texto = self.fuente2.render("Mejores Puntuaciones",0,COLOR_ROJO)
            self.pantalla_principal.blit(texto,(160,100))
            texto_continuar= self.fuente.render("Pulsa z para continuar",True,COLOR_ROJO)
            self.pantalla_principal.blit(texto_continuar,(350,600))


            pg.display.flip()
    """   
    def puntajes(self):
        con = sqlite3.connect("data/puntuaciones.sqlite")
        cur = con.cursor()
        res = cur.execute("select * from records;")
        res.fetchall()
        res.description
    """

       



      
    

        





        

            
            
                  
            
    
    
         
        
            

        

        



        


    
                

        
    
    
    





    

