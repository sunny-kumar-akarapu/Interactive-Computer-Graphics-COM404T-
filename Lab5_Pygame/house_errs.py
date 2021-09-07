import os
import pygame
from pygame import gfxdraw
import sys
import math
from pygame import OPENGLBLIT
from pygame import OPENGL
import random


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def Round(a):
    return int(a + 0.5)


def findY(p1, slope, x):
    x1, y1 = p1[0], p1[1]
    return ((slope)*(x-x1))+y1


def ErrorCal(p1, p2, pts):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    try:
        slope = (y1-y2)/(x1-x2)
        ans = 0
        for i in pts:
            ans += (findY(p1, slope, i[0])-i[1])**2
        return ans/len(pts)
    except:
        return 0


def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Draw():
    Errors_DDA = 0
    Errors_BRE = 0
    Errors_DDA += DrawPoly((300, 200), 3, 120)
    Errors_BRE += DrawPoly((300, 200), 3, 120, algo="Bresenham")
    Errors_DDA += DrawPoly((300, 295), 4, 120)
    Errors_BRE += DrawPoly((300, 295), 4, 120, algo="Bresenham")
    Errors_DDA += DrawPoly((270, 295), 4, 20)
    Errors_BRE += DrawPoly((270, 295), 4, 20, algo="Bresenham")
    Errors_DDA += DrawPoly((330, 295), 4, 20)
    Errors_BRE += DrawPoly((330, 295), 4, 20, algo="Bresenham")
    Errors_DDA += DrawRectangle(300, 320, 20, 70)
    Errors_BRE += DrawRectangle(300, 320, 20, 70, algo="Bresenham")
    # Errors_DDA += drawDDA((0, 0), (200, 220))
    # Errors_BRE += drawBresenham((0, 0), (200, 220))
    print("Errors_DDA", Errors_DDA)
    print("Errors_BRE", Errors_BRE)
    pygame.display.update()


def drawDDA(p1, p2, color=[0, 0, 0]):
    pts = []
    x0, y0, x1, y1 = p1[0], p1[1], p2[0], p2[1]
    steps = abs(x0-x1) if abs(x0-x1) > abs(y0-y1) else abs(y0-y1)
    dx = (x1-x0)/float(steps)
    dy = (y1-y0)/float(steps)
    x, y = x0, y0
    dx, dy = round(dx, 1), round(dy, 1)
    for i in range(int(steps)):
        pts.append((Round(x), Round(y)))
        gfxdraw.pixel(screen, Round(x), Round(y), color)
        x += dx
        y += dy
    # print(len(pts))
    # print(pts)
    return ErrorCal(p1, p2, pts)


def drawBresenham(p1, p2, color=[0, 0, 0]):
    pts = []
    x0, y0, x1, y1 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    pts = []
    error = 0
    for x in range(dx + 1):
        x_ = x0 + x*xx + y*yx
        y_ = y0 + x*xy + y*yy
        gfxdraw.pixel(screen, x_, y_, color)
        pts.append((x_, y_))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    # print(len(pts))
    return ErrorCal((x0, y0), (x1, y1), pts)


def DrawPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
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
    errors = []
    for i in range(n):
        errors.append(eval("draw"+algo+"(pts[i], pts[i+1], color)"))
    print(algo[0:3], "\tsides:", n, "\tlength", s, "\t", sum(errors))
    return sum(errors)


def FillPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
    errors = []
    for i in range(1, s):
        errors.append(DrawPoly(center, n, i, color, algo))
    # print(algo[0:3], "\tsides:", n, "\tlength", s, "\t", sum(errors))
    return sum(errors)


def DrawRectangle(h: float, k: float, length: float, breadth: float, color=[0, 0, 0], algo="DDA"):
    l = length/2
    b = breadth/2
    errors = []
    errors.append(eval("draw"+algo+"((h + l, k+b), (h + l, k-b), color)"))
    errors.append(eval("draw"+algo+"((h + l, k-b), (h - l, k-b), color)"))
    errors.append(eval("draw"+algo+"((h - l, k+b), (h - l, k-b), color)"))
    errors.append(eval("draw"+algo+"((h - l, k+b), (h + l, k+b), color)"))
    print(algo[0:3], "\tsides:", 4, "\tlength", length,
          "\tbreadth", breadth, "\t", sum(errors))
    return sum(errors)


def FillRectangle(h, k, length, breadth, color=[0, 0, 0], algo="DDA"):
    l, b = 1, 1
    errors = []
    for i in range(1, max(length, breadth)):
        errors.append(DrawRectangle(h, k, l, b, color, algo))
        if l < length:
            l += 1
        if b < breadth:
            b += 1
    print(algo[0:3], "\tsides:", 4, "\tlength", length,"\tbreadth", breadth, "\t", sum(errors))
    return sum(errors)


size = [640, 720]
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
Draw()
mainloop()

# errors
