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
                
                
                menu=Menu()
                menu.bucle_pantalla()
                return "menu"

           
           
           
            """
            valor = self.menu.bucle_pantalla() #valor = menu

            while valor != "salir":  #mientras que valor sea distinto o igual salir                                                                                                        
                if valor == "partida":  #si menu es igual a partida  
                    self.partida.bucle_fotograma() #se ejecuta bucle fotograma de partida
                    valor = self.partida.fin_de_juego() #menu = fin

                   

                    
                    
                    valor = self.menu.bucle_pantalla() 
            """           
        
                    
                       
                         
                    

                   
                    
                   
           

            
                   
                    
        
          
    

            
       

