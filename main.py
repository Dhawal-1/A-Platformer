import pygame

pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()