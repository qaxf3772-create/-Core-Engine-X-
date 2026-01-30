import pygame
import sys

# Core Systems
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Core-Engine-X")
clock = pygame.time.Clock()

# Player Data
x, y = 375, 275
speed = 5

while True:
    # 1. Input System
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed

    # 2. Rendering System
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 127), (x, y, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)
