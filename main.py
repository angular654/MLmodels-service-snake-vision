from typing import Optional

from fastapi import FastAPI

from Controller import Controller
from Controller import RequestData
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
ctrl = Controller()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return ctrl.service_info()


@app.post("/upload-script")
def upload(data: RequestData):
    return ctrl.upload_info(data)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
