from MVC.models import Bed
from MVC.models import BedRequestCreate
from MVC.models import Plant
from MVC.models import PlantRequestCreate
from MVC.models import Yard
from MVC.models import YardRequestCreate
from utils.db import session


class ControllerYards:
    _yards = list[Yard]

    def __init__(self):
        self._yards = self.get_all()

    def get_all(self):
        return (session.query(Yard).all())

    def get(self, id: int) -> Yard:
        return (session.query(Yard).all())

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
