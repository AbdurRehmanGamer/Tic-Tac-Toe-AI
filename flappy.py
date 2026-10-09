import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - By AbdurRehman")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)

bird_x = 100
bird_y = 300
bird_vel = 0
gravity = 0.5
jump_power = -9

pipe_x = 400
pipe_width = 70
pipe_gap = 160
pipe_height = random.randint(80, 380)

score = 0
game_over = False

def reset_game():
    global bird_y, bird_vel, pipe_x, pipe_height, score
    bird_y = 300
    bird_vel = 0
    pipe_x = 400
    pipe_height = random.randint(80, 380)
    score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump_power
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        bird_vel += gravity
        bird_y += bird_vel

        pipe_x -= 4

        if pipe_x < -pipe_width:
            pipe_x = 400
            pipe_height = random.randint(80, 380)
            score += 1

        if bird_y + 15 > HEIGHT - 30 or bird_y - 15 < 0:
            game_over = True

        if pipe_x < bird_x + 15 and pipe_x + pipe_width > bird_x - 15:
            if bird_y - 15 < pipe_height or bird_y + 15 > pipe_height + pipe_gap:
                game_over = True

    screen.fill((135, 206, 250))

    pygame.draw.rect(screen, (0, 200, 0), (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, (0, 200, 0), (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

    pygame.draw.circle(screen, (255, 255, 0), (bird_x, int(bird_y)), 18)
    pygame.draw.circle(screen, (255, 140, 0), (bird_x + 8, int(bird_y)), 5)
    pygame.draw.circle(screen, (0, 0, 0), (bird_x + 5, int(bird_y) - 5), 3)

    pygame.draw.rect(screen, (222, 184, 135), (0, HEIGHT - 30, WIDTH, 30))
    pygame.draw.rect(screen, (34, 139, 34), (0, HEIGHT - 30, WIDTH, 10))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("Press R to Restart", True, (255, 0, 0))
        screen.blit(over_text, (60, HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)
