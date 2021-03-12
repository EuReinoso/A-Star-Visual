import pygame,sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (640,480)
BLOCK_SIZE = 20

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

            
def main():

    global window
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("A* Pathfinding")

    window.fill(WHITE)
    draw_grid()

    fps = pygame.time.Clock()

    loop = True
    while loop:
        

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        pygame.display.update()
        fps.tick(60)

def draw_grid():
    for x in range(WINDOW_SIZE[0]):
        for y in range(WINDOW_SIZE[1]):
            rect = pygame.Rect(x * BLOCK_SIZE,y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(window,BLACK,rect,1,2)


main()

