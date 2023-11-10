import pygame
from pygame.locals import *
from OpenGL.GL import *
import math

vertices = []
edges = []

def create_sphere(radius, vertical_slices, horizontal_slices):
    for i in range(horizontal_slices + 1):
        h_angle = 2 * math.pi * i / horizontal_slices
        h_y = radius * math.cos(h_angle)
        h_radius = radius * math.sin(h_angle)

        for j in range(vertical_slices + 1):
            v_angle = math.pi * j / vertical_slices
            x = h_radius * math.cos(v_angle)
            y = h_y
            z = h_radius * math.sin(v_angle)

            vertices.append((x, y, z))

    # Add edges for vertical circles
    for i in range(horizontal_slices):
        for j in range(vertical_slices):
            edges.append((i * (vertical_slices + 1) + j, (i + 1) * (vertical_slices + 1) + j))

    # Add edges for horizontal circles
    for i in range(vertical_slices):
        for j in range(horizontal_slices):
            edges.append((j * (vertical_slices + 1) + i, j * (vertical_slices + 1) + i + 1))

def draw_sphere():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def set_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Sphere with Circles")

    set_projection()

    create_sphere(radius=1, vertical_slices=15, horizontal_slices=15)

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

        draw_sphere()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
