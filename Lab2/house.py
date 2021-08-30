import glfw
import numpy as np
from OpenGL.GL import *


class Window:
    def __init__(self, width: int, height: int, title: str):
        if not glfw.init():
            raise Exception("glfw cannot be initialized.")
        self.win = glfw.create_window(width, height, title, None, None)
        if not self.win:
            glfw.terminate()
            raise Exception("window cannot be created.")
        glfw.set_window_pos(self.win, 400, 200)
        glfw.make_context_current(self.win)
        glClearColor(0, 0, 0, 1)
        glColor3f(0, 1, 1)

    def main_loop(self):
        while not glfw.window_should_close(self.win):
            glfw.poll_events()
            DrawSquare(0.0, 0.0, 0.4)
            DrawRectangle(0.0, -0.05, 0.1, 0.3)
            DrawRectangle(-0.1, 0.05, 0.05, 0.1)
            DrawRectangle(0.1, 0.05, 0.05, 0.1)
            DrawTriangle()
            glFlush()
            glfw.swap_buffers(self.win)
        glfw.terminate()


def DrawSquare(h: float, k: float, sidelength: float):
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5) 
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 1)
    halfside = sidelength/2
    glVertex2f(h + halfside, k+halfside)
    glVertex2f(h + halfside, k-halfside)
    glVertex2f(h - halfside, k-halfside)
    glVertex2f(h - halfside, k+halfside)
    glEnd()


def DrawRectangle(h: float, k: float, length: float, breadth: float):
    glBegin(GL_POLYGON)
    glColor3f(255, 255, 255)
    glVertex2f(h+length/2, k+breadth/2)
    glVertex2f(h+length/2, k-breadth/2)
    glVertex2f(h-length/2, k-breadth/2)
    glVertex2f(h-length/2, k+breadth/2)
    glEnd()


def DrawTriangle():
    # glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    glVertex3f(-0.2, 0.21, 0.0)
    # glColor3f(0, 1, 0)
    glVertex3f(0.2, 0.21, 0.0)
    # glColor3f(0, 0, 1)
    glVertex3f(0.0, 0.7, 0.0)
    glEnd()


win = Window(1280, 720, "House")

glEnableClientState(GL_VERTEX_ARRAY)

win.main_loop()
