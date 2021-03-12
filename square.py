import pygame

pygame.init()

class Square:
    def __init__(self,rect):
        self.rect = rect
        self.objective_distance = 0
        
    