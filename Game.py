from Map import *
import os
import time
class Game:
    def __init__(self):
        self.map = Map()
        
    def Play(self, times):
        while True:
            time.sleep(times)
            os.system("clear")
            self.map.Display()
            new_list2D = [[Cell() for y in range(self.map.mapSize)] for x in range(self.map.mapSize)]
            for i in range(self.map.mapSize):
                for j in range(self.map.mapSize):
                    alive_neighbors = self.get_alive_neighbors(i, j)
                    if self.map.list2D[i][j].isAlive:
                        if alive_neighbors == 2 or alive_neighbors == 3:
                            new_list2D[i][j].Switch()
                    else:
                        if alive_neighbors == 3:
                            new_list2D[i][j].Switch()
            self.map.list2D = new_list2D
            
    def get_alive_neighbors(self, i, j):
        alive_neighbors = 0
        for x in range(max(0, i-1), min(i+2, self.map.mapSize)):
            for y in range(max(0, j-1), min(j+2, self.map.mapSize)):
                if x == i and y == j:
                    continue
                if self.map.list2D[x][y].isAlive:
                    alive_neighbors += 1
        return alive_neighbors

