from fastapi import APIRouter 
from pydantic import BaseModel

router2=APIRouter(prefix="",tags=["POST request body"])

class Item(BaseModel):
    name:str
    description: str | None=None 
    price:float 
    tax:float | None=None 


@router2.post("/items")
def create_item(item:Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+item.tax 
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict 

@router2.put("/items/{item_id}")
def create_item_with_put(item_id:int,item:Item,q:str | None=None):
    result={"item_id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result

