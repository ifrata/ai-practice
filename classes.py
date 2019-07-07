class shape():
    def __init__(self,sides,color):
        self.sides=sides
        self.color=color

    def showsides(self):
        print("the sides are", self.sides)

    def showcolor(self):
        print("the color is",self.color)

triangle=shape(3,"yellow") 
ab=shape(2,"red") 
ab.showcolor()
triangle.showcolor()
triangle.showsides()