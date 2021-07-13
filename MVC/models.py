from typing import List

from utils.db import Database


class Plant():
    _id: int

    def __init__(self):
        pass

    def fech_all(self):
        db = Database()
        query = 'SELECT * FROM plant'
        plants = db.execute(query)
        return plants

    def update(self, plant):
        if plant.id:
            self._id = plant.id

    def create(self, id: int):
        if id:
            self._id = id


class Bed():
    _id: int
    _plants: List[Plant]

    def __init__(self):
        pass

    def create(self, id: int, plants: List[Plant] = []):
        if id:
            self._id = id
        if plants:
            self._plants = plants

    def fech_all(self):
        db = Database()
        query = 'SELECT * FROM bed'
        beds = db.execute(query)
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

    def __init__(self):
        pass

    def create(self, id: int, name: str, location: str, beds: List[Bed] = []):
        if id:
            self._id = id
        if name:
            self._name = name
        if location:
            self._location = location
        if beds:
            self._beds = beds
        return self

    def fecth_all(self):
        db = Database()
        query = 'SELECT * FROM yard'
        yards = db.execute(query)
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
