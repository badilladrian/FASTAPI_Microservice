from MVC.models import Bed
from MVC.models import BotanicalCategory
from MVC.models import EntryGroup
from MVC.models import EntryType
from MVC.models import Plant
from MVC.models import PlantFamily
from MVC.models import PlantFamilyRequestCreate
from MVC.models import Yard
from MVC.models import YardRequestCreate
from utils.db import session


class ControllerYards:
    _yards = list[Yard]

    def __init__(self):
        self._yards = self.get_all()

    def get_all(self):
        return (session.query(Yard).all())

    def create(self, request: list[YardRequestCreate]) -> list[Yard]:
        self._yards = [Yard.create(yard) for yard in request]
        session.add_all(self._yards)
        session.commit
        return self._yards


class ControllerBeds:
    def __init__(self):
        pass

    def get_all(self) -> dict:
        beds = self.fetch_all()
        return beds

    def fetch_all(self):
        beds = Bed()
        return beds.fech_all()


class ControllerPlants:
    def __init__(self):
        self._plant = Plant()
        pass

    def getOne(self):
        pass

    def get_all(self) -> dict:
        plants = self.fetch_all()
        return plants

    def fetch_all(self):
        plants = Plant()
        return plants.fech_all()

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class ControllerEntryGroups:
    _entry_group_model = EntryGroup

    def __init__(self):
        self._entry_group_model = EntryGroup()

    def get_all(self) -> dict:
        entry_groups = self.fetch_all()
        return ({
            'message': 'Listing all entry groups',
            'entry_groups': entry_groups,
        })

    def fetch_all(self):
        pass


class ControllerEntryTypes:
    _entry_type_model = EntryType

    def __init__(self):
        self._entry_type_model = EntryType()

    def get_all(self) -> dict:
        entry_types = self.fetch_all()
        return entry_types

    def fetch_all(self):
        pass


class ControllerPlantFamilies:
    _plant_families = list[PlantFamily]

    def __init__(self):
        self._yards = self.get_all()

    def create(self, plant_families_request: list[PlantFamilyRequestCreate]) -> list[PlantFamily]:
        self._plant_families = [
            PlantFamily.create(
                plant_family,
            ) for plant_family in plant_families_request
        ]
        session.add_all(self._plant_families)
        session.commit
        return self._plant_families

    def get_all(self) -> list[PlantFamily]:
        return (session.query(PlantFamily).all())


class ControllerBotanicalCategories:
    _botanical_category_model = BotanicalCategory

    def __init__(self):
        self._botanical_category_model = BotanicalCategory()

    def get_all(self) -> dict:
        pass

    def createModels(self, query):
        pass
