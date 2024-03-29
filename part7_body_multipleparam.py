from fastapi import APIRouter,FastAPI,Path,Body
from pydantic import BaseModel

router5=APIRouter(prefix="",tags=["Body Multiple Parameters"])

class Item(BaseModel):
    name:str 
    description:str |None=None 
    price:float
    tax:float |None=None

class User(BaseModel):
    username:str 
    full_name:str | None =None 

@router5.put("/put_items/{item_id}")
def update_item(*,item_id:int=Path(...,title="The ID of the item to get",ge=0,le=150),q:str |None =None,item:Item=Body(...,embed=True)):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item":item})
    return results  
