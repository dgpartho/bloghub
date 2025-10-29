from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def read_root():
    return {"status":"healthy"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
