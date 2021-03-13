import pygame,sys,numpy
from pygame.locals import *
from square import Square
from adjacent import Adjacent

pygame.init()

WINDOW_SIZE = (640,480)
BLOCK_SIZE = 20

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


grid_list = numpy.empty(shape=[24,32],dtype=object)

def draw_grid():
    for line in grid_list:
        for sqr in line:
            pygame.draw.rect(window,BLACK,sqr,1,2)

def gen_rects():
    i=0
    for x in range(0,WINDOW_SIZE[0],20):
        j=0
        for y in range(0,WINDOW_SIZE[1],20):
            rect = pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            grid_list[j][i] = Square(rect)
            j+=1
        i+=1

def set_pos(x,y):
    return (x*BLOCK_SIZE,y* BLOCK_SIZE)

def get_objective_distance(actual,objective):
    return (objective[0] - actual[0]) + (objective[1] - actual[1])

def gen_objective_distance():
    for line in grid_list:
        for sqr in line:
            sqr.objective_distance = get_objective_distance((sqr.rect.x,sqr.rect.y),objective_pos)


objective_pos = set_pos(28,12)
objective_rect = pygame.Rect(objective_pos[0],objective_pos[1],BLOCK_SIZE,BLOCK_SIZE)

def main():

    global window
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("A* Pathfinding")

    window.fill(WHITE)
    gen_rects()
    draw_grid()
    gen_objective_distance()

    pygame.draw.rect(window,RED,objective_rect)

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
    

main()

