# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    # Make the screen close and end program
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updatable.update(dt)


        # Asteroid collision with player unit
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over")
                sys.exit()
        
            # Collision with bullets
            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()

        # Fill the screen black
        pygame.Surface.fill(screen, (0, 0, 0))

        # Draw objects on screen
        for obj in drawable:
            obj.draw(screen)
        

        pygame.display.flip()

        # limiting the framerate to 60 fps
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
