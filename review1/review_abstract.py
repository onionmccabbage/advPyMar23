from abc import ABCMeta, abstractmethod, abstractproperty

# we can declare an abstract top-level class
class Review():
    __metaclass__ = ABCMeta
    @abstractmethod
    def __str__(self):
        pass
    @abstractproperty
    def min(self):
        pass
    @abstractproperty
    def max(self):
        pass
