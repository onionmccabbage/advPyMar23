# Planets class
from swapi import Swapi

class Planets(Swapi):
    def __init__(self, name, population):
        super().__init__(name)
        self.population = population
    @property
    def population(self):
        return self.__population
    
    @population.setter
    def population(self, value):
        self.__population  = value