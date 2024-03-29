from fastapi import APIRouter,Path,FastAPI,Query

router4=APIRouter(prefix="",tags=["Path parameter Validation"])

@router4.get("/items_validation/{item_id}")
def read_items_validation(*,item_id: int =Path(...,title="ID of the item to get",gt=10,le=100),q:str="hello",size:float=Query(...,gt=0,lt=7.75)):
    results={"item_id":item_id,"size":size}
    if q:
        results.update({"q":q})
    return results 