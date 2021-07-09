from MVC.models import Yard, Bed, Plant

class ControllerYards:
    def __init__(self):
        pass

        
    def get_all(self) -> dict:
        yards = self.fetch_all()
        return ( { "message" : "Listing all yards", "yards" : yards } )


    def fetch_all(self):
        return Yard.fech_all()


class ControllerBeds:
    def __init__(self):
        pass

        
    def get_all(self) -> list:
        beds = self.fetch_all()
        return ({"message":"Listing all beds","beds":beds})
        

    def fetch_all(self):
        return Bed.fech_all()

class ControllerPlants:
    def __init__(self):
        pass

        
    def get_all(self) -> list:
        plants = self.fetch_all()
        return ({"message":"Listing all plants","plants":plants})


    def fetch_all(self):
        return Plant.fech_all()