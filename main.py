from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from bodyModel import FarmsEdit, Item, Farmers, FarmersEdit, UserLogin, Operations
from DatabaseFile import  create_farm1, create_farmer1, create_user, fetch_all_items, fetch_farmer1, fetch_single_item, update_farmer1, update_user, verify_password, get_user_by_email, fetch_all_farms, delete_farm, update_farm, create_operations, update_operations, delete_crop

app = FastAPI()


# Add CORS middleware
origins = [
    "https://elegant-fox-c1d48d.netlify.app/", 
    "https://first-project-jx9w.onrender.com/login",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
def read_root(para1):
    return {"Hello": para1}

# @app.post("/items/")
# async def create_item(item: Item):
#     create_user(item.name,item.description,item.price,item.tax)
#     return {"message": "Item created successfully"}


@app.post("/Farmers/")
async def create_farmer(item: Farmers):
    create_farmer1(item.name, item.email, item.phone, item.address, item.password)
    return {"message": "Farmer registered successfully"}

# @app.put("/items")
# async def update_item(item: Item):
#     update_user(item.id,item.name,item.description,item.price,item.tax)
#     return{"message":"Item Edited Successfully"}

@app.put("/Farmer")
async def update_farmer(item: FarmersEdit):
    update_farmer1(item.id, item.name, item.email, item.phone, item.address, item.password)
    return{"message":"Profile Edited Successfully"}

# @app.get("/items")
# async def fetch_item():
#     result = fetch_all_items()
#     return {"result" : result}

# @app.get("/item")
# async def fetch_one_item(userid):
#     result = fetch_single_item(userid)
#     return {"result" : result}

@app.get("/Farmer")
async def fetch_farmer(userid):
    result = fetch_farmer1(userid)
    return {"result" : result}

@app.post("/Create Farm")
async def create_farm(item : FarmsEdit):
    result = create_farm1(item.farmname, item.geometry,item.created_at,item.updated_at,item.description,item.isPaid,item.UserID)
    return {"message": "Farm Created Successfully"}



@app.post("/login")
async def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    
    # Verify the password
    if user.password != db_user['Password']:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    # If login is successful, you could return a token (JWT), but for now, let's just return a success message
    return {
        "message": "Login successful", 
        "username": db_user['Email'],

        }


@app.get("/Get Farms", response_model=List[dict])
async def get_farms(farm_id:int):
    farms = fetch_all_farms(farm_id)
    
    if not farms:
        raise HTTPException(status_code=404, detail="No farms found with this ID")
    
    return farms

@app.delete("/Delete Farm")
async def delete_farm_by_id(farm_id: int):
    success = delete_farm(farm_id) 

    if not success:
        raise HTTPException(status_code=404, detail="Farm not found or could not be deleted")

    return {"message": "Farm deleted successfully"}

@app.put("/farms")
async def update_farm_by_id(farm_id: int, farm: FarmsEdit):
    success = update_farm(farm_id, farm)

    if not success:
        raise HTTPException(status_code=404, detail="Farm not found or could not be updated")

    return {"message": "Farm updated successfully"}


@app.post("/Create Operations")
async def operations(item : Operations):
    result = create_operations(item.crop_name, item.supervisor_name, item.chemical_used, item.chemical_quantity, item.labour, item.area_in_acre, item.estimated_cost, item.add_comment)
    return {"message": "Operation Created Successfully"}


@app.put("/Update operations/")
async def update_crop_by_id(crop_id: int, crop: Operations):
    success = update_operations(crop_id, crop)

    if not success:
        raise HTTPException(status_code=404, detail="Crop not found or could not be updated")

    return {"message": "Crop updated successfully"}


@app.delete("/Delete Operation")
async def crop(crop_id: int):
    
    success = delete_crop(crop_id) 

    if not success:
        raise HTTPException(status_code=404, detail="Crop not found or could not be deleted")

    return {"message": "Crop deleted successfully"}


