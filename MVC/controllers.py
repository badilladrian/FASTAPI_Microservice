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
        self._yards = self.get_all()

    def get_multi(self, request: Optional[List[int]] = None) -> List[Yard]:
        yards: List[Yard] = []
        if (request):
            for id in request:
                yard = self.get_one(id)
                if (yard):
                    yards.append(yard)
        else:
            yards = self.get_all()
        return yards

    def get_all(self) -> List[Yard]:
        return session.query(Yard).all()

    def get_one(self, id) -> Yard:
        return session.query(Yard).get(id)

    def create(self, request: list[YardRequestCreate]) -> list[Yard]:
        self._yards = [Yard.create(yard) for yard in request]
        session.add_all(self._yards)
        session.commit
        return self._yards


class ControllerBeds:
    _beds = list[Bed]

    def __init__(self):
        self._beds = self.get_all()

    def get_all(self) -> dict:
        return (session.query(Bed).all())

    def create(self, request: list[BedRequestCreate]) -> list[Bed]:
        self._beds = [Bed.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds


class ControllerPlants:
    _plants = list[Plant]

    def __init__(self):
        self._plants = self.get_all()
        pass

    def get_all(self) -> dict:
        return (session.query(Plant).all())

    def create(self, request: list[PlantRequestCreate]) -> list[Plant]:
        self._beds = [Plant.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds
