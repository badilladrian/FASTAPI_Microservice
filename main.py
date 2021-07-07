from fastapi import FastAPI;
from MVC.controllers import ControllerYards, ControllerBeds, ControllerPlants

yards_controller = ControllerYards()
beds_controller = ControllerBeds()
plants_controller = ControllerPlants()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is the best farmer assistence app ever!"}

@app.get('/yards')
def get_all():
    return yards_controller.get_all()


@app.get('/beds')
def get_all():
    return beds_controller.get_all()


@app.get('/plants')
def get_all():
    return plants_controller.get_all()



# @app.post('/user/')
# def post_add_user(user:User):
#     return controller.add_user(user) 

# @app.delete('/user/')
# def delete_user(username_request:UserRequestDelete):
#     return controller.delete_user(username_request)

# @app.post('/login/')
# def login(credentials_request:UserRequestLogin):
#     return controller.login(credentials_request)

if __name__ == '__main__':
    main()