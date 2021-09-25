from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
import math

xAxisLimits = [-800, 800]
yAxisLimits = [-800, 800]


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]


def randomEllipseRadius():
    return random.randint(0, (xAxisLimits[1]-xAxisLimits[0])/2)


def randomCenter():
    return [i for i in random.choices(range(-150, 150), k=2)]

def randomAngle():
    return random.randint(0,360)

def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawEllipseArc(randomCenter(), randomEllipseRadius(),
                   randomEllipseRadius(), randomAngle(), randomAngle(), randomColor())
    glFlush()



def drawEllipseArc(center, rx, ry, startAngle, endAngle, color):
    cx, cy = center[0], center[1]
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    x = 1
    y = ry
    y_f = floor(y/sqrt(2))-1
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    while dx < dy:
        angle = [0 for i in range(8)]
        alpha = int(90 - (atan(y/x)*180)/math.pi)
        angle[0] = 90 - alpha
        angle[1] = alpha
        angle[2] = 360 - alpha
        angle[3] = 270 + alpha
        angle[4] = 270 - alpha
        angle[5] = 180 + alpha
        angle[6] = 180 - alpha
        angle[7] = 90 + alpha
        if(angle[0] >= startAngle and angle[0] <= endAngle):
            glVertex2i(cx + x, cy + y)
        if(angle[3] >= startAngle and angle[3] <= endAngle):
            glVertex2i(cx + x, cy - y)
        if(angle[4] >= startAngle and angle[4] <= endAngle):
            glVertex2i(cx - x, cy - y)
        if(angle[7] >= startAngle and angle[7] <= endAngle):
            glVertex2i(cx - x, cy + y)
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
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    while y >= 0:
        angle = [0 for i in range(8)]
        alpha = int(90 - (atan(y/x)*180)/math.pi)
        angle[0] = 90 - alpha
        angle[1] = alpha
        angle[2] = 360 - alpha
        angle[3] = 270 + alpha
        angle[4] = 270 - alpha
        angle[5] = 180 + alpha
        angle[6] = 180 - alpha
        angle[7] = 90 + alpha
        if(angle[0] >= startAngle and angle[0] <= endAngle):
            glVertex2i(cx + x, cy + y)
        if(angle[3] >= startAngle and angle[3] <= endAngle):
            glVertex2i(cx + x, cy - y)
        if(angle[4] >= startAngle and angle[4] <= endAngle):
            glVertex2i(cx - x, cy - y)
        if(angle[7] >= startAngle and angle[7] <= endAngle):
            glVertex2i(cx - x, cy + y)
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


def drawArc(c, r, startAngle, endAngle):
    cx, cy = c[0], c[1]
    glColor3ub(0, 0, 0)
    d = 1 - r
    x = 1
    y = r
    y_f = floor(y/sqrt(2)) - 1

    while(y != y_f):
        glBegin(GL_POINTS)
        angle = [0 for i in range(8)]
        alpha = int(90 - (atan(y/x)*180)/math.pi)
        angle[0] = 90 - alpha
        angle[1] = alpha
        angle[2] = 360 - alpha
        angle[3] = 270 + alpha
        angle[4] = 270 - alpha
        angle[5] = 180 + alpha
        angle[6] = 180 - alpha
        angle[7] = 90 + alpha
        if(angle[0] >= startAngle and angle[0] <= endAngle):
            glVertex2i(cx + x, cy + y)
        if(angle[1] >= startAngle and angle[1] <= endAngle):
            glVertex2i(cx + y, cy + x)
        if(angle[2] >= startAngle and angle[2] <= endAngle):
            glVertex2i(cx + y, cy - x)
        if(angle[3] >= startAngle and angle[3] <= endAngle):
            glVertex2i(cx + x, cy - y)
        if(angle[4] >= startAngle and angle[4] <= endAngle):
            glVertex2i(cx - x, cy - y)
        if(angle[5] >= startAngle and angle[5] <= endAngle):
            glVertex2i(cx - y, cy - x)
        if(angle[6] >= startAngle and angle[6] <= endAngle):
            glVertex2i(cx - y, cy + x)
        if(angle[7] >= startAngle and angle[7] <= endAngle):
            glVertex2i(cx - x, cy + y)
        glEnd()
        x = x + 1
        if(d < 0):
            d += (2*x) + 3
        else:
            d += (2*(x-y)) + 5
            y = y - 1


def drawEllipseMED(center, rx, ry, color):
    xc, yc = center[0], center[1]
    x = 0
    y = ry
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
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
glutCreateWindow("Ellipse ARC")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(xAxisLimits[0], xAxisLimits[1], yAxisLimits[0], yAxisLimits[1])
glutDisplayFunc(draw)
glutMainLoop()

