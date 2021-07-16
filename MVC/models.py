from __future__ import annotations

from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.db import engine
Base = declarative_base()


class YardRequestCreate(BaseModel):
    name: str


class Yard(Base):
    __tablename__ = 'yards'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    beds = relationship('Bed')

    def __init__(self, name) -> None:
        self.name = name

    def update(self, yard):
        if yard.id:
            self.id = yard.id
        if yard.name:
            self.name = yard.name

    @staticmethod
    def create(request: YardRequestCreate) -> Yard:
        return Yard(
            name=request.name,
        )

    def __repr__(self):
        return {'id': self.id, 'name': self.name, 'beds': self.beds}


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
    def create(request: BedRequestCreate) -> Plant:
        return Bed(request.yard)

    def __repr__(self):
        return {'id': self.id, 'yard': self.yard_id, 'plants': self.plants}


class PlantRequestCreate(BaseModel):
    bed: int


class Plant(Base):
    __tablename__ = 'plants'
    id = Column('id', Integer, primary_key=True)
    bed_id = Column('bed_id', Integer, ForeignKey('beds.id'))

    def __init__(self, bed) -> None:
        self.bed_id = bed
        pass

    @staticmethod
    def create(request: PlantRequestCreate) -> Plant:
        return Plant(request.bed)

    def __repr__(self):
        return {'id': self.id, 'bed': self.bed_id}


Base.metadata.create_all(engine)
