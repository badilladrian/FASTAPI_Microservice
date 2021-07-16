from __future__ import annotations

from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

from utils.db import engine
BASE = automap_base()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True


class Plant(BaseModel):
    _id: int

    def __init__(self):
        pass

    def fech_all(self):
        pass

    def update(self, plant):
        if plant.id:
            self._id = plant.id

    def create(self, id: int):
        if id:
            self._id = id


class Bed(BaseModel):
    _id: int
    _plants: list[Plant]

    def __init__(self):
        pass

    def create(self, id: int, plants: list[Plant] = []):
        if id:
            self._id = id
        if plants:
            self._plants = plants

    def fech_all(self):
        pass

    def update(self, bed):
        if bed.id:
            self._id = bed.id
        if bed.plants:
            self._plants = bed.plants


class YardRequestCreate(BaseModel):
    _name: str


class Yard(Base):
    __tablename__ = 'yards'
    _id = Column('id', Integer, primary_key=True)
    _name = Column('name', String)

    def __init__(self, name) -> None:
        self._name = name

    def update(self, yard):
        if yard.id:
            self._id = yard.id
        if yard.name:
            self._name = yard.name

    @staticmethod
    def create(request: YardRequestCreate) -> Yard:
        return Yard(
            name=request._name,
        )

    def __repr__(self):
        return {'id': self._id, 'name': self._name}


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
    _entry_groups: list[EntryGroup]

    def __init__(self):
        pass

    def create(self, id: int, type: str, entry_groups: list[EntryGroup] = []):
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


class PlantFamilyRequestCreate(BaseModel):
    _plant_family: str

    def __repr__(self):
        return {'plant_family': self._plant_family}


class PlantFamily(Base):
    __tablename__ = 'plant_families'
    id = Column(Integer, primary_key=True)
    _plant_family = Column('plant_family', String)

    def __init__(self, plant_family) -> None:
        self._plant_family = plant_family

    def update(self, request):
        if request.id:
            self._id = request.id
        if request.plant_family:
            self._plant_family = request._plant_family

    @ staticmethod
    def create(request: PlantFamilyRequestCreate) -> PlantFamily:
        return PlantFamily(
            plant_family=request._plant_family,
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


BASE.prepare(engine, reflect=True)
