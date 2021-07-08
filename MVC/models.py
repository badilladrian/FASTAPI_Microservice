import json

class Yard():
    id: int
    name: str
    location: str
    beds: list


    def __init__(self,id:int, name:str, location:str, bets:list=[]):
        self.id = id
        self.name = name
        self.location = location
        self.bets = bets


    def fech_all():
        data_file  = open('./utils/data.json',)
        yards = json.loads(data_file.read())["yards"]
        return yards


    def update(self, yard):
        self.id = yard.id
        self.name = yard.usenamername
        self.location = yard.location
        self.bets = yard.bets



class Bed():
    id: int
    plants: list


    def __init__(self,id:int, plants:list=[]):
        self.id = id
        self.plants = plants


    def fech_all():
        data_file  = open('./utils/data.json',)
        beds = json.loads(data_file.read())["beds"]
        return beds


    def update(self, bed):
        self.id = bed.id
        self.plants = bed.plants


class Plant():
    id: int


    def __init__(self,id:int):
        self.id = id


    def fech_all():
        data_file  = open('./utils/data.json',)
        plants = json.loads(data_file.read())["plants"]
        return plants


    def update(self, plant):
        self.id = plant.id