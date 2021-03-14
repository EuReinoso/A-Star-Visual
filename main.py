import pygame,sys,numpy,math
from pygame.locals import *
from square import Square
from adjacent import Adjacent
from orderedVector import OrderedVector
from astar import AStar

pygame.init()

WINDOW_SIZE = (640,480)
BLOCK_SIZE = 20

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (50,100,200)

fps = pygame.time.Clock()

grid_list = numpy.empty(shape=[24,32],dtype=object)

def draw_grid():
    for line in grid_list:
        for sqr in line:
            if sqr.visited == False:
                pygame.draw.rect(window,BLACK,sqr.rect,1,2)
            if sqr.visited == True:
                pygame.draw.rect(window,GREEN,sqr.rect)

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
    return math.sqrt(((objective[0] - actual[0]))**2 + abs((objective[1] - actual[1]))**2)

def gen_objective_distance():
    for line in grid_list:
        for sqr in line:
            sqr.objective_distance = get_objective_distance((sqr.rect.x,sqr.rect.y),objective_pos)

def gen_adjacents():
    i=0
    for line in grid_list:
        j=0
        for sqr in line:
            if j < len(line) -1:
                sqr.add_adjacent(Adjacent(grid_list[i][j+1]))
            if j > 0:
                sqr.add_adjacent(Adjacent(grid_list[i][j-1]))
            if i < len(grid_list) -1:
                sqr.add_adjacent(Adjacent(grid_list[i+1][j]))
            if i > 0:
                sqr.add_adjacent(Adjacent(grid_list[i-1][j]))
            j+=1
        i+=1

objective_pos = set_pos(28,12)
objective_rect = pygame.Rect(objective_pos[0],objective_pos[1],BLOCK_SIZE,BLOCK_SIZE)


def main():

    global window,fps
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("A* Pathfinding")

    window.fill(WHITE)
    gen_rects()
    gen_objective_distance()
    gen_adjacents()
    astar = AStar(grid_list[0][0],grid_list[12][28])
    

    pygame.draw.rect(window,RED,objective_rect)

    loop = True

    while loop:
        

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if astar.found == False:
            astar.seach()
        
        draw_grid()

        for actual in astar.actual_list:
            pygame.draw.rect(window,BLUE,actual.rect)

        
        pygame.display.update()
        fps.tick(5)
    
main()

