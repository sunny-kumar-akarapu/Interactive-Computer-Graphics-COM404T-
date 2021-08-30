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
            glClear(GL_COLOR_BUFFER_BIT)
            glPointSize(5)

            DrawTriangle((-0.3, 0), (0.3, 0), (0, 0.6))

            glFlush()
            glfw.swap_buffers(self.win)
        glfw.terminate()


def DrawTriangle(v1: tuple, v2: tuple, v3: tuple, color: list = [255, 255, 255]):
    glBegin(GL_POLYGON)
    # glColor3f(color[0] ,color[1], color[2])
    glColor3f(1, 0, 0)
    glVertex2f(v1[0],v1[1])
    glColor3f(0, 1, 0)
    glVertex2f(v2[0],v2[1])
    glColor3f(0, 0, 1)
    glVertex2f(v3[0],v3[1])
    glEnd()


win = Window(1280, 720, "Triangle")

glEnableClientState(GL_VERTEX_ARRAY)

win.main_loop()

