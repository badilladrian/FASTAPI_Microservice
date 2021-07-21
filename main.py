from typing import List
from typing import Optional

from fastapi import FastAPI
from fastapi import Query

from MVC.controllers import ControllerBeds
from MVC.controllers import ControllerPlants
from MVC.controllers import ControllerYards
from MVC.models import BedRequestCreate
from MVC.models import PlantRequestCreate
from MVC.models import YardRequestCreate

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


# DELETE
@app.delete('/yard')
def delete_yard(id: int):
    message = 'Yard does not exist'
    if yards_controller.delete(id):
        message = 'Yard successfully deleted'
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


# Plant endpoints
# GET
@app.get('/plant')
def get_all_plants():
    plants = plants_controller.get_all()
    return {
        'message': 'Listing all plants',
        'plants': plants,
    }


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
