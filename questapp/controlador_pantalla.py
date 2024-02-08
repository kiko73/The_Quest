from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.record = Record()
        self.vidas = 3
      
       
   
    def start(self):
            continuar_partida= "seguir"
            valor = self.menu.bucle_pantalla()

            if valor == "partida":
                while continuar_partida == "menu":
                    partida = Partida()
                    partida.bucle_fotograma()
                    continuar_partida = self.partida.fin_de_juego()
                    return Menu
                
                partida= Partida()
                partida.bucle_fotograma()
          
            juego = self.partida.bucle_fotograma()

            if juego == "seguir":
                 while continuar_partida == "menu":
                    menu = Menu()
                    menu.bucle_pantalla()
                    continuar_partida = self.partida.fin_de_juego()
                  
    
    

            
       

