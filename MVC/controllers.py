from typing import List
from typing import Optional

from MVC.models import Bed
from MVC.models import BedRequestCreate
from MVC.models import Plant
from MVC.models import PlantRequestCreate
from MVC.models import Yard
from MVC.models import YardRequestCreate
from utils.db import session


class ControllerYards:
    _yards: List[Yard] = []

    def __init__(self):
        self._yards = self.get()

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
        self._plants = self.get()

    # this method allows get one, get multi and get all
    def get(self, request: Optional[List[int]] = None) -> List[Plant]:
        self._plants = []
        if (request):
            for _ in request:
                plant = session.query(Plant).get(_)
                if (plant):
                    self._plants.append(plant)
        else:
            self._plants = (session.query(Plant).all())
        return self._plants

    def create(self, request: list[PlantRequestCreate]) -> list[Plant]:
        self._beds = [Plant.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds
