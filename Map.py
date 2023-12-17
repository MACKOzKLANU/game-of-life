from Cell import *

# print(my_list)

class Map:
    def __init__(self) -> None:
        self.list2D = []
        self.mapSize = 20
        for i in range(self.mapSize):
            inner_list = []
            for j in range(self.mapSize):
                inner_list.append(Cell())
            self.list2D.append(inner_list)
    def Display(self):
        for i in range(self.mapSize):
            for j in range(self.mapSize):
                if self.list2D[i][j].isAlive:
                    print("X",end="")
                else:
                    print(" ",end="")
            print()
    def Set(self, i, j, status):
        self.list2D[i][j].isAlive = status

    def Fill(self, filename):
        file = open(filename +".txt", "r")
        tekst = file.read().split("\n")
        file.close()
        print(tekst)
        
        for element in tekst:
    
            liczba = element.split(" ")
            x = liczba[0]
            y = liczba[1]
            print(x)
            print(y)
            self.Set(int(x), int(y), True)
        
M = Map()
M.Fill("save1")
M.Display()
