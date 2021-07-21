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


# Bed endpoints
# GET
@app.get('/bed')
def get_all_beds():
    beds = beds_controller.get_all()
    return ({
        'message': 'Listing all beds',
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
