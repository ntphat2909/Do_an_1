import pygame
from pygame.locals import *
from OpenGL.GL import *
from math import *
def draw_circle(radius, center):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(center)
    for i in range(0, 361):
        glVertex3fv((center[0] + radius * cos(radians(i)), center[1] + radius * sin(radians(i)), 0))
    glEnd()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình tròn 3D")

    center = (0, 0, 0)
    radius = 0.6

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        draw_circle(radius, center)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
