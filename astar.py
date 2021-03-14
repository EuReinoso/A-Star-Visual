from orderedVector import OrderedVector
import pygame

class AStar:
    def __init__(self,actual,objective):
        self.objective = objective
        self.found = False
        self.actual = actual
        self.actual_list = []

    def seach(self):
        print(self.actual.objective_distance)
        self.actual.visited = True
        self.actual_list.append(self.actual)

        if self.actual == self.objective:
            print("Found")
            self.found = True
        else:
            adj_list = OrderedVector(len(self.actual.adjacents))
            for adj in self.actual.adjacents:
                if adj.square == self.objective:
                    self.actual = self.objective
                    return
                else:
                    if adj.square.visited == False and adj.square.is_wall == False:
                        adj.square.visited = True
                        adj_list.insert(adj)
                
            if adj_list.valors[0] != None:
                self.actual = adj_list.valors[0].square
    
            
