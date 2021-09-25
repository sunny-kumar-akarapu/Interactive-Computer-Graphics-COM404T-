from math import *
import math
import sys
import random
import time
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

gray = [i/255 for i in [169, 169, 169]]


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)
    drawArc((0, 0), 100, 210, 270)
    glFlush()


def drawArc(c, r, startAngle, endAngle):
    cx, cy = c[0], c[1]
    glColor3ub(0, 0, 0)
    d = 1 - r
    x = 1
    y = r
    y_f = floor(y/sqrt(2)) - 1

    while(y != y_f):
        glBegin(GL_POINTS)
        angle = [0 for i in range(8)]
        alpha = int(90 - (atan(y/x)*180)/math.pi)
        angle[0] = 90 - alpha
        angle[1] = alpha
        angle[2] = 360 - alpha
        angle[3] = 270 + alpha
        angle[4] = 270 - alpha
        angle[5] = 180 + alpha
        angle[6] = 180 - alpha
        angle[7] = 90 + alpha
        if(angle[0] >= startAngle and angle[0] <= endAngle):
            glVertex2i(cx + x, cy + y)
        if(angle[1] >= startAngle and angle[1] <= endAngle):
            glVertex2i(cx + y, cy + x)
        if(angle[2] >= startAngle and angle[2] <= endAngle):
            glVertex2i(cx + y, cy - x)
        if(angle[3] >= startAngle and angle[3] <= endAngle):
            glVertex2i(cx + x, cy - y)
        if(angle[4] >= startAngle and angle[4] <= endAngle):
            glVertex2i(cx - x, cy - y)
        if(angle[5] >= startAngle and angle[5] <= endAngle):
            glVertex2i(cx - y, cy - x)
        if(angle[6] >= startAngle and angle[6] <= endAngle):
            glVertex2i(cx - y, cy + x)
        if(angle[7] >= startAngle and angle[7] <= endAngle):
            glVertex2i(cx - x, cy + y)
        glEnd()
        x = x + 1
        if(d < 0):
            d += (2*x) + 3
        else:
            d += (2*(x-y)) + 5
            y = y - 1


def drawCircle(c, radius, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    p = 1 - radius
    df_x = 1
    df_y = -2 * radius
    x = 0
    y = radius
    glVertex2i(x0, y0 + radius)
    glVertex2i(x0, y0 - radius)
    glVertex2i(x0 + radius, y0)
    glVertex2i(x0 - radius, y0)

    while x < y:
        if p >= 0:
            y -= 1
            df_y += 2
            p += df_y
        x += 1
        df_x += 2
        p += df_x
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 - x, y0 + y)
        glVertex2i(x0 + x, y0 - y)
        glVertex2i(x0 - x, y0 - y)
        glVertex2i(x0 + y, y0 + x)
        glVertex2i(x0 - y, y0 + x)
        glVertex2i(x0 + y, y0 - x)
        glVertex2i(x0 - y, y0 - x)
    glEnd()


def fillCircle(c, radius, color=[0, 0, 0]):
    for i in range(radius):
        drawCircle(c, i, color)


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def ROUND(a):
    return int(a + 0.5)


def findY(p1, slope, x):
    x1, y1 = p1[0], p1[1]
    return ((slope)*(x-x1))+y1


def drawBresenham(p1, p2, color=[0, 0, 0]):
    glPointSize(3)
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
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    pts = []
    error = 0
    for x in range(dx + 1):
        x_ = x0 + x*xx + y*yx
        y_ = y0 + x*xy + y*yy
        glVertex2i(x_, y_)
        pts.append((x_, y_))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    glEnd()


def drawDDA(p1, p2, color=[0, 0, 0]):
    glPointSize(3)
    x1, y1, x2, y2 = round(p1[0], 1), round(
        p1[1], 1), round(p2[0], 1), round(p2[1], 1)
    x, y = x1, y1
    length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    pts = []
    dx, dy = round(dx, 1), round(dy, 1)
    for i in range(int(length+1)):
        pts.append((ROUND(x), ROUND(y)))
        glVertex2i(ROUND(x), ROUND(y))
        x += dx
        y += dy
    glEnd()


def DrawIrPoly(vertices: list, color: list = [0, 0, 0], algo="DDA"):
    glColor3f(color[0], color[1], color[2])
    for i in range(len(vertices)-1):
        eval("draw"+algo+"(vertices[i], vertices[i+1], color)")
    eval("draw"+algo+"(vertices[-1], vertices[0], color)")


def drawPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
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
        x = (bv1x-x0)*math.cos(sideAngle) - (bv1y-y0) * math.sin(sideAngle)+x0
        y = (bv1x-x0)*math.sin(sideAngle) + (bv1y-y0) * math.cos(sideAngle)+y0
        pts.append([x, y])
    for i in range(n):
        eval("draw"+algo+"(pts[i], pts[i+1], color)")


def FillPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
    glPointSize(5)
    for i in range(1, s):
        drawPoly(center, n, i, color, algo)


def drawRectangle(h: float, k: float, length: float, breadth: float, color=[0, 0, 0], algo="DDA"):
    glPointSize(3)
    glColor3f(color[0], color[1], color[2])
    l = length/2
    b = breadth/2
    eval("draw"+algo+"((h + l, k+b), (h + l, k-b), color)")
    eval("draw"+algo+"((h - l, k-b), (h + l, k-b), color)")
    eval("draw"+algo+"((h - l, k-b), (h - l, k+b), color)")
    eval("draw"+algo+"((h - l, k+b), (h + l, k+b), color)")


def FillRectangle(h, k, length, breadth, color=[0, 0, 0], algo="DDA"):
    glPointSize(5)
    l, b = 1, 1
    for i in range(1, max(length, breadth)):
        drawRectangle(h, k, l, b, color)
        if l < length:
            l += 1
        if b < breadth:
            b += 1


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("DDA Car")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()
