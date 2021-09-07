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


def findY(p1, slope, x):
    x1, y1 = p1[0], p1[1]
    return ((slope)*(x-x1))+y1


def ErrorCal(p1, p2, pts):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    try:
        slope = (y1-y2)/(x1-x2)
        ans = 0
        for i in pts:
            ans += (findY(p1, slope, i[0])-i[1])**2
        return ans/len(pts)
    except:
        return 0


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    Errors_DDA = 0
    Errors_BRE = 0
    # Errors_DDA += FillPoly((0, 0), 6, 120, algo="DDA")

    Errors_DDA += DrawPoly((0, 0), 4, 120, algo="DDA")
    Errors_BRE+=DrawPoly((0, 0), 4, 120, algo="Bresenham")
    Errors_DDA+=DrawPoly((0, 95), 3, 120, algo="DDA")
    Errors_BRE+=DrawPoly((0, 95), 3, 120, algo="Bresenham")
    Errors_DDA+=DrawPoly((-30, 0), 4, 20)
    Errors_BRE+=DrawPoly((-30, 0), 4, 20, algo="Bresenham")
    Errors_DDA+=DrawPoly((30, 0), 4, 20)
    Errors_BRE+=DrawPoly((30, 0), 4, 20, algo="Bresenham")
    Errors_DDA+=DrawRectangle(0, -25, 20, 70)
    Errors_BRE+=DrawRectangle(0, -25, 20, 70, algo="Bresenham")
    # Errors_DDA+=drawDDA((0,0),(200,220))
    # Errors_BRE+=drawBresenham((0,0),(200,220))
    print("Errors_DDA", Errors_DDA)
    print("Errors_BRE", Errors_BRE)
    glFlush()


def drawBresenham(p1, p2, color=[0, 0, 0]):
    glPointSize(3)
    pts = []
    x0, y0, x1, y1 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    pts = []
    error = 0
    for x in range(dx + 1):
        x_ = x0 + x*xx + y*yx
        y_ = y0 + x*xy + y*yy
        glVertex2i(x_, y_)
        pts.append((x_, y_))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    glEnd()
    # print(len(pts))
    # print("BRE",pts)
    return ErrorCal((x0, y0), (x1, y1), pts)


def drawDDA(p1, p2, color=[0, 0, 0]):
    glPointSize(3)
    x1, y1, x2, y2 = round(p1[0], 1), round(
        p1[1], 1), round(p2[0], 1), round(p2[1], 1)
    x, y = x1, y1
    length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    pts = []
    dx, dy = round(dx, 1), round(dy, 1)
    for i in range(int(length+1)):
        pts.append((ROUND(x), ROUND(y)))
        glVertex2i(ROUND(x), ROUND(y))
        x += dx
        y += dy
    glEnd()
    # print(len(pts))
    # print("DDA",pts)
    return ErrorCal((x1, y1), (x2, y2), pts)


def DrawPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
    x0, y0 = center[0], center[1]
    a = math.radians(360 / n)
    d = s / 2 / math.sin(a / 2)
    pts = []
    bv1x = x0-s/2
    bv1y = y0 - (s/2)*(1/math.tan(math.radians(180/n)))
    bv2x = x0+s/2
    bv2y = bv1y
    for i in range(n+1):
        sideAngle = math.radians((360 * i / n))
        x = (bv1x-x0)*math.cos(sideAngle) - (bv1y-y0) * math.sin(sideAngle)+x0
        y = (bv1x-x0)*math.sin(sideAngle) + (bv1y-y0) * math.cos(sideAngle)+y0
        pts.append([x, y])
    errors = []
    for i in range(n):
        errors.append(eval("draw"+algo+"(pts[i], pts[i+1], color)"))
    print(algo[0:3], "\tsides:", n, "\tlength", s, "\t", sum(errors))
    return sum(errors)


def FillPoly(center, n, s, color=[0, 0, 0], algo="DDA"):
    glPointSize(5)
    errors = []
    for i in range(1, s):
        errors.append(DrawPoly(center, n, i, color, algo))
    print(algo[0:3], "\tsides:", n, "\tlength", s, "\t", sum(errors))
    return sum(errors)


def DrawRectangle(h: float, k: float, length: float, breadth: float, color=[0, 0, 0], algo="DDA"):
    glPointSize(3)
    glColor3f(color[0], color[1], color[2])
    l = length/2
    b = breadth/2
    errors = []
    errors.append(eval("draw"+algo+"((h + l, k+b), (h + l, k-b), color)"))
    errors.append(eval("draw"+algo+"((h - l, k-b), (h + l, k-b), color)"))
    errors.append(eval("draw"+algo+"((h - l, k-b), (h - l, k+b), color)"))
    errors.append(eval("draw"+algo+"((h - l, k+b), (h + l, k+b), color)"))
    print(algo[0:3], "\tsides:", 4, "\tlength", length,
          "\tbreadth", breadth, "\t", sum(errors))
    return sum(errors)


def FillRectangle(h, k, length, breadth, color=[0, 0, 0],algo="DDA"):
    glPointSize(5)
    l, b = 1, 1
    errors=[]
    for i in range(1, max(length, breadth)):
        errors.append(DrawRectangle(h, k, l, b, color))
        if l < length:
            l += 1
        if b < breadth:
            b += 1
    print(algo[0:3], "\tsides:", 4, "\tlength", length,
          "\tbreadth", breadth, "\t", sum(errors))
    return sum(errors)


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
