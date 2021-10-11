from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def ROUND(a):
    return int(a + 0.5)


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)

    drawHyperbolaMidPoint((-80, 0), 120, 100, 200, [1, 0, 0])
    drawHyperbolaGeneral((-30, 0), 120, 100, 200)

    drawHyperbolaParametric((20, 0), 120, 100, 200,[0,1,0])
    glFlush()


def hyperbolaGeneralY(a, b, x):
    return ((x*x - a*a)**0.5)*(b/a)


def drawHyperbolaGeneral(c, a, b, limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for x in range(limitX+1):
        try:
            glVertex2i(x0 + x, int(y0 + hyperbolaGeneralY(a, b, x)))
            glVertex2i(x0 + x, int(y0 - hyperbolaGeneralY(a, b, x)))
            glVertex2i(x0 - x, int(y0 + hyperbolaGeneralY(a, b, x)))
            glVertex2i(x0 - x, int(y0 - hyperbolaGeneralY(a, b, x)))
        except:
            pass
    glEnd()


def parabolaParaY(a, t):
    return 2*a*t


def parabolaParaX(a, t):
    return 2*a*t


def drawHyperbolaParametric(c, a, b,limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    values = [radians(i) for i in range(0,360)]
    for t in values:
        glVertex2i(int(x0 + (a/cos(t))), int(y0 + b*tan(t)))
        # glVertex2i(x0 + (a/cos(t)), y0 + b*tan(t))
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



def drawHyperbolaMidPoint(c, a, b, limitX, color=[0, 0, 0]):
    x0, y0 = c[0], c[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    p = (((a+0.5)**2)/(a*a)) - (1/(b*b)) - 1
    x = a
    y = 0
    while x <= (a*a) / (((a*a)-(b*b))**0.5):
        if p <= 0:
            p += (2*x / (a*a))
            x += 1
        p -= (1+2*y)/(b*b)
        y += 1
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 + x, y0 - y)
        glVertex2i(x0 - x, y0 - y)
        glVertex2i(x0 - x, y0 + y)
        if x >= limitX:
            break
    p = (((x+1)**2)/(a*a)) - (((y+0.25)**2)/(b*b)) - 1
    while x < limitX:
        if p >= 0:
            y += 1
            p -= (2*y)/(b*b)
        x += 1
        p += (2*x + 1)/(a*a)
        glVertex2i(x0 + x, y0 + y)
        glVertex2i(x0 + x, y0 - y)
        glVertex2i(x0 - x, y0 - y)
        glVertex2i(x0 - x, y0 + y)
    glEnd()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Hyperbola")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()
