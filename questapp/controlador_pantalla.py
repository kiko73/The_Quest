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
                while continuar_partida == "menu":
                    partida = Partida()
                    partida.bucle_fotograma()
                    continuar_partida = self.partida.fin_de_juego()
                       
                record = Record()
                record.bucle_pantalla()

            
            
                
       

