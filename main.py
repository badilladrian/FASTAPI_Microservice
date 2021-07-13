from fastapi import FastAPI

from MVC.controllers import ControllerBeds
from MVC.controllers import ControllerPlants
from MVC.controllers import ControllerYards

yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()
app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'This is the best farmer assistence app ever!',
    }


@app.get('/yards')
def get_all_yards():
    yards = yards_controller.get_all()
    return ({'message': 'Listing all yards', 'yards': yards})


@app.get('/beds')
def get_all_beds():
    beds = beds_controller.get_all()
    return ({'message': 'Listing all beds', 'beds': beds})


@app.get('/plants')
def get_all_plants():
    plants = plants_controller.get_all()
    return {
        'message': 'Listing all plants',
        'plants': plants,
    }
