import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == '__main__':
  main()
