import pygame
from pygame.locals import *
from OpenGL.GL import *

def ve_hinh_chu_nhat():
    glLineWidth(3.0)
    glBegin(GL_QUADS)
    glColor3f(0,1, 0)
    glVertex2f(-0.6, -0.4)
    glVertex2f(0.6, -0.4)
    glVertex2f(0.6, 0.4)
    glVertex2f(-0.6, 0.4)
    glEnd()

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình chữ nhật")

    glOrtho(-1, 1, -1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        ve_hinh_chu_nhat()

        pygame.display.flip()

if __name__ == "__main__":
    main()
