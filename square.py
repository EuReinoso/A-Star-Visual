import pygame

pygame.init()

class Square:
    def __init__(self,rect):
        self.rect = rect
        self.objective_distance = 0
        self.visited = False
        self.adjacents = []
        self.is_wall = False
    
    def add_adjacent(self,adjacent):
        self.adjacents.append(adjacent)
        
    