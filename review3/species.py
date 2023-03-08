# Species class
from swapi import Swapi

class Species(Swapi):
    def __init__(self, name, classification):
        super().__init__(name)
        self.classification = classification
    @property
    def classification(self):
        return self.__classification
    
    @classification.setter
    def classification(self, value):
        self.__classification = value