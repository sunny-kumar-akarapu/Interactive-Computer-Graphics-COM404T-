from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# xMin, xMax, yMin, yMax = map(int, input().split())
x_min, x_max, y_min, y_max = -100,100,-100,100

xAxisLimits = [x_min-200, x_max+200]
yAxisLimits = [y_min-200, y_max+200]

def drawViewingWindow(color=[1, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex2i(int(x_min), int(y_min))
    glVertex2i(int(x_min), int(y_max))
    glVertex2i(int(x_max), int(y_min))
    glVertex2i(int(x_max), int(y_max))
    glVertex2i(int(x_min), int(y_max))
    glVertex2i(int(x_max), int(y_max))
    glVertex2i(int(x_min), int(y_min))
    glVertex2i(int(x_max), int(y_min))
    glEnd()


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)
    drawViewingWindow()
    plotClippedPoints([(0, 0),(100,100),(10,20),(20,10),(-20,-10),(120,120),(-120,-120),(-40,-10)], [0, 0, 0])
    glFlush()


def plotClippedPoints(listOfPoints, color=[0, 0, 0]):
    # glPointSize(10)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for pt in listOfPoints:
        x, y = pt[0], pt[1]
        if x_min <= x <= x_max and y_min <= y <= y_max:
            glVertex2i(int(x), int(y))
    glEnd()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Point Clipping")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)

gluOrtho2D(xAxisLimits[0], xAxisLimits[1], yAxisLimits[0], yAxisLimits[1])
glutDisplayFunc(draw)
glutMainLoop()
