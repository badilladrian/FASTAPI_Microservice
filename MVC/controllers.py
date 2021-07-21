from typing import List, Optional

from MVC.models import (
    Bed,
    BedRequestCreate,
    Plant,
    PlantRequestCreate,
    Yard,
    YardRequestCreate,
)

from utils.db import session


class ControllerYards:
    _yards: List[Yard] = []

    def __init__(self):
        self._yards = self.get()

    # this method allows get one, get multi and get all
    def get(self, request: Optional[List[int]] = None) -> List[Yard]:
        self._yards = []
        if (request):
            for _ in request:
                yard = session.query(Yard).get(_)
                if (yard):
                    self._yards.append(yard)
        else:
            self._yards = (session.query(Yard).all())
        return self._yards

    def create(self, request: list[YardRequestCreate]) -> list[Yard]:
        self._yards = [Yard.create(yard) for yard in request]
        session.add_all(self._yards)
        session.commit
        return self._yards


class ControllerBeds:
    _beds: List[Bed] = []

    def __init__(self) -> None:
        self._beds = self.get()

    # this method allows get one, get multi and get all
    def get(self, request: Optional[List[int]] = None) -> List[Bed]:
        self._beds = []
        if (request):
            for _ in request:
                bed = session.query(Bed).get(_)
                if (bed):
                    self._beds.append(bed)
        else:
            self._beds = (session.query(Bed).all())
        return self._beds

    def create(self, request: list[BedRequestCreate]) -> list[Bed]:
        self._beds = [Bed.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds


class ControllerPlants:
    _plants: List[Plant] = []

    def __init__(self) -> None:
        self._plants = self.get_all()

    # this method allows get one, multi and all
    def get_multi(self, request: Optional[List[int]] = None) -> List[Plant]:
        plants = []
        if (request):
            for id in request:
                plant = self.get_one(id)
                if (plant):
                    plants.append(plant)
        else:
            plants = self.get_all()
        return plants

    def get_one(self, id) -> Plant:
        return session.query(Plant).get(id)

    def get_all(self) -> List[Plant]:
        return session.query(Plant).all()

    def create(self, request: list[PlantRequestCreate]) -> list[Plant]:
        self._beds = [Plant.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds
