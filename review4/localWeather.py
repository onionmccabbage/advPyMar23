from countries import countries
from weather import Weather
from threading import Lock
import os


# some gloabl assets
lock = Lock()
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

class LocalWeather(Weather): # inherit from our Weather class
    def __init__(self, city='Athlone', country='ie', desc='fine', temp=12): # sensible defaults
        super().__init__(desc, temp) # we call the parent class constructor
        self.city = city
        self.country = country # use the setter method
    def __str__(self):
        loc = 'Local weather in {}, {} is {} at {:.2f}C'.format(self.__city, self.country, self.desc, self.temp)
        return loc
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and new_city != '':
            self.__city = new_city
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, new_country):
        if type(new_country) == str and new_country !='' and new_country in countries:
            self.__country = new_country
        else:
            self.__country = 'uk' # default
    def run(self):
        '''write to an exclusively locked text file'''
        lock.acquire()
        with open(f'{CURR_DIR}/weather.txt', 'at') as fout:
            fout.write(self.__str__())
            fout.write('\n') # add a new line character to the output file
        lock.release()

def main():
    l1 = LocalWeather('Edinburgh', 'uk', 'rainy', -3.7)
    l2 = LocalWeather('Galway', 'ie', 'humid', 5)
    l3 = LocalWeather('Kingston', 'jm', 'sunny', 32)
    # chck the defaults work as expected
    l4 = LocalWeather('Begonia', 'es', True ,True)
    weather_t = (l1,l2, l3, l4)
    for w in weather_t:
        w.start()
    for w in weather_t:
        w.join()

if __name__ == '__main__':
    main()