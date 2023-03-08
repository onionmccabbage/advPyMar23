# generic class for others to descend from

class Swapi(list):
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

if __name__ == "__main__":
    Swapi().__init__()