import os
import pygame
from pygame import gfxdraw
import sys
import math
from OpenGL.GL import *
from pygame import OPENGLBLIT
from pygame import OPENGL
from OpenGL.GLU import *
import random
from math import *


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def Round(a):
    return int(a + 0.5)


def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Draw():
    drawEllipseMED((300,300),120,80,[1,0,0])
    drawEllipseMED((300,300),80,120,[1,0,0])
    pygame.display.update()


def drawEllipseMED(center, rx, ry, color):
    xc, yc = center[0], center[1]
    x = 0
    y = ry
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    # For region 1
    while (dx < dy):
        # Print points based on 4-way symmetry
        gfxdraw.pixel(screen, int(x+xc), int(y+yc), color)
        gfxdraw.pixel(screen, int(-x+xc), int(y+yc), color)
        gfxdraw.pixel(screen, int(x+xc), int(-y+yc), color)
        gfxdraw.pixel(screen, int(-x+xc), int(-y+yc), color)
        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    # Plotting points of region 2
    while (y >= 0):
        # printing points based on 4-way symmetry
        gfxdraw.pixel(screen, int(x+xc), int(y+yc), color)
        gfxdraw.pixel(screen, int(-x+xc), int(y+yc), color)
        gfxdraw.pixel(screen, int(x+xc), int(-y+yc), color)
        gfxdraw.pixel(screen, int(-x+xc), int(-y+yc), color)
        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)



size = [640, 720]
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
Draw()
mainloop()
