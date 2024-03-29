from fastapi import Query, FastAPI, APIRouter 

router3=APIRouter(prefix="",tags=["Query Param Validation"])

@router3.get("/query_items")
def read_items(q:str |None = Query(None,min_length=3,max_length=10,title="Sample query string",description="This is a sample query string",alias="item-query")):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

@router3.get("/items_hidden")
def hidden_query_route(hidden_query: str | None =Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query":hidden_query}
    return {"hidden_query":"Not found"}

