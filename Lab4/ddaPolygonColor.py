from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
import math


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def ROUND(a):
    return int(a + 0.5)


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)
    FillPoly((0,0), 7, 100,[1,1,0])
    DrawPoly((0, 0), 7, 100)
    glFlush()


def drawDDA(p1, p2, color=[0, 0, 0]):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    x, y = x1, y1
    length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2i(ROUND(x), ROUND(y))
    for i in range(int(length)):
        x += dx
        y += dy
        glVertex2i(ROUND(x), ROUND(y))
    glEnd()


def DrawPoly(center, n, s, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    cx, cy = center[0], center[1]
    sideAngle = 360/n
    sideAngleH = sideAngle/2
    sideAngleHRadians = math.radians(sideAngleH)
    bv1x = cx-s/2
    bv1y = cy - (s/2)*(1/math.tan(sideAngleHRadians))
    bv2x = cx+s/2
    bv2y = bv1y
    drawDDA((bv1x, bv1y), (bv2x, bv2y), color)
    for i in range(n-1):
        glRotatef(sideAngle, 0, 0, 1)
        drawDDA((bv1x, bv1y), (bv2x, bv2y), color)

def FillPoly(center,n,s,color=[0,0,0]):
    for i in range(1,s):
        DrawPoly(center,n,i,color)
    

def DrawEquiTriangle(leftbaseVertex, side, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    x, y = leftbaseVertex[0], leftbaseVertex[1]
    drawDDA((x, y), (x+side, y))
    drawDDA((x+side/2, y+(side*(3**0.5))/2), (x+side, y))
    drawDDA((x, y), (x+side/2, y+(side*(3**0.5))/2))


def DrawRectangle(h: float, k: float, length: float, breadth: float, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    l = length/2
    b = breadth/2
    drawDDA((h + l, k+b), (h + l, k-b))
    drawDDA((h + l, k-b), (h - l, k-b))
    drawDDA((h - l, k+b), (h - l, k-b))
    drawDDA((h - l, k+b), (h + l, k+b))


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("DDA hexagon")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()
