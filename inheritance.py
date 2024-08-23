class quadilateral():
    def __init__(self , a, b , c , d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d 
    
    def parameter(self):
        p = self.side1 + self.side2 + self.side3  + self.side4
        print("parameter :" , p)
    


Q1 = quadilateral(7,5,8,4)
Q1.parameter()


class Rectangle(quadilateral):
    def __init__(self, a, b, c = None, d = None):
        super().__init__(a, b, c, d)
        self.side3 = self.side1
        self.side4 = self.side2
        
        
        
R1=Rectangle(10,20)
R1.parameter()
