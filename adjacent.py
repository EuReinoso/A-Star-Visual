import pygame

pygame.init()

class Adjacent:
    def __init__(self,square):
        self.square = square
        self.astar_distance = square.objective_distance + 20