from fastapi import FastAPI
from fastapi import Request

from MVC.controllers import ControllerBeds
from MVC.controllers import ControllerEntryGroups
from MVC.controllers import ControllerPlants
from MVC.controllers import ControllerYards


yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()
entry_group_controller = ControllerEntryGroups()
app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'This is the best farmer assistence app ever!',
    }


@app.get('/yard')
def get_all_yards():
    yards = yards_controller.get_all()
    return ({'message': 'Listing all yards', 'yards': yards})


@app.get('/bed')
def get_all_beds():
    beds = beds_controller.get_all()
    return ({'message': 'Listing all beds', 'beds': beds})


@app.get('/plant')
def get_all_plants():
    plants = plants_controller.get_all()
    return {
        'message': 'Listing all plants',
        'plants': plants,
    }


@app.get('/entry_group')
def get_all_entry_groups():
    entry_groups = entry_group_controller.get_all()
    return ({
        'message': 'Listing all entry groups',
        'entry_groups': entry_groups,
    })


@app.post('/yard')
def create_yard(request: Request):
    return dir(request)


@app.post('/bed')
def create_bed():
    beds = beds_controller.get_all()
    return ({'message': 'Listing all beds', 'beds': beds})


@app.post('/plant')
def create_plant():
    plants = plants_controller.get_all()
    return {
        'message': 'Listing all plants',
        'plants': plants,
    }
