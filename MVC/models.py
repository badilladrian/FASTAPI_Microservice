from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.db import engine

Base = declarative_base()


class YardRequestUpdate(BaseModel):
    id: int
    name: Optional[str]
    new_id: Optional[int]


class YardRequestCreate(BaseModel):
    name: str


class Yard(Base):
    __tablename__ = 'yards'
    _id = Column('id', Integer, primary_key=True)
    _name = Column('name', String)
    _beds = relationship('Bed')

    def __init__(self, name: str) -> None:
        self._name = name

    @staticmethod
    def create(request: YardRequestCreate) -> Yard:
        return Yard(request.name)

    def update(self, request: YardRequestUpdate) -> None:
        if request.new_id:
            self._id = request.new_id
        if request.name:
            self._name = request.name

    def __repr__(self):
        return f'id {self._id} name {self._name} beds {self._beds}'


class BedRequestCreate(BaseModel):
    yard: int


class Bed(Base):
    __tablename__ = 'beds'
    id = Column('id', Integer, primary_key=True)
    yard_id = Column('yard_id', Integer, ForeignKey('yards.id'))
    plants = relationship('Plant')

    def __init__(self, yard) -> None:
        self.yard_id = yard

    @staticmethod
    def create(request: BedRequestCreate) -> Bed:
        return Bed(request.yard)

    def __repr__(self):
        return {'id': self.id, 'yard': self.yard_id, 'plants': self.plants}


class PlantRequestCreate(BaseModel):
    name: str
    bed_id: int


class Plant(Base):
    __tablename__ = 'plants'
    _id = Column('id', Integer, primary_key=True)
    _name = Column('name', String)
    _bed_id = Column('bed_id', Integer, ForeignKey('beds.id'))

    def __init__(self, name, bed_id) -> None:
        self._nane = name
        self._bed_id = bed_id

    @staticmethod
    def create(request: PlantRequestCreate) -> Plant:
        return Plant(request.name, request.bed_id)

    def __repr__(self):
        return {'id': self._id, 'name': self._name, 'bed_id': self._bed_id}


Base.metadata.create_all(engine)
