Juego del espacio hecho con pygame en el que una nave debe esquivar asteroides hsata aterrizar en un planeta


-Activar el entorno e instalar los requerimientos

python3 -m venv entorno
.\entorno\Scripts\activate
instalamos pygame
pip install -r requirements.txt
para actualizar requirements.txt pip freeze > requirements.txt
instalacion de pygame_gui para base de datos

-Juego

Se ejecuta en Main
Aparece la pantalla de Menu
Enter para empezar a jugar
con los cursores arriba y abajo manejas la nave para esquivar los asteroides
si hay choque se produce una explosion y se vuelve a Menu para volver a empezar la partida
Al cabo de 60 segundos sin choques el juego toma el control y la nave aterriza sola en el planeta Orion
Se muestra la puntuacion en pantalla y se vuelve a Menu







