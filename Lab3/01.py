from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def DrawPoly(vertices: list, color: list = [1, 0, 0]):
    glBegin(GL_POLYGON)
    glColor3f(color[0], color[1], color[2])
    for i in vertices:
        glVertex2f(i[0], i[1])
    glEnd()


def num0(color):
    glColor3f(0.5, 0, 0.5)
    glLineWidth(2)
    DrawPoly([(110, 325), (110, 300), (190, 300), (190, 325)], color)
    DrawPoly([(135, 300), (135, 150), (110, 150), (110, 300)], color)
    DrawPoly([(190, 300), (190, 150), (165, 150), (165, 300)], color)
    DrawPoly([(110, 150), (110, 125), (190, 125), (190, 150)], color)


def num1(color):
    glColor3f(1, 1, 1)
    glLineWidth(2)
    DrawPoly([(270, 325), (300, 325), (300, 125), (270, 125)], color)
    DrawPoly([(270, 325), (270, 300), (245, 285), (230, 300)], color)


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    color = randomColor()
    num0(color)
    color = randomColor()
    num1(color)
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100, 100)
glutInitWindowSize(500, 450)
glutCreateWindow("01")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0.0, 600.0, 0.0, 600.0)
glutDisplayFunc(draw)
glutMainLoop()
