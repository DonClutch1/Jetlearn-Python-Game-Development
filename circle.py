import pgzrun
import pygame
import pgzero
from random import randint

WIDTH = 300
HEIGHT = 300
x = randint(0, WIDTH)
y = randint(0, HEIGHT - 100)
radius = randint(10, 30)
color = (randint(0,255), randint(0,255), randint(0,255))
def draw():
    screen.clear()
    screen.draw.filled_circle((x,y), radius, color)
pgzrun.go()
