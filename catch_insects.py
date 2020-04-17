import pygame as pg
import os
import random
import time

### --- In this game player has to catch bugs when they appear to score. Bugs show up faster with time and if they reach a critical number the game ends --- ###

pg.init()
width = 600
height = 600
screen = pg.display.set_mode((width, height))

def write(text, x, y, size):
    """This functions writes a text message in a specified location"""
    cz = pg.font.SysFont("Arial", size)
    rend = cz.render(text, 1, (255, 0, 0))
    screen.blit(rend, (x, y))

class insect():
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.h = 20
        self.w = 20
        self.shape = pg.Rect(self.x, self.y, self.h, self.w)
        self.color = (0, 100, 0)
        self.sprite = pg.image.load(os.path.join('insect_sprite.png'))
        self.dx = random.randint(-1, 1)
        self.dy = random.randint(-1, 1)
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.dx = random.randint(-1, 1)
        self.dy = random.randint(-1, 1)
        self.shape = pg.Rect(self.x, self.y, self.w, self.h)
    def if_catch(self, player):
        if self.shape.colliderect(player.shape):
            return True
        else:
            return False

    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))
        pg.draw.rect(screen, self.color, self.shape, 1)
class catcher():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.dx = 0
        self.dy = 0
        self.h = 30
        self.w = 30
        self.color = (100, 0, 0)
        self.shape = pg.Rect(self.x, self.y, self.w, self.h)
        self.sprite = pg.image.load(os.path.join('hat_sprite.png'))
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.shape = pg.Rect(self.x, self.y, self.w, self.h)
    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))
        pg.draw.rect(screen, self.color, self.shape, 1)


whatShows = 'menu'
delta = 10
ddelta = 10
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYUP:
            p_dx = 0
            p_dy = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                p_dx = -1
            if event.key == pg.K_RIGHT:
                p_dx = 1
            if event.key == pg.K_UP:
                p_dy = -1
            if event.key == pg.K_DOWN:
                p_dy = 1
            if event.key == pg.K_SPACE:
                if whatShows != 'gameplay':
                    ### --- Setting up the game --- ###
                    whatShows = 'gameplay'
                    player = catcher()
                    max_insects = 10
                    enemies = []
                    start = time.time()
                    enemy_timer_start = time.time()
                    delta_timer_start = time.time()
                    p_dx = 0
                    p_dy = 0
                    timer = 0
                    score = 0
                    end_time = 180

    screen.fill((0, 0, 0))
    if whatShows == 'gameplay':
        enemy_timer_end = time.time() - enemy_timer_start
        delta_timer_end = time.time() - delta_timer_start
        if enemy_timer_end > delta:
            ### --- This cause add insects after delta time --- ###
            new_enemy = insect()
            enemies.append(new_enemy)
            enemy_timer_start = time.time()
        if delta_timer_end > ddelta:
            ### --- This cause makes sure that the bugs are added faster with time --- ###
            delta = 3*delta/4
            delta_timer_start = time.time()
        for enemy in enemies:
            if enemy.if_catch(player):
                score = score + 1
                enemies.remove(enemy)
            enemy.move()
            enemy.draw()
        player.move(p_dx, p_dy)
        player.draw()
        write('Score:' + str(score), 10, 10, 20)

        if len(enemies) >= max_insects:
            whatShows = 'gameover'

    elif whatShows == 'menu':
        write('Welcome to bugs game', width / 2, 3*height / 4, 20)
        write('Press space to start', width/2, height/2, 20)
    elif whatShows == 'gameover':
        write('Game Over', width/2, height/2, 50)
        write('Your score = ' + str(score), width / 2, height - height / 3, 20)
        write('Press space to play again', width / 2, height - height / 4, 20)

    time.sleep(0.0001) # This value is calibrated such that the gameplay is comfortable
    pg.display.update()

