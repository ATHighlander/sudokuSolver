import numpy

class Board():
    def __init__(self):
        self.filling = 0
        self.line = list(np.repeat(filling,9))
        self.line1 = list(np.repeat(filling,9))
        self.line2 = list(np.repeat(filling,9))
        self.line3 = list(np.repeat(filling,9))
        self.line4 = list(np.repeat(filling,9))
        self.line5 = list(np.repeat(filling,9))
        self.line6 = list(np.repeat(filling,9))
        self.line7 = list(np.repeat(filling,9))
        self.line8 = list(np.repeat(filling,9))
        self.line9 = list(np.repeat(filling,9))
    
    def display(self):
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.line6)
        print(self.line7)
        print(self.line8)
        print(self.line9)