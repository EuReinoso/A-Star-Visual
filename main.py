import pygame,sys
from pygame.locals import *

WINDOW_SIZE = (640,480)

class Main:
    
    def main():

        window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("A* Pathfinding")

        fps = pygame.time.Clock()

        loop = True
        while loop:
            
            window.fill((0,0,0))

            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            fps.tick(60)

Main.main()

