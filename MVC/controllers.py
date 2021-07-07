yards = [{"name":"home","location":"LA","beds":[{"id": 1,"plants":[{"id": 2}]},{"id": 2,"plants":[{"id": 3}]}]},{"name":"favorite","location":"MI","beds":[{"id": 3,"plants":[{"id": 1}]}]}]
beds = [{"id": 1,"plants":[{"id": 2}]},{"id": 2,"plants":[{"id": 3}]},{"id": 3,"plants":[{"id": 1}]}]
plants = [{"id":1},{"id": 2},{"id": 3}]


class ControllerYards:
    def __init__(self):
        pass

        
    def get_all(self) -> dict:
        return ({"message":"Listing all yards","yards":yards})


class ControllerBeds:
    def __init__(self):
        pass

        
    def get_all(self) -> list:
        return ({"message":"Listing all beds","beds":beds})
        

class ControllerPlants:
    def __init__(self):
        pass

        
    def get_all(self) -> list:
        return ({"message":"Listing all plants","plants":plants})
