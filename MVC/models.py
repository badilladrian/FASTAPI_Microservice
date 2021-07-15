from typing import List

from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.automap import automap_base

from utils.db import engine

Base = automap_base()


class Plant(BaseModel):
    _id: int

    def __init__(self):
        pass

    def fech_all(self):
        # db = Database()
        query = 'SELECT * FROM plant'
        plants = db.execute(query)
        return plants

    def update(self, plant):
        if plant.id:
            self._id = plant.id

    def create(self, id: int):
        if id:
            self._id = id


class Bed(BaseModel):
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
        # db = Database()
        query = 'SELECT * FROM bed'
        beds = db.execute(query)
        return beds

    def update(self, bed):
        if bed.id:
            self._id = bed.id
        if bed.plants:
            self._plants = bed.plants


class YardRequestCreate(BaseModel):
    name: str


class Yard(Base):
    __tablename__ = 'yards'
    id = Column(Integer, primary_key=True)
    name: Column('name', String)

    def update(self, yard):
        if yard.id:
            self.id = yard.id
        if yard.name:
            self.name = yard.name

    @staticmethod
    def create(yard: YardRequestCreate):
        if yard.name:
            return Yard(
                name=yard.name,
            )

    def __repr__(self):
        return {'id': self.id, 'name': self.name}


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


class PlantFamilyCreate(BaseModel):
    plant_family: str


class PlantFamily(Base):
    __tablename__ = 'plant_families'
    id = Column(Integer, primary_key=True)
    plant_family: Column('plant_family', String)

    def update(self, plant_family):
        if plant_family.id:
            self._id = plant_family.id
        if plant_family.plant_family:
            self._plant_family = plant_family.plant_family

    @staticmethod
    def create(yard: PlantFamilyCreate):
        if yard.plant_family:
            return PlantFamily(
                plant_family=yard.plant_family,
            )

    def __repr__(self):
        return {'id': self._id, 'plant_family': self._plant_family}


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


Base.prepare(engine, reflect=True)
