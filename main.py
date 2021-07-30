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
    PlantRequestUpdate,
    YardRequestCreate,
    YardRequestUpdate,
)

yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()


tags_metadata = [
    {
        'name': 'Farmly',
        'description': 'All general operations',
    },
    {
        'name': 'Yards',
        'description': "Manage your yards, all yard's operations are here",
    },
    {
        'name': 'Beds',
        'description': "Manage your beds, all bed's operations are here",
    },
    {
        'name': 'Plants',
        'description': "Manage your plants, all plant's operations are here",
    },
]

app = FastAPI(
    title='Farmly',
    description='The best assistant for farmers',
    version='0.0.1',
    openapi_tags=tags_metadata,
)


@app.get('/', tags=['Farmly'])
async def welcome():
    response = {
        'message': 'Welcome to the best farmer assistant app ever!',

    }
    return response


# Yard endpoints


# POST
# Create a new Yard
@app.post('/yard', tags=['Yards'])
def create_yard(request: list[YardRequestCreate]):
    response = {
        'message': 'Yards couldn´t be created',
    }
    yards = yards_controller.create(request=request)
    if yards:
        response['message'] = 'Yards created successfully'
        response['yards'] = yards
    return response


# GET
# Get a all and multi yards
@app.get('/yards', tags=['Yards'])
async def get_yards(id: Optional[List[int]] = Query(None)):
    response = {
        'message': 'Yards not found',
    }
    yards = yards_controller.get_multi(id)
    if yards:
        response['message'] = 'Listing yards'
        response['yards'] = yards_controller.get_multi(id)
    return response


# Get a single yard
@app.get('/yard', tags=['Yards'])
async def get_yard(id: int):
    response = {
        'message': 'Yard not found',
    }
    yard = yards_controller.get_one(id)
    if yard:
        response['message'] = 'Yard found'
        response['yard'] = yard
    return response


# DELETE
# Remove a single yard
@app.delete('/yard', tags=['Yards'])
def delete_yard(id: int):
    response = {
        'message': 'Yard does not exist',
    }
    if yards_controller.delete(id):
        response['message'] = 'Yard successfully deleted'
    return response

# PUT
# Update a single yard


@app.put('/yard', tags=['Yards'])
def update_yard(id: int, request: YardRequestUpdate):
    response = {
        'message': 'Yard not found',
    }
    if yards_controller.update(id, request):
        response['message'] = 'Yard successfully updated'
    return response


# Bed endpoints


# GET
# Get all and multi beds
@app.get('/beds', tags=['Beds'])
async def get_beds(id: Optional[List[int]] = Query(None)):
    response = {
        'message': 'Beds not found',
    }
    beds = beds_controller.get_multi(id)
    if (beds):
        response['message'] = 'Listing beds'
        response['beds'] = beds
    return response


# Get a single bed
@app.get('/bed', tags=['Beds'])
async def get_bed(id: int = Query(None)):
    response = {
        'message': 'Beds not found',
    }
    bed = beds_controller.get_one(id)
    if bed:
        response['message'] = 'Bed found'
        response['bed'] = bed
    return response


# POST
# Create  a bed
@app.post('/bed', tags=['Beds'])
def create_bed(request: list[BedRequestCreate]):
    response = {
        'message': 'Beds couldn´t be created',
    }
    if beds_controller.create(request=request):
        response['message'] = 'Beds created successfully'
    return response


# DELETE
# Remove a bed
@app.delete('/bed', tags=['Beds'])
def delete_bed(id: int):
    response = {
        'message': 'Bed does not exist',
    }
    if beds_controller.delete(id):
        response['message'] = 'Bed successfully deleted'
    return response


# PUT
# Update a bed
@app.put('/bed', tags=['Beds'])
def update_bed(id: int, request: BedRequestUpdate):
    response = {
        'message': 'Bed not found',
    }
    if beds_controller.update(id, request):
        response['message'] = 'Bed successfully updated'
    return response


# Plant endpoints


# GET
# Get all and multi plants
@app.get('/plants', tags=['Plants'])
async def get_plants(id: Optional[List[int]] = Query(None)):
    response = {
        'message': 'Plants not found',
    }
    plants = plants_controller.get_multi(id)
    if plants:
        response['message'] = 'Listing plants'
        response['plants'] = plants
    return response


# Get a single plant
@app.get('/plant', tags=['Plants'])
async def get_plant(id: int):
    response = {
        'message': 'Plant not found',
    }
    plant = plants_controller.get_one(id)
    if plant:
        response['message'] = 'Plant found'
        response['plant'] = plant
    return response


# POST
# Create a plant
@app.post('/plant', tags=['Plants'])
def create_plant(request: list[PlantRequestCreate]):
    response = {
        'message': 'Plants couldn´t be created',
    }
    if plants_controller.create(request=request):
        response['message'] = 'Plants created successfully'
    return response


# DELETE
# Remove a plant
@app.delete('/plant', tags=['Plants'])
def delete_plant(id: int):
    response = {
        'message': 'Plant does not exist',
    }
    if plants_controller.delete(id):
        response['message'] = 'Plant successfully deleted'
    return response


# Put
# Update a plant
@app.put('/plant', tags=['Plants'])
def update_plant(id: int, request: PlantRequestUpdate):
    response = {
        'message': 'Plant not found',
    }
    if plants_controller.update(id, request):
        response['message'] = 'Plant successfully updated'
    return response
