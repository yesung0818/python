import math
class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius

    def setradius(self, r):
        self.__radius=r

    def getradius(self):
        return self.__radius

    def calcArea(self):
        area= math.pi*self.__radius*self.__radius
        return area

    def calcCircum(self):
        circumference= 2.0*math.pi*self.__radius
        return circumference

c1= Circle(10)
print("원의 반지름=",c1.getradius())
print("원의 넓이=",c1.calcArea())
print("원의 둘레=",c1.calcCircum())
    
