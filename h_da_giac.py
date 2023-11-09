import pygame
from pygame.locals import *
from OpenGL.GL import *

def ve_da_giac_5_canh():
    glBegin(GL_POLYGON)
    # Định nghĩa các đỉnh của đa giác 5 cạnh
    glVertex2f(0.0, 0.5)   # Đỉnh 1
    glVertex2f(-0.4, 0.2)  # Đỉnh 2
    glVertex2f(-0.25, -0.3)  # Đỉnh 3
    glVertex2f(0.25, -0.3)   # Đỉnh 4
    glVertex2f(0.4, 0.2)  # Đỉnh 5
    glEnd()

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình đa  giác 5 cạnh")

    glOrtho(-1, 1, -1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        ve_da_giac_5_canh()

        pygame.display.flip()

if __name__ == "__main__":
    main()
