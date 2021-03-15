from orderedVector import OrderedVector
import pygame

class AStar:
    def __init__(self,actual,objective):
        self.origin = actual
        self.objective = objective
        self.found = False
        self.actual = actual
        self.visited_list = []
        self.path = []
        self.entered = False

    def seach(self):
        print(self.actual.objective_distance)
        self.actual.visited = True
        

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
                    if adj.square.is_wall == False and not adj.square.visited:
                        adj.square.visited = True
                        self.visited_list.append(adj)
                        adj_list.insert(adj)   
                
            if adj_list.valors[0] != None:
                self.actual = adj_list.valors[0].square

            else:
                ordered = OrderedVector(len(self.visited_list))
                for adj in self.visited_list:
                    x = 0
                    for a in adj.square.adjacents:
                        if a.square.visited == False and a.square.is_wall == False:
                            x+=1
                    if x > 0:
                        ordered.insert(adj)
                    
                if ordered.valors[0] != None:
                    self.actual = ordered.valors[0].square
                    print("baixo")

    def seach_back(self):
        print(self.actual.objective_distance)
        self.path.append(self.actual)
        
        adj_list = OrderedVector(len(self.actual.adjacents))
        
    
        for adj in self.actual.adjacents:
            if adj.square.visited:
                adj_list.insert(adj)  

        if adj_list.valors[0] != None:
            self.actual = adj_list.valors[0].square


    def return_origin(self):
        
        if not self.entered:
            self.objective = self.origin
            self.entered = True
            
