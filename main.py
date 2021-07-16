from fastapi import FastAPI

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
