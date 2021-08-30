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

            DrawRectangle(0, 0, 1, 1, [0, 0, 1])

            glFlush()
            glfw.swap_buffers(self.win)
        glfw.terminate()


def DrawRectangle(h: float, k: float, length: float, breadth: float, color: list = [255, 255, 255]):
    glBegin(GL_POLYGON)
    glColor3f(color[0] ,color[1], color[2])
    glVertex2f(h + length / 2, k + breadth / 2)
    glVertex2f(h + length / 2, k - breadth / 2)
    glVertex2f(h - length / 2, k - breadth / 2)
    glVertex2f(h - length / 2, k + breadth / 2)
    glEnd()



win = Window(1280, 720, "Square")

glEnableClientState(GL_VERTEX_ARRAY)

win.main_loop()
