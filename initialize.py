import main
import pygame as pg
import sys


# generation_map = []

pg.init()

screen = pg.display.set_mode((main.screen_width/2, main.screen_height/2))

background = pg.image.load("textures\\backgrounds\\background.jpg")
background = pg.transform.scale(background, (main.screen_width/2, main.screen_height/2))
screen.blit(background, (0, 0))


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
