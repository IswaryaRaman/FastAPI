from fastapi import FastAPI,APIRouter,Body
from pydantic import BaseModel,HttpUrl, Field

router7=APIRouter(prefix="",tags=["Nested Models"])

class Image(BaseModel):
    url: HttpUrl
    name: str 

class Item(BaseModel):
    name: str 
    description: str|None =None 
    price: float 
    tags: set[str] =[]
    image: list[Image] | None =None 

class Offer(BaseModel):
    name: str 
    description: str |None =None 
    price: float 
    items: list[Item]

@router7.put("/nested_items/{item_id}")
def update_item(item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results 

@router7.post("/offers")
def create_offer(offer:Offer=Body(...,embed=True)):
    return offer 

@router7.post("/images/multiple")
def create_multiple_images(images:list[Image]):
    return images 

@router7.post("/blah")
def create_some_blah(blahs:dict[int,float]):
    return blahs

