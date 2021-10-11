from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

xAxisLimits = [-300, 300]
yAxisLimits = [-300, 300]


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def ROUND(a):
    return int(a + 0.5)


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def randomParabolaFocalLen():
    return random.randint(0, (xAxisLimits[1]-xAxisLimits[0])/2)


def randomCenter():
    return [i for i in random.choices(range(-150, 150), k=2)]

def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)
    drawParabolaMidPoint((0, 0), 10, 200, [1, 0, 0])
    drawParabolaMidPointVertical((0, 50), 10, 200, [1, 0, 0])
    drawParabolaGeneral((-50, 0), 10, 200,[0,1,0])
    drawParabolaGeneralVertical((-50, 50), 10, 200,[0,1,0])
    drawParabolaParametric((50, 0), 10, 200, [0, 1, 1])
    drawParabolaParametricVertical((50, 50), 10, 200, [0, 1, 1])
    glFlush()


def parabolaParaY(a, t):
    return 2*a*t


def parabolaParaX(a, t):
    return 2*a*t


def drawParabolaParametric(c, a, limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for x in range(limitX):
        glVertex2i(x0 + x, int(y0 + parabolaParaY(a, (x/a)**0.5)))
        glVertex2i(x0 + x, int(y0 - parabolaParaY(a, (x/a)**0.5)))
    glEnd()


def drawParabolaParametricVertical(c, a, limitY, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for y in range(limitY):
        glVertex2i(int(x0 + parabolaParaX(a, (y/a)**0.5)), y0 + y)
        glVertex2i(int(x0 - parabolaParaX(a, (y/a)**0.5)), y0 + y)
    glEnd()


def parabolaGeneralY(a, x):
    return (4*a*x)**0.5


def parabolaGeneralX(a, y):
    return (4*a*y)**0.5


def drawParabolaGeneral(c, a, limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for x in range(limitX+1):
        glVertex2i(x0 + x, int(y0 + parabolaGeneralY(a, x)))
        glVertex2i(x0 + x, int(y0 - parabolaGeneralY(a, x)))
    glEnd()


def drawParabolaGeneralVertical(c, a, limitY, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for y in range(limitY+1):
        glVertex2i(int(x0 + parabolaGeneralX(a, y)), y0 + y)
        glVertex2i(int(x0 - parabolaGeneralX(a, y)), y0 + y)
    glEnd()


def drawParabolaMidPointVertical(c, a, limitY, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    p = 1 - 2*a
    x = 0
    y = 0
    while 2*a >= x:
        if p >= 0:
            y += 1
            p -= 4*a
        x += 1
        p += 3+2*x
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 - x, y0 + y)
        if y >= limitY:
            break
    p = (x+0.5)**2 - 4*a*(y+1)
    while y < limitY:
        if p < 0:
            x += 1
            p += 2*x
        y += 1
        p -= 4*a
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 - x, y0 + y)
    glEnd()

def drawParabolaMidPoint(c, a, limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    p = 1 - 2*a
    x = 0
    y = 0
    while 2*a >= y:
        if p >= 0:
            x += 1
            p -= 4*a
        y += 1
        p += 1+2*y
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 + x, y0 - y)
        if x >= limitX:
            break
    p = (y+0.5)**2 - 4*a*(x+1)
    while x < limitX:
        if p < 0:
            y += 1
            p += 2*y
        x += 1
        p -= 4*a
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 + x, y0 - y)
    glEnd()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Parabola")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()
