import pygame
import sys

# 1. الإعدادات الأساسية
pygame.init()
# الحصول على أبعاد الشاشة الحقيقية للهاتف
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 2. إعدادات اللاعب
player_pos = [WIDTH // 2, HEIGHT // 2]
speed = 7

# 3. حساب أحجام الأزرار بناءً على مساحة الشاشة (توزيع ذكي)
# سنجعل حجم الزر حوالي 15% من عرض الشاشة
btn_size = int(WIDTH * 0.15) 
margin = 20 # مسافة بسيطة من الحواف

# أماكن الأزرار (تلقائية)
left_btn  = pygame.Rect(margin, HEIGHT - btn_size*2 - margin, btn_size, btn_size)
right_btn = pygame.Rect(margin + btn_size*2, HEIGHT - btn_size*2 - margin, btn_size, btn_size)
up_btn    = pygame.Rect(margin + btn_size, HEIGHT - btn_size*3 - margin, btn_size, btn_size)
down_btn  = pygame.Rect(margin + btn_size, HEIGHT - btn_size - margin, btn_size, btn_size)

# زر الإطلاق في الجهة اليمنى
shoot_btn = pygame.Rect(WIDTH - btn_size - margin*2, HEIGHT - btn_size - margin*2, btn_size*1.2, btn_size*1.2)

while True:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # فحص اللمس
    m_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if up_btn.collidepoint(m_pos): player_pos[1] -= speed
        if down_btn.collidepoint(m_pos): player_pos[1] += speed
        if left_btn.collidepoint(m_pos): player_pos[0] -= speed
        if right_btn.collidepoint(m_pos): player_pos[0] += speed

    # رسم اللاعب
    pygame.draw.rect(screen, (0, 255, 150), (*player_pos, 50, 50))

    # رسم أزرار التحكم بشكل أوضح (نصف شفاف)
    for btn in [up_btn, down_btn, left_btn, right_btn]:
        pygame.draw.rect(screen, (150, 150, 150), btn, 3) # إطار الزر
    
    # رسم زر الإطلاق بلون مختلف
    pygame.draw.rect(screen, (255, 80, 80), shoot_btn, 5)

    pygame.display.flip()
    clock.tick(60)
