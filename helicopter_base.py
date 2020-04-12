import pygame as pg
import os
import random

pg.init()
width = 600
height = 600
v = 1
screen = pg.display.set_mode((width, height))


def write(text, x, y, size):
    cz = pg.font.SysFont("Arial", size)
    rend = cz.render(text, 1, (255, 0, 0))
    screen.blit(rend, (x, y))

class obstacle():
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.y_up = 0
        self.h_up = random.randint(150, 250)
        self.space = 200
        self.y_down = self.h_up + self.space
        self.h_down = height - self.y_down
        self.color = (160, 140, 190)
        self.shape_up = pg.Rect(self.x, self.y_up, self.width, self.h_up)
        self.shape_down = pg.Rect(self.x, self.y_down, self.width, self.h_down)
    def draw(self):
        pg.draw.rect(screen, self.color, self.shape_up, 0)
        pg.draw.rect(screen, self.color, self.shape_down, 0)
    def movement(self, v):
        self.x = self.x - v
        self.shape_up = pg.Rect(self.x, self.y_up, self.width, self.h_up)
        self.shape_down = pg.Rect(self.x, self.y_down, self.width, self.h_down)

whatShows = 'gameplay'

obstacles = []
for i in range(21):
    obstacles.append(obstacle(int(i * width/20), int(width/20)))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill((0,0,0))
    if whatShows == 'menu':
        graphic = pg.image.load(os.path.join('logo.png'))
        screen.blit(graphic, (0, 0))
        write('Press space to start', 200, 450, 20)
    elif whatShows == 'gameplay':
        for o in obstacles:
            o.movement(v)
            o.draw()

    pg.display.update()

