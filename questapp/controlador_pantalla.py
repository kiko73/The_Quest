from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.record = Record()
        
      
       
   
    def start(self):
            continuar_partida= "seguir"
            valor = self.menu.bucle_pantalla()
                                                                                                                      
            if valor == "partida":
                while continuar_partida == "seguir":
                    partida = Partida()
                    partida.bucle_fotograma()
                    valor = self.partida.fin_de_juego()

                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_r:
                                break                

                    
                    menu=Menu()
                    menu.bucle_pantalla()
                            
        
                    
                       
                         
                    

                   
                    
                   
           

            
                   
                    
        
          
    

            
       

