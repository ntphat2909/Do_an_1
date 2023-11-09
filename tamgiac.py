import pygame
from pygame.locals import *
from OpenGL.GL import *


vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
)

def ve_hinh_tam_giac():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def cai_dat_phoi_canh():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Hình tam giác 3D")

    cai_dat_phoi_canh()

    angle_x = 0
    angle_y = 0
    is_rotating = False
    last_x = 0
    last_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            #Bắt sự kiện giữ click chuột để xoay ảnh
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                is_rotating = True
                last_x, last_y = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                is_rotating = False

        if is_rotating:
            x, y = pygame.mouse.get_pos()
            delta_x = x - last_x
            delta_y = y - last_y
            angle_x += delta_x
            angle_y += delta_y
            last_x, last_y = x, y

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(angle_x, 0, 1, 0)
        glRotatef(angle_y, 1, 0, 0)

        ve_hinh_tam_giac()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
