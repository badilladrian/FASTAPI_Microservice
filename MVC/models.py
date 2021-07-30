from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.db import engine

import logging


Base = declarative_base()


# Setting logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s:%(name)s-%(levelname)ss:%(message)s")
file_handler = logging.FileHandler("logs/models.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


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
        """
            Create a new yard.

        Args:
            name(str): the name that is going to be provided to the new yard.
        Returns:
            None
        Raises:
            None
        """
        logger.debug(f"Executing Yard __init__ with name:{name}")
        self._name = name

    @staticmethod
    def create(request: YardRequestCreate) -> Yard:
        """
            Return a new yard.

        Args:
            request(YardRequestCreate): this object could have the following attributes:
                name(str)
        Returns:
            A Yard object
        Raises:
            None
        """
        logger.debug(f"Executing Yard create with request:{request}")
        return Yard(request.name)

    def update(self, request: YardRequestUpdate) -> None:
        """
            Update a yard.

        Args:
            request(YardRequestUpdate): this object could have the following attributes:
                id(int)
                name(str)
        Returns:
            None
        Raises:
            None
        """
        logger.debug(f"Executing Yard update with request:{request}")
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

    def __init__(self, yard_id: int) -> None:
        """
            Create a new bed.

        Args:
            yard_id(int): the id corresponding to the yard which the bed belongs.
        Returns:
            None
        Raises:
            None
        """
        logger.debug(f"Executing Bed __init__ with yard_id:{yard_id}")
        self._yard_id = yard_id

    @staticmethod
    def create(request: BedRequestCreate) -> Bed:
        """
            Return a new bed.

        Args:
            request(BedRequestCreate): this object could have the following attributes:
                yard_id(int)
        Returns:
            A Bed object
        Raises:
            None
        """
        logger.debug(f"Executing Bed create with request:{request}")
        return Bed(request.yard_id)

    def update(self, request: BedRequestUpdate) -> None:
        """
            Update a bed.

        Args:
            request(BedRequestUpdate): this object could have the following attributes:
                id(int)
                yard_id(int)
        Returns:
            None
        Raises:
            None
        """
        logger.debug(f"Executing Bed update with request:{request}")
        if request.id:
            self._id = request.id
        if request.yard_id:
            self._yard_id = request.yard_id

    def __repr__(self):
        return {'id': self._id, 'yard_id': self._yard_id, 'plants': self._plants}


class PlantRequestUpdate(BaseModel):
    id: Optional[int]
    name: Optional[str]


class PlantRequestCreate(BaseModel):
    name: str
    bed_id: int


class Plant(Base):
    __tablename__ = 'plants'
    _id = Column('id', Integer, primary_key=True)
    _name = Column('name', String)
    _bed_id = Column('bed_id', Integer, ForeignKey('beds.id'))

    def __init__(self, name, bed_id) -> None:
        """
            Create a new plant.

        Args:
            name(str): the corresponding name for the new plant.
            bed_id(int): the corresponding id for bed which the plant belogs.
        Returns:
            None
        Raises:
            None
        """
        logger.debug(
            f"Executing Plant __init with name:{name}, bed_id:{bed_id} ")
        self._name = name
        self._bed_id = bed_id

    @staticmethod
    def create(request: PlantRequestCreate) -> Plant:
        """
            Return a new Plant.

        Args:
            request(PlantRequestCreate): this object could have the following attributes:
                bed_id(int)
                name(str)
        Returns:
            A Plant object
        Raises:
            None
        """
        logger.debug(f"Executing Plant create with request:{request}")
        return Plant(request.name, request.bed_id)

    def update(self, request: PlantRequestUpdate) -> None:
        """
            Update a plant.

        Args:
            request(PlantRequestUpdate): this object could have the following attributes:
                id(int)
                name(str)
        Returns:
            None
        Raises:
            None
        """
        logger.debug(f"Executing Plant update with request:{request}")
        if request.id:
            self._id = request.id
        if request.name:
            self._name = request.name

    def __repr__(self):
        return {'id': self._id, 'name': self._name, 'bed_id': self._bed_id}


Base.metadata.create_all(engine)
