# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    td = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # This makes the window's close button work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(td)
        screen.fill("black")
        player.draw(screen)
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
