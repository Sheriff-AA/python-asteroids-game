import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    running = True

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player_obj = Player(x, y)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        player_obj.draw(screen)
        player_obj.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()