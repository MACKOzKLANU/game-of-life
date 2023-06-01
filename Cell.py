class Cell:
    def __init__(self) -> None:
        self.isAlive = False
        
    def Switch(self):
        if self.isAlive:
            self.isAlive = False
        else:
            self.isAlive = True