import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird by AbdurRehman")
clock = pygame.time.Clock()

bird_y = 300
gravity = 0.5
bird_vel = 0
pipe_x = 400

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            bird_vel = -8

    bird_vel += gravity
    bird_y += bird_vel
    pipe_x -= 3
    if pipe_x < -50:
        pipe_x = 400

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 255, 0), (100, int(bird_y)), 20)
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, 50, 250))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 350, 50, 250))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
