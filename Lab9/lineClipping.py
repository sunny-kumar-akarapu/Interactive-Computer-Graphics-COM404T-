from math import *
import math
import sys
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# xMin, xMax, yMin, yMax = map(int, input().split())
x_min, x_max, y_min, y_max = 0, 9, 1, 7

xAxisLimits = [x_min-10, x_max+10]
yAxisLimits = [y_min-10, y_max+10]

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

p = [0]*4
q = [0]*4
r = [0]*4


def computeCode(x, y):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT   # **01
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT  # **10
    if y < y_min:      # below the rectangle
        code |= BOTTOM  # 01**
    elif y > y_max:    # above the rectangle
        code |= TOP    # 10**

    return code


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
    listOfLines = [[(1, 8), (1, 4)], [(1, 1), (3, 7)], [(4, 4), (6, 5)], [(2, 10), (8, 9)], [(8, 10), (10, 8)], [(0, 9), (3, 9)], [
        (7, 6), (10, 6)], [(3, 5), (9, 8)], [(-1, 4), (5, 9)], [(4, 2), (10, 5)], [(3, 1), (6, 0)], [(-3, 2), (2, -2)], [(8, 3), (8, 0)]]
    drawClippedLines(listOfLines, color=[0, 1, 0])
    drawClippedLines(listOfLines, color=[0, 0, 1], algo="liang_barsky")
    glFlush()


def liang_barsky(p1, p2, color=[0, 0, 0]):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    dx = x2-x1
    dy = y2-y1
    p = [-dx, dx, -dy, dy]
    q = [x1-x_min, x_max-x1, y1-y_min, y_max-y1]
    u1List = [0]
    u2List = [1]
    for i in range(4):
        if p[i] < 0:
            u1List.append(q[i]/p[i])
        elif p[i] > 0:
            u2List.append(q[i]/p[i])
        if p[i] == 0 and q[i] < 0:
            return
    u1 = max(u1List)
    u2 = min(u2List)
    pts = []
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINES)
    if u1 > u2:
        pass
    else:
        for u in u1, u2:
            pts.append([x1+u*dx, y1+u*dy])
            glVertex2i(int(x1+u*dx), int(y1+u*dy))
    glEnd()


def cohenSutherlandClip(p1, p2, color=[0, 0, 0]):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break
        # Some segment lies within the rectangle
        else:
            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:
                x = x1 + (x2 - x1) * \
                    (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * \
                    (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * \
                    (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * \
                    (x_min - x1) / (x2 - x1)
                x = x_min
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        print([int(x1), int(y1)], [int(x2), int(y2)])
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_LINES)
        glVertex2i(int(x1), int(y1))
        glVertex2i(int(x2), int(y2))
        glEnd()
        return [(x1, y1), (x2, y2)]
    else:
        print("Line rejected")
        return -1


def drawClippedLines(listOfLines, color=[0, 0, 0], algo="cohenSutherlandClip"):
    # glPointSize(10)
    for line in listOfLines:
        eval(algo+"(["+str(line[0][0])+"," + str(line[0][1])+"],[" +
             str(line[1][0])+"," + str(line[1][1])+"],"+str(color)+")")


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Line Clipping")
glClearColor(1, 1, 1, 0)
glMatrixMode(GL_PROJECTION)

gluOrtho2D(xAxisLimits[0], xAxisLimits[1], yAxisLimits[0], yAxisLimits[1])
glutDisplayFunc(draw)
glutMainLoop()
