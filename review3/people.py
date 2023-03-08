# People class
from swapi import Swapi

class People(Swapi):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value