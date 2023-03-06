from review_abstract import Review
import review1a
import review1b

class ReviewOne(Review):
    def __init__(self, min, max):
        self.min = min # use the setter method
        self.max = max
    def __str__(self):
        return 'Review One min:{} max:{}'.format(self.min, self.max) # use the accesors
    @property
    def min(self):
        return self.__min
    @min.setter
    def min(self, min):
        if type(min) == int:
            self.__min = min
        else:
            self.__min = 0
    @property
    def max(self):
        return self.__max
    @max.setter
    def max(self, max):
        if type(max) == int:
            self.__max = max
        else:
            self.__max = 10 # a sensible default
    # use imported functions
    def mapSquareRoots(self):
        review1a.mapRoots(self.min, self.max)
    def filterSquares(self):
        review1b.filterSquares(self.min, self.max)

if __name__ == '__main__':
    r = ReviewOne(-100, 100)
    print(r)
    r.mapSquareRoots()
    r.filterSquares()