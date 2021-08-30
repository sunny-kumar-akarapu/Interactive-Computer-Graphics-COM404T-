from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np

def randomColor():
    color = [i/255 for i in random.choices(range(256), k=3)]
    return color


def DrawPoly(vertices: list, color: list = [1, 0, 0]):
    glBegin(GL_POLYGON)
    glColor3f(color[0] ,color[1], color[2])
    for i in vertices:
        glVertex2f(i[0],i[1])
    glEnd()


def letterI(color):
    glColor3f(0.5, 0, 0.5)
    glLineWidth(2)
    DrawPoly([(110, 325), (110, 300), (190, 300), (190, 325)],color)
    DrawPoly([(140, 300), (140, 150), (160, 150), (160, 300)],color)
    DrawPoly([(110, 150), (110, 125), (190, 125), (190, 150)],color)


def letterC(color):
    glColor3f(0.5, 0, 0)
    glLineWidth(2)
    DrawPoly([(240, 325), (240, 300), (310, 300), (310, 325)],color)
    DrawPoly([(240, 300), (240, 150), (270, 150), (270, 300)],color)
    DrawPoly([(240, 150), (240, 125), (310, 125), (310, 150)],color)
    DrawPoly([(310, 325), (310, 300), (325, 275), (340, 300)],color)
    DrawPoly([(310, 150), (310, 125), (340, 150), (325, 175)],color)


def letterG(color):
    glColor3f(0.5, 0, 0)
    glLineWidth(2)
    DrawPoly([(390, 325), (390, 125), (420, 125), (420, 325)],color)
    DrawPoly([(420, 150), (420, 125), (490, 125), (490, 150)],color)
    DrawPoly([(460, 200), (460, 150), (490, 150), (490, 225), (440, 225)],color)
    DrawPoly([(460, 300), (460, 275), (490, 275), (490, 325), (420, 325), (420, 300)],color)


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    color = randomColor()
    letterI(color)
    color = randomColor()
    letterC(color)
    color = randomColor()
    letterG(color)
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100, 100)
glutInitWindowSize(500, 450)
glutCreateWindow("ICG")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0.0, 600.0, 0.0, 600.0)
glutDisplayFunc(draw)
glutMainLoop()
