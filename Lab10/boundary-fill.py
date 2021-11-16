from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

# include <GL/glut.h>
ww = 600
wh = 500
fillCol = [0.0, 1.0, 1.0]
borderCol = [0.0, 0.0, 0.0]

def setPixel(pointx, pointy, f):
    glBegin(GL_POINTS)
    glColor3fv(f)
    glVertex2i(pointx, pointy)
    glEnd()
    glFlush()

def getPixel( x, y):
    return glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
  

def drawLine(p1, p2, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glEnd()

def drawRectangle(xmin,xmax,ymin,ymax,color=[0,0,0]):
    glColor3f(color[0], color[1], color[2])
    drawLine((xmin,ymin-10),(xmin,ymax+10),color)
    drawLine((xmin-10,ymax),(xmax+10,ymax),color)
    drawLine((xmax, ymax+10), (xmax, ymin-10), color)
    drawLine((xmin-10, ymin), (xmax+10, ymin), color)

    
def drawPoly(center, n, s, color=[0, 0, 0]):
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
    drawLine((bv1x, bv1y), (bv2x, bv2y), color)
    for i in range(n-1):
        glRotatef(sideAngle, 0, 0, 1)
        drawLine((bv1x, bv1y), (bv2x, bv2y), color)
    glRotatef(sideAngle, 0, 0, 1)
    glTranslatef(-center[0], -center[1], 0)


def display():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    # drawPoly((50,50),4,40,[0,0,0])
    drawRectangle(50,100,50,100)
    glFlush()


def boundaryFill4(x, y, fillColor, borderColor):
    interiorColor= getPixel(x, y)
    # print(interiorColor)
    interiorColor = list(np.frombuffer(interiorColor, np.float32))
    print("interiorColor:",interiorColor)
    if ((interiorColor != borderColor) and (interiorColor != fillColor)):
        setPixel(x, y, fillColor)
        print("workingggggggggggg")
        boundaryFill4(x + 1, y, fillColor, borderColor)
        boundaryFill4(x - 1, y, fillColor, borderColor)
        boundaryFill4(x, y + 1, fillColor, borderColor)
        boundaryFill4(x, y - 1, fillColor, borderColor)
    

def boundaryFill8(x, y, fillColor, borderColor):
    interiorColor = getPixel(x, y)
    # print(interiorColor)
    interiorColor = list(np.frombuffer(interiorColor, np.float32))
    print("interiorColor:", interiorColor)
    if ((interiorColor != borderColor) and (interiorColor != fillColor)):
        setPixel(x, y, fillColor)
        print("workingggggggggggg")
        boundaryFill8(x + 1, y, fillColor, borderColor)
        boundaryFill8(x - 1, y, fillColor, borderColor)
        boundaryFill8(x, y + 1, fillColor, borderColor)
        boundaryFill8(x, y - 1, fillColor, borderColor)
        boundaryFill8(x+1, y - 1, fillColor, borderColor)
        boundaryFill8(x+1, y + 1, fillColor, borderColor)
        boundaryFill8(x-1, y - 1, fillColor, borderColor)
        boundaryFill8(x-1, y + 1, fillColor, borderColor)


def mouse(btn, state, x, y):
    if (btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        xi = x
        yi = (wh - y)
        boundaryFill4(xi, yi, fillCol, borderCol)
    elif (btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN):
        xi = x
        yi = (wh - y)
        boundaryFill8(xi, yi, fillCol, borderCol)

def myinit():
    glViewport(0, 0, ww, wh)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, ww, 0.0, wh)
    glMatrixMode(GL_MODELVIEW)


# def main(int argc, char ** argv):
glutInit(sys.argv)
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(ww, wh)
glutCreateWindow("Boundary-Fill-Recursive")
glutDisplayFunc(display)
myinit()
glutMouseFunc(mouse)
glutMainLoop()

