import main
import pygame as pg
import sys
import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth() * 0.7
screen_height = root.winfo_screenheight() * 0.7

# generation_map = []

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))

background = pg.image.load("textures\\backgrounds\\background.jpg")
background = pg.transform.scale(background, (screen_width, screen_height))

kolb = pg.image.load("textures\\tubes\\5_kolb.png")
kolb = pg.transform.scale(kolb, (screen_width, screen_height))

screen.blit(background, (0, 0))
screen.blit(kolb, (0, 0))


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
