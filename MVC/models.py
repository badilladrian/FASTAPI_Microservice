from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.db import engine

Base = declarative_base()


class YardRequestUpdate(BaseModel):
    id: Optional[int]
    name: Optional[str]


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
        if request.id:
            self._id = request.id
        if request.name:
            self._name = request.name

    def __repr__(self):
        return {'id': self._id, 'name': self._name, 'beds': self._beds}


class BedRequestUpdate(BaseModel):
    id: Optional[int]
    yard_id: Optional[int]


class BedRequestCreate(BaseModel):
    yard_id: int


class Bed(Base):
    __tablename__ = 'beds'
    _id = Column('id', Integer, primary_key=True)
    _yard_id = Column('yard_id', Integer, ForeignKey('yards.id'))
    _plants = relationship('Plant')

    def __init__(self, id: int) -> None:
        self._yard_id = id

    @staticmethod
    def create(request: BedRequestCreate) -> Bed:
        return Bed(request.yard_id)

    def update(self, request: BedRequestUpdate) -> None:
        if request.id:
            self._id = request.id
        if request.yard_id:
            self._yard_id = request.yard_id

    def __repr__(self):
        return {'id': self._id, 'yard_id': self._yard_id, 'plants': self._plants}


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
