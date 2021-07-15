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


class EntryGroup():
    _id: int
    _group: str

    def __init__(self):
        pass

    def create(self, id: int, group: str):
        if id:
            self._id = id
        if group:
            self._group = group
        return self

    def update(self, entry_group):
        if entry_group.id:
            self._id = entry_group.id
        if entry_group.group:
            self._group = entry_group.group


class EntryType():
    _id: int
    _type: str
    _entry_groups: List[EntryGroup]

    def __init__(self):
        pass

    def create(self, id: int, type: str, entry_groups: List[EntryGroup] = []):
        if id:
            self._id = id
        if type:
            self._type = type
        if entry_groups:
            self._entry_groups = entry_groups
        return self

    def update(self, entry_type):
        if entry_type.id:
            self._id = entry_type.id
        if entry_type.type:
            self._type = entry_type.type
        if entry_type.entry_groups:
            self._entry_groups = entry_type.entry_groups


class PlantFamily():
    _id: int
    _plant_family: str

    def __init__(self):
        pass

    def create(self, id: int, plant_family: str):
        if id:
            self._id = id
        if plant_family:
            self._plant_family = plant_family
        return self

    def update(self, plant_family):
        if plant_family.id:
            self._id = plant_family.id
        if plant_family.plant_family:
            self._plant_family = plant_family.plant_family


class BotanicalCategory():
    _id: int
    _botanical_category: str

    def __init__(self):
        pass

    def create(self, id: int, botanical_category: str):
        if id:
            self._id = id
        if botanical_category:
            self._botanical_category = botanical_category
        return self

    def update(self, botanical_category):
        if botanical_category.id:
            self._id = botanical_category.id
        if botanical_category.botanical_category:
            self._botanical_category = botanical_category.botanical_category
