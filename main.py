import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Core-Engine-X")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 127), (375, 275, 50, 50))
    pygame.display.flip()
    clock.tick(60)
