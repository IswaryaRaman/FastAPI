from fastapi import FastAPI 
import uvicorn 
import part3_query_param,part4_request_body,part5_queryparam_validation,part6_pathparam_validation,part7_body_multipleparam,part8_body_fields
app=FastAPI()
app.include_router(part3_query_param.router1)
app.include_router(part4_request_body.router2)
app.include_router(part5_queryparam_validation.router3)
app.include_router(part6_pathparam_validation.router4)
app.include_router(part7_body_multipleparam.router5)
app.include_router(part8_body_fields.router6)
from enum import Enum

# @app.get("/")
# def root():
#     return {"message":"hello world"}

# @app.put("/")
# def put():
#     return {"message":"hello from put"}

# @app.post("/")
# def post():
#     return {"message":"hello from post"}

@app.get("/users")
def list_users():
    return {"message":"list users route"}

@app.get("/users/me")
def get_current_user():
    return {"message":"this is the current user"}

@app.get("/users/{user_id}")
def get_user(user_id:str):
    return {"user_id":user_id}

class FoodEnum(str,Enum):
    fruits="fruits"
    vegetables="vegetables"
    dairy="dairy"

@app.get("/foods/{food_name}")
def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetables:
        return {"food_name":food_name,"message":"you are healthy"}
    if food_name.value=="fruits":
        return {
            "food_name":food_name,
            "message":"still healthy but like sweet things"
        }
    return {"food_name":food_name,"message":"i like hot melted chocolate:)"}







