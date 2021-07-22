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

    def delete(self, id) -> bool:
        result = False
        yard = self.get_one(id)
        if yard:
            session.delete(yard)
            session.commit
            result = True
        return result


class ControllerBeds:
    _beds: List[Bed] = []

    def __init__(self) -> None:
        self._beds = self.get_all()

    # this method allows get one, get multi and get all
    def get(self, request: Optional[List[int]] = None) -> List[Bed]:
        self._beds = []
        if (request):
            for id in request:
                bed = self.get_one(id)
                if (bed):
                    self._beds.append(bed)
        else:
            beds = self.get_all()
        return beds

    def get_all(self) -> List[Bed]:
        return session.query(Bed).all()

    def get_one(self, id: int) -> Bed:
        return session.query(Bed).get(id)

    def create(self, request: list[BedRequestCreate]) -> list[Bed]:
        self._beds = [Bed.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds

    def delete(self, id) -> bool:
        result = False
        bed = self.get_one(id)
        if bed:
            session.delete(bed)
            session.commit
            result = True
        return result


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

    def delete(self, id) -> bool:
        result = False
        plant = self.get_one(id)
        if plant:
            session.delete(plant)
            session.commit
            result = True
        return result
