from abc import ABCMeta, abstractmethod
# Abscraction brings some rigour to our code

# declare an abscract shape
class AbscractShape():
    '''Abscract Classes do not implement any detail - they are abstract'''
    @abstractmethod
    def __str__(self):# we can override the built-in 'print' capability with __str__
        pass
    @abstractmethod
    def shape_name(self, new_name):
        pass


# then create concrete shapes inherit from abscract shape


if __name__ == '__main__':
    pass