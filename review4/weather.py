from random import randint
from threading import Thread

class Weather(Thread):
    '''
    The Weather class takes a non-empty string for the description
    and a floating point number for the temperature
    '''
    def __init__(self, desc, temp):
        Thread.__init__(self)
        self.desc = desc # make use of the setter methods
        self.temp = temp
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str and new_desc != '':
            self.__desc = new_desc
        else:
            self.__desc = 'fine'
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) == int or type(new_temp) == float:
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def changeTemp(self):
        # alter the temperature by a small random amount
        tempChange = randint(-5, 5) 
        self.temp += tempChange
    def __str__(self):
        # output a nicely formatted weather report
        report  = 'The weather is {0} at {1:.2f}C'.format(self.__desc, self.__temp)
        return report
    def run(self):
        '''return a nicely formatted weather report'''
        print( self.__str__() )

if __name__ == '__main__':
    # exercise this module
    w_1 = Weather('rainy', 9.04)
    w_2 = Weather('windy', 6.70)
    w_3 = Weather('Sunny', 27.98)
    
    w_1.changeTemp()
    w_1.start()
    w_2.start()
    w_3.start()

    w_1.join()
    w_2.join()
    w_3.join()
    # check the default values work in the validators
    w_default = Weather([], ()) # wrong data types so should fall back to the defaults
    print(w_default)
