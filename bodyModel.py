from pydantic import BaseModel

class Item(BaseModel):
    id:int = None
    name: str
    description: str = None
    price: int
    tax: int = None


class UserLogin(BaseModel):
    email: str
    password: str



class Farmers(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    password: str

class FarmersEdit(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    password: str




class FarmsEdit(BaseModel):
    farmname : str
    geometry: str
    created_at:str
    updated_at:str
    description:str
    isPaid:int
    UserID:int


class Operations(BaseModel):
    crop_name : str
    supervisor_name: str
    chemical_used:str
    chemical_quantity:str
    labour:str
    area_in_acre:str
    estimated_cost:str
    add_comment:str



class UserLogin(BaseModel):
    email: str
    password: str