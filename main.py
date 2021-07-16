from fastapi import FastAPI

from MVC.controllers import ControllerBeds
from MVC.controllers import ControllerBotanicalCategories
from MVC.controllers import ControllerEntryGroups
from MVC.controllers import ControllerEntryTypes
from MVC.controllers import ControllerPlantFamilies
from MVC.controllers import ControllerPlants
from MVC.controllers import ControllerYards
from MVC.models import BedRequestCreate
from MVC.models import PlantFamilyRequestCreate
from MVC.models import YardRequestCreate


yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()
entry_group_controller = ControllerEntryGroups()
entry_types_controller = ControllerEntryTypes()
plant_families_controller = ControllerPlantFamilies()
botanical_categories_controller = ControllerBotanicalCategories()
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
        message = 'Yards created successfuly'
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
        message = 'Beds created successfuly'
    return ({
        'message': message,
    })


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


@app.get('/entry_type')
def get_all_entry_types():
    entry_types = entry_types_controller.get_all()
    return ({
        'message': 'Listing all entry types',
        'entry_types': entry_types,
    })


@app.get('/plant_family')
def get_all_plant_families():
    plant_families = plant_families_controller.get_all()
    return ({
        'message': 'Listing all plant families',
        'entry_types': plant_families,
    })


@app.post('/plant_family')
def create_plant_family(plant_family_request: list[PlantFamilyRequestCreate]):
    message = 'Plant families couldn´t be created'
    if plant_families_controller.create(plant_family_request):
        message = 'Plant families created successfuly'
    return ({
        'message': message,
    })
