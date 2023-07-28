import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))

white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

place = [100, 100]
triplace = [0, 0]
cubpos = [0, 0]
font = pygame.font.SysFont("Arial", 70)
game_over = font.render("Game Over", True, white)
gameoveris = False
time_when_game_over = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200, 0, 0))
    mouspos = pygame.mouse.get_pos()
    triplace = mouspos
    keys = pygame.key.get_pressed()
    muspes = pygame.mouse.get_pressed()
    if muspes[0]:
        place = mouspos
    if keys[pygame.K_SPACE]:
        place = mouspos
    
    if not gameoveris:
        cubpos[1] += 0.5
    if ((cubpos[0] + 25 - triplace[0]) ** 2 + (cubpos[1] + 25 - triplace[1]) ** 2) ** 0.5 < (50):
        cubpos[1] = 0
        cubpos[0] = random.randint(0, 750)
    if (((cubpos[0] + 25 - place[0]) ** 2 + (cubpos[1] + 25 - place[1]) ** 2) ** 0.5 < (50) or cubpos[1] > 600) and not gameoveris:
        gameoveris = True
        time_when_game_over = time.time_ns()
    if gameoveris:
        screen.blit(game_over, (250, 250))
    if gameoveris and time.time_ns() - time_when_game_over > 3000000000:
        running = False

    pygame.draw.circle(screen, (0, 0, 255), place, 25)
    pygame.draw.polygon(screen, (0, 200, 0), (triplace, (triplace[0] - 25, triplace[1] + 43), (triplace[0] + 25, triplace[1] + 43)))
    pygame.draw.rect(screen, (255, 255, 255), (cubpos[0], cubpos[1], 50, 50))
    pygame.display.update()

