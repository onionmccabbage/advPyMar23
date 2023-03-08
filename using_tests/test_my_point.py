import unittest
from my_point import Point

class testPoint(unittest.TestCase): # convention
    '''set up for tests then test the Point class'''
    def setUp(self): # this will run BEFORE every test
        super().setUp() # call the parent setUp
        # define an instance of a Point to be tested
        self.point = Point(3, 5)
    # here are the test cases
    def testMoveByXY(self):
        '''test we can move a point by x and y'''
        self.point.moveBy(5, 2)
        self.assertEqual( self.point.display(), (8, 7) )
    def testMoveByX(self):
        '''test we can move a point by x'''
        self.point.moveBy(5)
        self.assertEqual( self.point.display(), (8, 5) )
    def testMoveByY(self):
        '''test we can move a point by y'''
        self.point.moveBy(y=5)
        self.assertEqual( self.point.display(), (3, 10) )


if __name__ == '__main__':
    unittest.main() # always call the tests like this