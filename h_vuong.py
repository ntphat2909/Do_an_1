import pygame
from pygame.locals import *
from OpenGL.GL import *

def ve_hinh_vuong():
    glLineWidth(3.0)
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.6, -0.6)
    glVertex2f(0.6, -0.6)
    glVertex2f(0.6, 0.6)
    glVertex2f(-0.6, 0.6)
    glEnd()
    

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình vuông")

    glOrtho(-1, 1, -1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        ve_hinh_vuong()

        pygame.display.flip()

if __name__ == "__main__":
    main()
