#композиция и агрегироание 
class Win_Door:
    def __init__(self,x,y):
        self._square=x*y
       

class Room:
    def __init__(self, x, y,z):
        self._widht=x
        self._height=z
        self._lenght=y
        
    def square_calc(self):
        self._square=2*self.__height*self.__widht+2*self.__height*self.__widht