from questapp.pantallas import Partida,Menu,Continuar

menu= Menu()

valor = menu.bucle_pantalla()


juego = Partida()

if valor == "partida":
    juego.bucle_fotograma()

continuar_partida = juego.fin_de_juego()

continuar = Continuar(continuar_partida)
continuar.bucle_pantalla()



















