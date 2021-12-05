import requests

class Brawery:
    def __init__(self):
        pass

    def __str__(self, name: str):
        self.name = name

response = requests.get("https://api.openbrewerydb.org/breweries")
