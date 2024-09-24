import pygame
from constants import *
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    running = True

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player_obj = Player(x, y)
    asteroid_field = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.collision(player_obj):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()