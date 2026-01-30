import pygame
import sys

# 1. إعدادات المحرك الأساسية
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Core-Engine-X: Mobile & PC")
clock = pygame.time.Clock()

# 2. بيانات اللاعب
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
speed = 5
target_x, target_y = x, y  # نقطة الهدف عند اللمس

while True:
    # --- نظام إدارة المدخلات (Input System) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # دعم اللمس للهاتف: المربع يلحق مكان الإصبع
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: # إذا كان هناك ضغط
                target_x, target_y = event.pos
                x, y = target_x - 25, target_y - 25

    # دعم لوحة المفاتيح للكمبيوتر
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed

    # --- نظام الرسم (Rendering System) ---
    screen.fill((20, 20, 25)) # خلفية داكنة احترافية
    
    # رسم المربع (اللاعب)
    pygame.draw.rect(screen, (0, 255, 150), (x, y, 50, 50))
    
    # إضافة نص بسيط يوضح الإحداثيات
    font = pygame.font.SysFont(None, 36)
    img = font.render(f'Pos: {int(x)}, {int(y)}', True, (255, 255, 255))
    screen.blit(img, (20, 20))

    pygame.display.flip()
    clock.tick(60)
