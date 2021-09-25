from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
import math


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def generalEllipseY(center, rx, ry, x):
    cal = (ry/rx)*(((rx)**2-(center[0]-x)**2)**0.5)
    return [center[1] + cal, center[1]-cal]


def generalEllipseX(center, rx, ry, y):
    cal = (rx/ry)*(((ry)**2-(center[1]-y)**2)**0.5)
    return [center[0] + cal, center[0]-cal]


def EllipseParaX(center, rx, ry, theta):
    return int(center[0] + rx * cos(theta))


def EllipseParaY(center, rx, ry, theta):
    return int(center[1]+ry*sin(theta))


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawEllipseGeneral((-100, 0), 160, 100, [0, 0, 0])
    drawEllipseParametric((-100, 0), 100, 160, [0, 0, 0])
    drawEllipseMED((180, 0), 100, 160, [0, 0, 0])
    glFlush()


def drawEllipseGeneral(center, xL, yL, color):
    glColor3f(color[0], color[1], color[2])
    cx, cy = center[0], center[1]
    glBegin(GL_POINTS)
    if xL >= yL:
        for i in range(cx-xL, int(cx+xL)+1):
            l = generalEllipseY(center, xL, yL, i)
            glVertex2i(i, int(l[0]))
            glVertex2i(i, int(l[1]))
    else:
        for i in range(cy-yL, int(cy+yL)+1):
            l = generalEllipseX(center, xL, yL, i)
            glVertex2i(int(l[0]), i)
            glVertex2i(int(l[1]), i)
    glEnd()


def drawEllipseParametric(center, xL, yL, color):
    glColor3f(color[0], color[1], color[2])
    cx, cy = center[0], center[1]
    glBegin(GL_POINTS)
    p = max(4*xL-4, 4*yL-4)
    stepSize = (2*pi) / p
    theta = 0
    while theta <= 2*pi:
        glVertex2i(EllipseParaX(center, xL, yL, theta),
                   EllipseParaY(center, xL, yL, theta))
        theta += stepSize
    glEnd()


def EllipseSlope(x, y, rx, ry):
    return -(ry**2/rx**2)*(x/y)


def drawEllipseMED(center, rx, ry, color):
    xc, yc = center[0], center[1]
    x = 0
    y = ry
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +(0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    # For region 1
    while (dx < dy):
        # Print points based on 4-way symmetry
        glVertex2i(int(x+xc), int(y+yc))
        glVertex2i(int(-x+xc), int(y+yc))
        glVertex2i(int(x+xc), int(-y+yc))
        glVertex2i(int(-x+xc), int(-y+yc))
        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    # Plotting points of region 2
    while (y >= 0):
        # printing points based on 4-way symmetry
        glVertex2i(int(x+xc), int(y+yc))
        glVertex2i(int(-x+xc), int(y+yc))
        glVertex2i(int(x+xc), int(-y+yc))
        glVertex2i(int(-x+xc), int(-y+yc))
        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)
    glEnd()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Ellipse")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
glutDisplayFunc(draw)
glutMainLoop()


print(LinesBresenham)
print(LinesDDA)
