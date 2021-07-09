import json
from typing import List


class Plant():
    _id: int


    def __init__(self,id:int):
        self._id = id


    def fech_all():
        data_file  = open('./utils/data.json',)
        plants = json.loads(data_file.read())["plants"]
        return plants


    def update(self, plant):
        if plant.id:
            self._id = plant.id


class Bed():
    _id: int
    _plants: List[Plant]


    def __init__(self,id:int, plants:List[Plant]=[]):
        self._id = id
        self._plants = plants


    def fech_all():
        data_file  = open('./utils/data.json',)
        beds = json.loads(data_file.read())["beds"]
        return beds


    def update(self, bed):
        if bed.id:
            self._id = bed.id
        if bed.plants:
            self._plants = bed.plants


class Yard():
    _id: int
    _name: str
    _location: str
    _beds: List[Bed]


    def __init__(self,id:int, name:str, location:str, beds:List[Bed]=[]):
        self._id = id
        self._name = name
        self._location = location
        self._beds = beds 


    def fech_all():
        data_file  = open('./utils/data.json',)
        yards = json.loads(data_file.read())["yards"]
        return yards


    def update(self, yard):
        if yard.id:
            self._id = yard.id
        if yard.name:
            self._name = yard.name
        if yard.location:
            self._location = yard.location
        if yard.beds:
            self._beds = yard.beds


