import pygame
from pygame.locals import *
from OpenGL.GL import *
goc_quay = 0.0  # Góc quay ban đầu
speed = 0.1  # Tốc độ quay
def ve_vuong():
    global goc_quay, speed
    goc_quay += speed
    glPushMatrix()
    glRotatef(goc_quay, 0, 0, 1)  # Quay hình vuông
    glBegin(GL_QUADS)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.3, 0.3)
    glVertex2f(-0.3, 0.3)
    glEnd()
    glPopMatrix()
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

        ve_vuong()

        pygame.display.flip()

if __name__ == "__main__":
    main()
