from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# xMin, xMax, yMin, yMax = map(int, input().split())
x_min, x_max, y_min, y_max = -100, 100, -100, 100

xAxisLimits = [x_min-100, x_max+100]
yAxisLimits = [y_min-100, y_max+100]


def randomPoint():
    return [random.choices(range(x_min, x_max), k=1)[0], random.choices(range(y_min, y_max), k=1)[0]]



def drawLine(p1,p2,color=[0,0,0]):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glEnd()


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

def drawHexagon(c,s,color=[0,0,0]):
    glColor3f(color[0], color[1], color[2])
    h,k = c[0],c[1]
    rad30 = radians(30)
    vertices = [(h, k-s), (h+s*cos(rad30), k-s*sin(rad30)),
                (h+s*cos(rad30), k+s*sin(rad30)),(h,k+s),(h-s*cos(rad30),k+s*sin(rad30)),(h-s*cos(rad30),k-s*sin(rad30)),(h,k-s)]
    glBegin(GL_LINES)
    for i in range(len(vertices)-1):
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[i+1][0], vertices[i+1][1])
    glEnd()
    return vertices

def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # polygonWinVertices = DrawPoly([(0,0),(100,0),(50,50)])
    polygonWinVertices = drawHexagon((0,0),100)
    print(polygonWinVertices)
    plotClippedPoints(polygonWinVertices,[(-40,-50),(-40,-100)],color=[1,0,0])
    # drawLine((0, 0), (100, 120))
    glFlush()

def DrawPoly(vertices: list, color: list = [1, 0, 0]):
    glBegin(GL_POLYGON)
    glColor3f(color[0] ,color[1], color[2])
    for i in vertices:
        glVertex2f(i[0],i[1])
    glEnd()
    return vertices

def plotClippedPoints(V,listOfPoints, color=[0, 0, 0]):
    glPointSize(3)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for p in listOfPoints:
        x, y = p[0], p[1]
        flag = 1
        for i in range(len(V)-1):
            p1 = V[i]
            p2 = V[i+1]
            p1p2 = (p2[0]-p1[0],p2[1]-p1[1])
            p1p = (x-p1[0],y-p1[1])
            pro = p1p2[0]*p1p[1] - p1p2[1]*p1p[0]
            if pro<0:
                flag = 0                   
                break
        if flag ==1:
            glVertex2f(x, y)
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
