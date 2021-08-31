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
    FillPoly((0, 0), 4, 120, [0.5, 0.8, 0.9])
    DrawPoly((0, 0), 4, 120)
    FillPoly((0, 60*(3**(0.4))), 3, 120,[1,0,0])
    DrawPoly((0, 60*(3**(0.4))), 3, 120)
    FillPoly((-30, 0), 4, 20, [1, 1, 1])
    DrawPoly((-30, 0), 4, 20)
    FillPoly((30, 0), 4, 20, [1, 1, 1])
    DrawPoly((30, 0), 4, 20)
    FillRectangle(0, -25, 20, 70,color = [1,1,1])
    DrawRectangle(0, -25, 20, 70)
    glFlush()


def drawDDA(p1, p2, color=[0, 0, 0]):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    x, y = x1, y1
    length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    print(dx,dy)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2i(ROUND(x), ROUND(y))
    for i in range(int(length)):
        x += dx
        y += dy
        glVertex2i(ROUND(x), ROUND(y))
    glEnd()


def DrawPoly(center, n, s, color=[0, 0, 0]):
    glPointSize(5)
    glColor3f(color[0], color[1], color[2])
    glTranslatef(center[0], center[1], 0)
    cx, cy = 0, 0
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
    glRotatef(sideAngle, 0, 0, 1)
    glTranslatef(-center[0], -center[1], 0)


def FillPoly(center, n, s, color=[0, 0, 0]):
    glPointSize(5)
    for i in range(1, s):
        DrawPoly(center, n, i, color)


def DrawRectangle(h: float, k: float, length: float, breadth: float, color=[0, 0, 0]):
    glPointSize(5)
    glColor3f(color[0], color[1], color[2])
    l = length/2
    b = breadth/2
    drawDDA((h + l, k+b), (h + l, k-b),color)
    drawDDA((h + l, k-b), (h - l, k-b),color)
    drawDDA((h - l, k+b), (h - l, k-b),color)
    drawDDA((h - l, k+b), (h + l, k+b),color)


def FillRectangle(h, k, length, breadth, color=[0, 0, 0]):
    glPointSize(5)
    l, b = 1, 1
    for i in range(1, max(length,breadth)):
        DrawRectangle(h,k,l,b,color)
        if l<length:
            l+=1
        if b<breadth:
            b+=1        


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("DDA House")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()
