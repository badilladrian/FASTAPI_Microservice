from typing import List, Optional

from fastapi import FastAPI, Query

from MVC.controllers import ControllerBeds, ControllerPlants, ControllerYards
from MVC.models import BedRequestCreate, PlantRequestCreate, YardRequestCreate

yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()
app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'This is the best farmer assistence app ever!',
    }

# Yard endpoints
# GET


@app.get('/yard')
def get_all_yards():
    yards = yards_controller.get_all()
    return ({
        'message': 'Listing all yards',
        'yards': yards,
    })


# POST
@app.post('/yard')
def create_yard(request: list[YardRequestCreate]):
    message = 'Yards couldn´t be created'
    if yards_controller.create(request=request):
        message = 'Yards created successfully'
    return ({
        'message': message,
    })


# Bed endpoints
# GET
@app.get('/bed')
async def get_beds(bed: Optional[List[int]] = Query(None)):
    message = 'Beds not found'
    beds = beds_controller.get(bed)
    if (beds or len(beds) > 0):
        message = 'Listing beds'
    return ({
        'message': message,
        'beds': beds,
    })


# POST
@app.post('/bed')
def create_bed(request: list[BedRequestCreate]):
    message = 'Beds couldn´t be created'
    if beds_controller.create(request=request):
        message = 'Beds created successfully'
    return ({
        'message': message,
    })


# Plant endpoints
# GET
@app.get('/plant')
async def get_plants(id: Optional[List[int]] = Query(None)):
    message = 'Plants not found'
    plants = plants_controller.get(id)
    if (plants or len(plants) > 0):
        message = 'Listing plants'
    return ({
        'message': message,
        'plants': plants,
    })


# POST
@app.post('/plant')
def create_plant(request: list[PlantRequestCreate]):
    message = 'Plants couldn´t be created'
    if plants_controller.create(request=request):
        message = 'Plants created successfully'
    return ({
        'message': message,
    })
