import pygame
from pygame.locals import *
from OpenGL.GL import *
import math

def ve_hinh_tron(ban_kinh, so_luong_mien):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Tâm của hình tròn
    for i in range(so_luong_mien + 1):
        goc = 2.0 * math.pi * i / so_luong_mien
        x = ban_kinh * math.cos(goc)
        y = ban_kinh * math.sin(goc)
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình tròn")

    glOrtho(-1, 1, -1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1.0, 1.0, 1.0)  # Màu trắng
        ve_hinh_tron(0.6, 36)  # Bán kính 0.3, xấp xỉ hình tròn với 36 mảnh

        pygame.display.flip()

if __name__ == "__main__":
    main()
