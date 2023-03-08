# this is main.py
import sys
import json
from swapi_service import SwapiService
from people import People
from vehicles import Vehicles
from planets import Planets
from species import Species

class Menu:
    categories = ('people', 'planets', 'species', 'vehicles')
    def __init__(self):
        self.menu_choices = {
            "1":self.getPeople,
            "2":self.getVehicles,
            "3":self.getPlanets,
            "4":self.getSpecies,
            "5":self.quit
        }
    def showMenu(self):
        print('''Choose an option:
        1: get people
        2: get vehicles
        3: get planets
        4: get species
        5: quit
        ''')
    def run(self):
        while True: # a run-loop
            self.showMenu()
            choice = input('option? ')
            action = self.menu_choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid option".format(choice))
    def getId(self):
        self.which_id = int(float(input('which number? '))) # cast the string to an int
        # check an int was entered
        if type(self.which_id) == int and 0<self.which_id<7:
            return self.which_id
        else:
            return 1 # default to id 1
    def getPeople(self):
        self.category = 'people'
        result_d = json.loads(SwapiService.getSwapi(self.category, self.getId()))
        self.people = People(result_d['name'], result_d['height'])
        result = "Name: {} Height: {}cm\n".format(self.people.name, self.people.height)
        print(result)
        self.appendData(result)
    def getPlanets(self):
        self.category = 'planets'
        result_d = json.loads(SwapiService.getSwapi(self.category, self.getId()))
        self.planets = Planets(result_d['name'], result_d['population'])
        print ("Name: {} Population: {}".format(self.planets.name, self.planets.population))
    def getSpecies(self):
        self.category = 'species'
        result_d = json.loads(SwapiService.getSwapi(self.category, self.getId()))
        self.species = Species(result_d['name'], result_d['classification'])
        print ("Name: {} Classification: {}".format(self.species.name, self.species.classification))
    def getVehicles(self):
        print('not currently working')
    def quit(self):
        sys.exit(0)
    def appendData(self,data_str):
        with open('swapi.txt', 'at') as fout:
            fout.writelines(data_str)

if __name__ == "__main__":
    Menu().run()