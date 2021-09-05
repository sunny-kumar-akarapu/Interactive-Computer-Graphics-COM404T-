import os
import pygame
from pygame import gfxdraw
import sys
import math
from OpenGL.GL import * 
from pygame import OPENGLBLIT
from pygame import OPENGL
from OpenGL.GLU import *

def Round(a):
    return int(a + 0.5)

def mainloop():
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def Draw():
    DrawPoly((300, 300), 6, 100)
    FillPoly((300, 300), 6, 100,[255,0,0])
    pygame.display.flip()



def drawDDA(p1, p2, color=[0, 0, 0]):
    x0, y0, x1, y1 = p1[0], p1[1], p2[0], p2[1]
    steps = abs(x0-x1) if abs(x0-x1) > abs(y0-y1) else abs(y0-y1)
    dx = (x1-x0)/steps
    dy = (y1-y0)/steps
    x, y = x0, y0
    gfxdraw.pixel(screen,Round(x),Round(y),color)
    for i in range(int(steps)):
        x += dx
        y += dy
        gfxdraw.pixel(screen,Round(x), Round(y),color)


def DrawPoly(center, n, s, color=[0, 0, 0]):
    x0, y0 = center[0], center[1]
    a = math.radians(360 / n)
    d = s / 2 / math.sin(a / 2)
    pts = []
    bv1x = x0-s/2
    bv1y = y0 - (s/2)*(1/math.tan(math.radians(180/n)))
    bv2x = x0+s/2
    bv2y = bv1y
    for i in range(n+1):
        sideAngle = math.radians((360 * i / n))
        x = (bv1x-x0)*math.cos(sideAngle) + (bv1y-y0) * math.sin(sideAngle)+x0
        y = (bv1x-x0)*math.sin(sideAngle) - (bv1y-y0) * math.cos(sideAngle)+y0
        pts.append([x, y])
    for i in range(n):
        drawDDA(pts[i], pts[i+1], color)

def FillPoly(center, n, s, color=[0, 0, 0]):
    for i in range(1, s):
        DrawPoly(center, n, i, color)


size = [640, 720]
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
Draw()
mainloop()
