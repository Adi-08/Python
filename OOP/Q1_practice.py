'''
Qs. Define a Circle class to create a circle with radius r using the constructor.

Define an Area( method of the class which calculates the area of the circle.

Define a PerimeterO method of the class which allows you to calculate the perimeter of the circle.

'''
class Circle:
    def __init__(self, r):
        self.r =r

    def Area(self,pi = 3.14):
        print(pi * self.r * self.r)

    def Perimeter(self):
        return 2 * 3.14 * self.r 

c1 = Circle(4)
c1.Area()
print(c1.Perimeter())