import pygame
import sys

# 1. الإعدادات
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 2. بيانات الكاميرا والعالم
player_pos = [WIDTH // 2, HEIGHT // 2]
camera_offset = [0, 0]
world_size = 2000 # حجم العالم (أكبر بكثير من الشاشة)

# 3. عوائق عشوائية في العالم (أشجار أو صخور)
obstacles = []
for i in range(20):
    obstacles.append((100 * i, 300))

while True:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # التحكم باللمس (تحديث مكان اللاعب)
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player_pos[0], player_pos[1] = event.pos[0] + camera_offset[0], event.pos[1] + camera_offset[1]

    # 4. منطق الكاميرا (تجعل اللاعب دائماً في المنتصف)
    camera_offset[0] = player_pos[0] - WIDTH // 2
    camera_offset[1] = player_pos[1] - HEIGHT // 2

    # 5. رسم الأشياء بالنسبة للكاميرا (Render Pipeline)
    # رسم خطوط الشبكة للأرضية لإظهار الحركة
    for x in range(0, world_size, 100):
        pygame.draw.line(screen, (50, 50, 50), (x - camera_offset[0], 0), (x - camera_offset[0], HEIGHT))
    for y in range(0, world_size, 100):
        pygame.draw.line(screen, (50, 50, 50), (0, y - camera_offset[1]), (WIDTH, y - camera_offset[1]))

    # رسم العوائق
    for obs in obstacles:
        pygame.draw.rect(screen, (200, 100, 0), (obs[0] - camera_offset[0], obs[1] - camera_offset[1], 40, 40))

    # رسم اللاعب
    pygame.draw.rect(screen, (0, 255, 150), (player_pos[0] - camera_offset[0], player_pos[1] - camera_offset[1], 50, 50))

    pygame.display.flip()
    clock.tick(60)
