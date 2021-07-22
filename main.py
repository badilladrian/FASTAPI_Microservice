from typing import List, Optional

from fastapi import FastAPI, Query

from MVC.controllers import (
    ControllerBeds,
    ControllerPlants,
    ControllerYards,
)
from MVC.models import (
    BedRequestCreate,
    BedRequestUpdate,
    PlantRequestCreate,
    YardRequestCreate,
    YardRequestUpdate,
)

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
@app.get('/yards')
async def get_yards(id: Optional[List[int]] = Query(None)):
    message = 'Yards not found'
    yards = yards_controller.get_multi(id)
    if (len(yards) > 0):
        message = 'Listing yards'
    return ({
        'message': message,
        'yards': yards,
    })


# GET
@app.get('/yard')
async def get_yard(id: int):
    message = 'Yard not found'
    yard = yards_controller.get_one(id)
    if (yard):
        message = 'Yard found'
    return ({
        'message': message,
        'yard': yard,
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


# DELETE
@app.delete('/yard')
def delete_yard(id: int):
    message = 'Yard does not exist'
    if yards_controller.delete(id):
        message = 'Yard successfully deleted'
    return ({
        'message': message,
    })


# UPDATE
@app.put('/yards')
def update_yard(yards: List[YardRequestUpdate]):
    message = 'Yards not found'
    if yards_controller.update_multi(yards):
        message = 'Yard successfully updated'
    return ({
        'message': message,
    })


# Bed endpoints
# GET
@app.get('/beds')
async def get_beds(id: Optional[List[int]] = Query(None)):
    message = 'Beds not found'
    beds = beds_controller.get_multi(id)
    if (len(beds) > 0):
        message = 'Listing beds'
    return ({
        'message': message,
        'beds': beds,
    })


# GET
@app.get('/bed')
async def get_bed(id: int = Query(None)):
    message = 'Beds not found'
    bed = beds_controller.get_one(id)
    if (bed):
        message = 'Bed found'
    return ({
        'message': message,
        'bed': bed,
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


# DELETE
@app.delete('/bed')
def delete_bed(id: int):
    message = 'Bed does not exist'
    if beds_controller.delete(id):
        message = 'Bed successfully deleted'
    return ({
        'message': message,
    })


# UPDATE
@app.put('/beds')
def update_beds(beds: List[BedRequestUpdate]):
    message = 'Beds not found'
    if beds_controller.update_multi(beds):
        message = 'Beds successfully updated'
    return ({
        'message': message,
    })


# Plant endpoints
# GET
@app.get('/plants')
async def get_plants(ids: Optional[List[int]] = Query(None)):
    message = 'Plants not found'
    plants = plants_controller.get_multi(ids)
    if (plants or len(plants) > 0):
        message = 'Listing plants'
    return ({
        'message': message,
        'plants': plants,
    })


# GET
@app.get('/plant/{id}')
async def get_plant(id: int):
    message = 'Plant not found'
    plant = plants_controller.get_one(id)
    if (plant):
        message = 'Plant found'
    return ({
        'message': message,
        'plants': plant,
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


# DELETE
@app.delete('/plant')
def delete_plant(id: int):
    message = 'Plant does not exist'
    if plants_controller.delete(id):
        message = 'Plant successfully deleted'
    return ({
        'message': message,
    })
