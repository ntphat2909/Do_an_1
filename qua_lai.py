import pygame
from pygame.locals import *
from OpenGL.GL import *

# Đặt biến toàn cục để theo dõi vị trí và tốc độ của tam giác
tran_x = 0.0
speed = 0.001

def ve_tam_giac():
    global tran_x, speed  # Sử dụng biến toàn cục
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6 + tran_x, -0.6)
    glVertex2f(0.6 + tran_x, -0.6)
    glVertex2f(0.0 + tran_x, 0.6)
    glEnd()
    tran_x += speed  # Cập nhật vị trí tam giác
    if tran_x > 1.0 or tran_x < -1.0:
        speed = -speed  # Đảo tốc độ khi đạt biên

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
