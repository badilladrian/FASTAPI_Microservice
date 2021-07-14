from MVC.models import Bed
from MVC.models import EntryGroup
from MVC.models import Plant
from MVC.models import Yard
from utils import db

DATABASE = db.Database()


class ControllerYards:
    _yard_model = Yard

    def __init__(self):
        self._yard_model = Yard()

    def get_all(self) -> dict:
        yards = self.fetch_all()
        return ({'message': 'Listing all yards', 'yards': yards})

    def fetch_all(self):
        query = 'SELECT Y.yard_id as id,',
        'Y.yard_name as name,',
        'Y.yard_location as location,',
        'B.bed_id as bed',
        'FROM YARD as Y, BED as B',
        'WHERE B.yard_id = Y.yard_id'
        query_result = DATABASE.execute(query)
        print(query_result)
        result = self.createModels(query_result)
        return result

    def createModels(self, query):
        print(query)
        return [
            self._yard_model.create(item[0], item[1], item[2], item[3])
            for item in query
        ]


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
        query = 'SELECT id FROM PLANT where id=1'
        result = DATABASE.execute(query)
        # result = self._plant.create(result)
        return result

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
        query = 'SELECT * FROM entry_groups'
        query_result = DATABASE.execute(query)
        # print(query_result)
        # result = self.createModels(query_result)
        return query_result

    def createModels(self, query):
        pass
