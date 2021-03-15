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

w = WINDOW_SIZE[0]//len(grid_list[0])
h = WINDOW_SIZE[1]//len(grid_list)

def click_wall(pos,state):
    i = pos[1]//w
    j = pos[0]//h
    grid_list[i][j].is_wall = state

def draw_grid():
    for line in grid_list:
        for sqr in line:
            if sqr.visited == True:
                pygame.draw.rect(window,GREEN,sqr.rect)
            if sqr.is_wall:
                pygame.draw.rect(window,BLACK,sqr.rect)
            if sqr == astar.actual:
                pygame.draw.rect(window,BLUE,sqr.rect)
            else:
                pygame.draw.rect(window,BLACK,sqr.rect,1,2)

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
            sqr.objective_distance = get_objective_distance((sqr.rect.x,sqr.rect.y),(objective.rect.x,objective.rect.y))

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


def main():

    global window,origin,objective,astar
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("A* Pathfinding")

    
    gen_rects()

    origin = grid_list[3][5]
    objective = grid_list[12][28]

    gen_objective_distance()
    gen_adjacents()
    
    astar = AStar(origin,objective)

    

    loop = True
    start = False

    vel = 30
    while loop:
        window.fill(WHITE)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed(3)[0]:
                    click_wall(pygame.mouse.get_pos(),True)
                if pygame.mouse.get_pressed(3)[2]:
                    click_wall(pygame.mouse.get_pos(),False)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed(3)[0]:
                    click_wall(pygame.mouse.get_pos(),True)
                if pygame.mouse.get_pressed(3)[2]:
                    click_wall(pygame.mouse.get_pos(),False)

        if start:
            vel = 5
            if astar.found == False:
                astar.seach()

        pygame.draw.rect(window,RED,objective.rect)
        pygame.draw.rect(window,GREEN,origin.rect)
        draw_grid()
        
        pygame.display.update()
        fps.tick(vel)
    
main()

