class Box:
    def __init__(self, w=0, l=0, h=0):
        self.__w= w
        self.__l= l
        self.__h= h

    def setW(self, w):
        self.__w= w

    def setL(self, l):
        self.__l= l

    def setH(self, h):
        self.__h= h

    def getVolume(self):
        return self.__w*self.__l*self.__h

    def __str__(self):
        return '(%d, %d, %d)' % (self.__w, self.__l, self.__h)

box= Box(100, 100, 100)
print(box)
print('상자의 부피는 ', box.getVolume())
