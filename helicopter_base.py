import pygame as pg
import os
import random
import time

pg.init()
width = 600
height = 600
v_screen = 1
v_helicopter = 1
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

class helictoper():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 30
        self.width = 50
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)
        self.sprite = pg.image.load(os.path.join('heli_sprite.png'))
    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))
    def move(self, v):
        self.x = self.x
        self.y = self.y - v
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)
whatShows = 'gameplay'
player = helictoper(300, 300)
dy = 0
obstacles = []
for i in range(21):
    obstacles.append(obstacle(int(i * width/20), int(width/20)))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                dy = v_helicopter
            elif event.key == pg.K_DOWN:
                dy = -v_helicopter
        if event.type == pg.KEYUP:
            dy = 0
        if event.type != pg.KEYUP and event.type != pg.KEYDOWN:
            dy = 0
    screen.fill((0,0,0))
    if whatShows == 'menu':
        graphic = pg.image.load(os.path.join('logo.png'))
        screen.blit(graphic, (0, 0))
        write('Press space to start', 200, 450, 20)
    elif whatShows == 'gameplay':
        for o in obstacles:
            o.movement(v_screen)
            o.draw()
        for o in obstacles:
            if o.x <= -o.width:
                obstacles.remove(o)
                obstacles.append(obstacle(width, int(width/20)))
        player.draw()
        player.move(dy)
    time.sleep(0.001)


    pg.display.update()

