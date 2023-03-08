import unittest
from my_point import Point

class testPoint(unittest.TestCase): # convention
    '''set up for tests then test the Point class'''
    def setUp(self): # this will run BEFORE every test
        super().setUp() # call the parent setUp
        # define an instance of a Point to be tested
        self.point = Point(3, 5) # since each test gets a fresh point, they remain independent
    # here are the test cases
    def testMoveByXY(self):
        '''test we can move a point by x and y'''
        self.point.moveBy(5, 2)
        self.assertEqual( self.point.display(), (8, 7) )
    def testMoveByX(self):
        '''test we can move a point by x'''
        self.point.moveBy(5) # pass x as a positional argument
        self.assertEqual( self.point.display(), (8, 5) )
    def testMoveByY(self):
        '''test we can move a point by y'''
        self.point.moveBy(dy=5) # pass y as a keyword argument
        self.assertEqual( self.point.display(), (3, 10) )
    def testHypot(self):
        '''test that the hypotenuse is derived as expected'''
        self.point.moveBy(dy=-1) # point is now (3, 4)
        h = self.point.hypot()
        self.assertEqual(h, 5.00)

if __name__ == '__main__':
    unittest.main() # always call the tests like this