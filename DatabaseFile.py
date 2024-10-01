import mysql.connector
from passlib.context import CryptContext
from bodyModel import FarmsEdit, Operations

# Configure password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def connect():
    return mysql.connector.connect(
        # srv1403.hstgr.io
        host= "srv1403.hstgr.io",
        user= "u381606128_MaheshGote",
        password= "Mahesh@2699",
        database= "u381606128_Cropgen"
    )


# Inside database.py
def create_user(name, description, price, tax):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, description, price, tax) VALUES (%s, %s,%s,%s)"
    values = (name, description, price, tax)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid


def create_farmer1(name, email, phone, address, password):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Farmers (name, email, phone, address, password) VALUES (%s, %s,%s,%s,%s)"
    values = (name, email, phone, address, password)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

# ... [other CRUD functions]



def update_user(id, name, description, price, tax):
    conn = connect()
    cursor = conn.cursor()
    query = '''UPDATE users
      SET price=%s
      WHERE userid = %s;'''
    values = (price,id)
    cursor.execute(query, values) 
    
    conn.commit()
    conn.close()
    return cursor.lastrowid


def update_farmer(id, name, email, phone, address, password):
    conn = connect()
    cursor = conn.cursor()
    query = '''UPDATE Farmers
      SET Name =%s,
      Email = %s,
      Phone = %s,
      Address = %s,
      Password = %s
      WHERE userid = %s;'''
    values = (name,email,phone,address,password,id)
    cursor.execute(query, values) 
    
    conn.commit()
    conn.close()
    return cursor.lastrowid

def fetch_all_items():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    arr = []
    for x in cursor.fetchall():
        arr.append({
            "name" : x[1],
            "description" : x[2]
        })


    conn.commit()
    conn.close()
    return arr
   


def fetch_single_item(userid):
    conn = connect()
    cursor = conn.cursor()
    query = f"SELECT name, description FROM users WHERE userid = {userid}"
    
    cursor.execute(query)
    arr = []
    for x in cursor.fetchall():
        arr.append({
            "name" : x[0],
            "description" : x[1]
        })
        # arr.append(str(x).replace("[","{").replace("]","}"))


    print(len(arr))
    
    conn.commit()
    conn.close()
    return arr[0]


def fetch_farmer1(userid):
    conn = connect()
    cursor = conn.cursor()
    query = f"SELECT Name, Email, Phone FROM Farmers WHERE userid = {userid}"
    
    cursor.execute(query)
    arr = []
    for x in cursor.fetchall():
        arr.append({
            "name" : x[0],
            "email" : x[1],
            "Phone" : x[2]
        })
        # arr.append(str(x).replace("[","{").replace("]","}"))


    print(len(arr))
    
    conn.commit()
    conn.close()
    return arr[0]
   
   
def create_farm1(farmname, geometry, created_at, updated_at, description, isPaid, UserID):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO farms (farmname, geometry, created_at, updated_at, description, isPaid, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (farmname, geometry, created_at, updated_at, description, isPaid, UserID)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid



def update_farmer1(id, farmname, isPaid, UserID):
    conn = connect()
    cursor = conn.cursor()
    query = '''UPDATE Farms
      SET farmname =%s,
      isPaid = %s
      WHERE FarmID = %s;'''
    values = (farmname,isPaid,id)
    cursor.execute(query, values) 
    
    conn.commit()
    conn.close()
    return cursor.lastrowid

def fetch_all_farms(FarmID):
    conn = connect()
    cursor = conn.cursor()
    query = f"SELECT * FROM farms WHERE FarmID = {FarmID}"
    cursor.execute(query)
    arr = []
    for x in cursor.fetchall():
        arr.append({
            "name" : x[1],
            "description" : x[2],
            "created_on": x[3]
        })
    
    conn.commit()
    conn.close()
    return arr

def delete_farm(farm_id: int) -> bool:
    conn = connect()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM farms WHERE FarmID = %s"
        cursor.execute(query, (farm_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def update_farm(farm_id: int, farm: FarmsEdit):
    conn = connect()
    cursor = conn.cursor()

     # Check if the farm exists
    check_query = "SELECT * FROM farms WHERE FarmID = %s"
    cursor.execute(check_query, (farm_id,))
    existing_farm = cursor.fetchone()

    if existing_farm is None:
        cursor.close()
        conn.close()
        return False 
    
    query = "UPDATE farms SET farmname = %s, geometry = %s, created_at = %s, updated_at = %s, description = %s, isPaid = %s, UserID = %s WHERE FarmID = %s"
    values = (farm.farmname, farm.geometry, farm.created_at, farm.updated_at, farm.description, farm.isPaid, farm.UserID, farm_id)
    
    cursor.execute(query, values)
    conn.commit()
    
    # Check if any rows were affected (i.e., farm was updated)
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return False

    cursor.close()
    conn.close()
    return True

def create_operations(crop_name, supervisor_name, chemical_used, chemical_quantity, labour, area_in_acre, estimated_cost, add_comment):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Operations (crop_name, supervisor_name, chemical_used, chemical_quantity, labour, area_in_acre, estimated_cost, add_comment) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)"
    values = (crop_name, supervisor_name, chemical_used, chemical_quantity, labour, area_in_acre, estimated_cost, add_comment)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def update_operations(crop_id: int, crop: Operations):
    conn = connect()
    cursor = conn.cursor()

     # Check if the farm exists
    check_query = "SELECT * FROM Operations WHERE CropID = %s"
    cursor.execute(check_query, (crop_id,))
    existing_crop = cursor.fetchone()

    if existing_crop is None:
        cursor.close()
        conn.close()
        return False 
    
    query = "UPDATE Operations SET crop_name = %s,  supervisor_name = %s, chemical_used = %s, chemical_quantity = %s, labour = %s, area_in_acre = %s, estimated_cost = %s, add_comment = %s WHERE CropID = %s"
    values = (crop.crop_name, crop.supervisor_name, crop.chemical_used, crop.chemical_quantity, crop.labour, crop.area_in_acre, crop.estimated_cost, crop.add_comment, crop_id)
    
    cursor.execute(query, values)
    conn.commit()
    
    # Check if any rows were affected (i.e., farm was updated)
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return False

    cursor.close()
    conn.close()
    return True

def delete_crop(crop_id: int) -> bool:
    conn = connect()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM Operations WHERE CropID = %s"
        cursor.execute(query, (crop_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(email: str):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM Farmers WHERE email = %s"
    cursor.execute(query, (email,))
    
    farmer = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return farmer