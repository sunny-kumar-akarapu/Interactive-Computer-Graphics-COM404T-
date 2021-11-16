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


def drawLine(p1, p2, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glEnd()

def drawLines(listOfLines,color=[0,0,0]):
    for line in listOfLines:
        drawLine(line[0],line[1],color)

def drawPolyWithPts(l,color=[0,0,0]):
    for i in range(len(l)):
        drawLine(l[i-1],l[i],color)

def drawViewingWindow(color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    vertices = []
    vertices.append((int(x_min), int(y_min)))
    vertices.append((int(x_max), int(y_min)))
    vertices.append((int(x_max), int(y_max)))
    vertices.append((int(x_min), int(y_max)))
    return vertices


def drawHexagon(c, s, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    h, k = c[0], c[1]
    rad30 = radians(30)
    vertices = [(h, k-s), (h+s*cos(rad30), k-s*sin(rad30)),
                (h+s*cos(rad30), k+s*sin(rad30)), (h, k+s), (h-s*cos(rad30), k+s*sin(rad30)), (h-s*cos(rad30), k-s*sin(rad30)), (h, k-s)]
    return vertices


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    polygonWinVertices = drawHexagon((55, 60), 100)
    drawPolyWithPts(polygonWinVertices,[0,0,0])
    rectangleVertices = drawViewingWindow()
    drawPolyWithPts(rectangleVertices, [0, 0, 0])

    sutherlandHodgmanCliping(polygonWinVertices,rectangleVertices, color=[1,0,0])
    glFlush()


def DrawPoly(vertices: list, color: list = [0, 0, 0]):
    glBegin(GL_POLYGON)
    glColor3f(color[0], color[1], color[2])
    for i in vertices:
        glVertex2f(i[0], i[1])
    glEnd()


def sutherlandHodgmanCliping(P, Q, color=[0, 0, 0]):
    glColor3f(color[0], color[1], color[2])
    fv = []
    # for j in range(len(Q)):
    for j in range(len(Q)):
        if fv!=[]:
            P = fv
            fv =[]
        e1 = Q[j-1]
        e2 = Q[j]
        for i in range(len(P)):
            p1 = P[i-1]
            p2 = P[i]
            # print(p1, p2)
            c1 = inOutCheck(p1, [e1, e2])
            c2 = inOutCheck(p2, [e1, e2])
            if c1==1 and c2==1:
                fv.append(p1)
                fv.append(p2)
            elif c1 == 1 and c2 == 0:
                # intersection pt on "I" between the extended edge E and the line segment p1p2
                # output "I"
                h = x_intersect(p1, p2, e1, e2)
                k = y_intersect(p1, p2, e1, e2)
                fv.append((h,k))
            elif c1 == 0 and c2 == 1:
                # the intersection point I between the extended edge E and the line segment p1p2
                # output "I" and "p2"
                h = x_intersect(p1, p2, e1, e2)
                k = y_intersect(p1, p2, e1, e2)
                fv.append((h,k))
                fv.append(p2)
            elif c1==0 and c2==0:
                # fv.append(p1)
                # fv.append(p2)
                pass
    print("fv",fv)  
    drawPolyWithPts(fv,color)
    


def x_intersect(p1, p2, e1, e2):
    x1, y1, x2, y2, x3, y3,  x4, y4 = p1[0], p1[1], p2[0], p2[1], e1[0], e1[1], e2[0], e2[1]
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den


def y_intersect(p1, p2, e1, e2):
    x1, y1, x2, y2, x3, y3,  x4, y4 = p1[0], p1[1], p2[0], p2[1], e1[0], e1[1], e2[0], e2[1]
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

def inOutCheck(p, V):
    x, y = p[0], p[1]
    for i in range(len(V)-1):
        p1 = V[i]
        p2 = V[i+1]
        p1p2 = (p2[0]-p1[0], p2[1]-p1[1])
        p1p = (x-p1[0], y-p1[1])
        pro = p1p2[0]*p1p[1] - p1p2[1]*p1p[0]
        if pro <= 0:
            return 0
    return 1


def plotClippedPoints(V, listOfPoints, color=[0, 0, 0]):
    glPointSize(3)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    for p in listOfPoints:
        x, y = p[0], p[1]
        flag = 1
        for i in range(len(V)-1):
            p1 = V[i]
            p2 = V[i+1]
            p1p2 = (p2[0]-p1[0], p2[1]-p1[1])
            p1p = (x-p1[0], y-p1[1])
            pro = p1p2[0]*p1p[1] - p1p2[1]*p1p[0]
            if pro < 0:
                flag = 0
                break
        if flag == 1:
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
