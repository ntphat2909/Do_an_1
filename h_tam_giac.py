import pygame
from pygame.locals import *
from OpenGL.GL import *

def ve_tam_giac():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6 , -0.6)
    glVertex2f(0.6, -0.6)
    glVertex2f(0.0, 0.6)
   
    glEnd()

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình tam giác")

    glOrtho(-1, 1, -1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        ve_tam_giac()


        pygame.display.flip()

if __name__ == "__main__":
    main()
