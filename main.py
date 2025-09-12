import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)   # Limit to 60 FPS
        dt = pygame.time.Clock().tick(60) / 1000  # Delta time in seconds
        

if __name__ == "__main__":
    main()
