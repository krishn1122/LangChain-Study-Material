class twoDarray:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector of 2D Array are: {self.i}i +{self.j}j")

class threeDarray(twoDarray):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the vectors of 3D array are: {self.i}i+ {self.j}j+ {self.k}k")

a=twoDarray(1,2)
a.show()
b=threeDarray(1,2,3)
b.show()