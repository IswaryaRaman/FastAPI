from fastapi import FastAPI 
from fastapi import APIRouter 

router1=APIRouter(prefix="",tags=["Query parameter"])

fake_items_db=[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@router1.get("/items")
def list_items(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

@router1.get("/items/{item_id}")
def get_item(item_id:str, sample_query_param:str,q:str | None=None,short :bool=False):
    item={"item_id":item_id,"sample_query_param":sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description":"Updating desc here"}
        )
    return item 

@router1.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id:int,item_id:str,q:str | None=None,short:bool=False):
    item={"item_id":item_id,"owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description":"practising fastapi:)"}
        )
    return item








