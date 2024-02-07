from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.record = Record()
        #self.continuar = Continuar()
       

    def start(self):
        valor = self.menu.bucle_pantalla()

        if valor == "partida":
            self.partida.bucle_fotograma()
            continuar_partida = self.partida.fin_de_juego()
            if continuar_partida !="":    
                record = Record(continuar_partida)
                record.bucle_pantalla()
        #elif valor =="record":
            #self.record.bucle_pantalla()

