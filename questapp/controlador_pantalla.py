from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        #self.continuar = Continuar()
        self.record = Record()

    def start(self):
        valor = self.menu.bucle_pantalla()

        if valor == "partida":
            self.partida.bucle_fotograma()
            continuar_partida = self.partida.fin_de_juego()
            if continuar_partida !="":    
                continuar = Continuar(continuar_partida)
                continuar.bucle_pantalla()
        elif valor =="record":
            self.record.bucle_pantalla()

