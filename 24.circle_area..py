'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle'''

import math
class Circle:
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return math.pi*self.r*self.r

    def perimeter(self):
        return 2*math.pi*self.r
a=Circle(7)
print(f"Area of circle{a.area()}")
print(f"Perimeter of circle{a.perimeter()}")

        
        
