import main as comand
import pygame
import sys
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pygame.init()
pygame.display.set_mode((screen_width/2, screen_height/2))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
