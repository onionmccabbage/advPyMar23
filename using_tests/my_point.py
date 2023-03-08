class Point(object):
    '''
    Define a point in 2-d space by x and y integer parameters
    Derive the hypotenuse from x and y
    Allow the point to move by dx and dy
    '''
    points = 0 # a count of how many points have been instantiated
    def __init__(self, x, y):
        '''call setter methods for __x and __y'''
        self.x = x
        self.y = y # call the setter for __y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==int:
            self.__y = new_y
        else:
            raise TypeError
    # derive the hypotenuse
    def hypot(self):
        h = (self.__x**2 + self.__y**2)**0.5 # raise to 0.5 will return square root
        return h
    def moveBy(self, dx, dy):
        ''' move the point by dx and dy'''
        self.x += dx
        self.y += dy
    def display(self):
        return (self.__x, self.__y) # a tuple of x and y values