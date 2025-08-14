# this allows us to use code from the open-source pygame library throughout this file
import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    td = 0

    updatable = pygame.sprite.Group() # all the objects that can be updated
    drawable = pygame.sprite.Group()  # all the objects that can be drawn
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    while True:
        # This makes the window's close button work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(td)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip() # refresh the screen
        # tick(60): pause the game loop for 1/60th of a second (60 FPS).
        td = clock.tick(60) / 1000 # from (16.67) milliseconds to seconds 
        


if __name__ == "__main__":
    main()
# "This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module.
# It's considered the "pythonic" way to structure an executable program in Python. 
# Technically, the program will work fine by just calling main(), 
# but you might get an angry letter from Guido van Rossum if you don't."
