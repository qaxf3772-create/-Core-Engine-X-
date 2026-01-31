import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# نقاط المكعب (X, Y, Z) والأوجه الملونة
points = [[-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1], [-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]]
# تعريف الوجوه (6 أوجه)
faces = [(0,1,2,3), (4,5,6,7), (0,1,5,4), (2,3,7,6), (0,3,7,4), (1,2,6,5)]
colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]

angle_x = angle_y = 0

def project(p):
    x, y, z = p
    # دوران X و Y
    ny = y*math.cos(angle_x) - z*math.sin(angle_x); nz = y*math.sin(angle_x) + z*math.cos(angle_x); y, z = ny, nz
    nx = x*math.cos(angle_y) + z*math.sin(angle_y); nz = -x*math.sin(angle_y) + z*math.cos(angle_y); x, z = nx, nz
    z += 5
    f = 600 / z
    return [x*f + WIDTH//2, y*f + HEIGHT//2], z

while True:
    screen.fill((5, 5, 15))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            angle_y += event.rel[0] * 0.01; angle_x -= event.rel[1] * 0.01

    # رندرة مع ترتيب العمق (Z-Sorting) لكي لا يتداخل الرسم
    rendered = [project(p) for p in points]
    face_list = []
    for i, face in enumerate(faces):
        avg_z = sum(rendered[p][1] for p in face) / 4
        face_list.append((avg_z, i))
    
    # رسم الأوجه من الأبعد للأقرب (Painter's Algorithm)
    for _, i in sorted(face_list, reverse=True):
        pts = [rendered[p][0] for p in faces[i]]
        pygame.draw.polygon(screen, colors[i], pts)
        pygame.draw.polygon(screen, (255,255,255), pts, 2) # إطار أبيض

    pygame.display.flip()
    clock.tick(60)
