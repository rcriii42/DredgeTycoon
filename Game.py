"""Game.py - Contains the Game object that holds all objects in the game - players, cities, 
   dredges, and the game world."""
# Model 
import datetime
from City import City
from Player import Player
Demo=True
days_to_hours = 24.


def comprehension_flatten(iter_lst):
    return list(item for iter_ in iter_lst for item in iter_)


class Game(object):
    """Holds the various game objects"""
    def __init__(self):
        self.date = datetime.datetime(1920, 1, 1)
        self.cities = [City(self.date, "Boston", (375,20)),
                       City(self.date, "New York", (400,80)),
                       City(self.date, "Jacksonville", (5,425)),
                       ]
        self.players = [Player()]    
        self.date = datetime.datetime(1920,1,1)
    
    @property
    def dredges(self):
        """return a list of all dredges"""
        return comprehension_flatten([p.dredges for p in self.players]) # this returns a flat list of all dredges
    
    @property
    def projects(self):
        """return a list of projects"""
        return comprehension_flatten([c.projects for c in self.cities]) # this returns a flat list of projects underway
