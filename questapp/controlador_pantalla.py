from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.record = Record()
        
      
       
   
    def start(self):
           
            valor = self.menu.bucle_pantalla()

            while valor != "salir":                                                                                                          
                if valor == "partida":    
                    self.partida.bucle_fotograma()
                    valor = self.partida.fin_de_juego()

                   

                    
                    
                    valor = self.menu.bucle_pantalla()
                            
        
                    
                       
                         
                    

                   
                    
                   
           

            
                   
                    
        
          
    

            
       

