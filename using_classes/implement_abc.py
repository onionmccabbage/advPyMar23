from using_abc import AbscractShape

# here we create concrete shapes
class Shape(AbscractShape):
    def __init__(self, name):
        # no need to call __super__
        self.shape_name = name
    def __str__(self): # used by 'print'
        return (f'This shape has the name {self.shape_name}')
    @property
    def shape_name(self): # the getter method
        return self.__name # this is the actual property
    @shape_name.setter
    def shape_name(self, new_name): # the setter method
        # validate
        if type(new_name) == str and new_name != '':
            self.__name = new_name

if __name__ == '__main__':
    sqr = Shape('square')
    tri = Shape('triangle')

    print(sqr) # this will use __str__
    print(f'The name of the imported class is {AbscractShape.__name__}')