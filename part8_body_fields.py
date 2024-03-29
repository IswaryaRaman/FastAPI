from fastapi import APIRouter,FastAPI,Body
from pydantic import BaseModel, Field

router6=APIRouter(prefix="",tags=["Body Fields"])

class Item(BaseModel):
    name:str 
    description:str | None =Field(None,title="The description of the item",max_length=20)
    price:float=Field(...,gt=0,description="The price must be greater than zero")
    tax:float |None=None

@router6.put("/Body_items/{item_id}")
def update_item(item_id:int,item:Item=Body(...,embed=True)):
    results={"item_id":item_id,"item":item}
    return results
