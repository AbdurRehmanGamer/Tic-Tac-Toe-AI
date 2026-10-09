import pygame
import random
import sys

pygame.init()
W, H = 360, 640
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

bird_y = H//2
bird_v = 0
gravity = 0.5
pipes = []
score = 0

def new_pipe():
    h = random.randint(100, 400)
    return [W, h]

pipes.append(new_pipe())

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running=False
        if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
            bird_v = -8

    bird_v += gravity
    bird_y += bird_v

    # pipes move
    for p in pipes:
        p[0] -= 3
    if pipes[0][0] < -60:
        pipes.pop(0)
        pipes.append(new_pipe())
        score += 1
    if pipes[-1][0] < W - 200:
        pipes.append(new_pipe())

    # collision
    bird_rect = pygame.Rect(80, bird_y, 30, 30)
    dead = False
    if bird_y < 0 or bird_y > H-30:
        dead = True
    for px, py in pipes:
        top_rect = pygame.Rect(px, 0, 60, py-70)
        bot_rect = pygame.Rect(px, py+70, 60, H)
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):
            dead = True

    if dead:
        screen.fill((0,0,0))
        txt = font.render(f"Game Over! Score: {score}", True, (255,255,255))
        screen.blit(txt, (50, H//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        bird_y = H//2
        bird_v = 0
        pipes = [new_pipe()]
        score = 0
        continue

    # draw
    screen.fill((135, 206, 250)) # sky
    pygame.draw.circle(screen, (255, 255, 0), (80+15, int(bird_y)+15), 15) # bird
    pygame.draw.polygon(screen, (255, 150, 0), [(95, bird_y+12), (115, bird_y+15), (95, bird_y+18)]) # beak

    for px, py in pipes:
        pygame.draw.rect(screen, (0, 200, 0), (px, 0, 60, py-70))
        pygame.draw.rect(screen, (0, 200, 0), (px, py+70, 60, H))

    txt = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(txt, (10,10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
