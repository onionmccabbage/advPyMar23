# a service to access https://swapi.co/api
import requests

class SwapiService:
    def __init__(self):
        pass
    @staticmethod
    def getSwapi(category, id): # no need for self this time (since its a static method)
        url = "https://swapi.dev/api/{}/{}".format(category, id)
        print(url)
        response = requests.get(url)
        return response.text

if __name__ == "__main__":
    SwapiService().__init__()