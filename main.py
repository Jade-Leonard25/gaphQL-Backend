from fastapi import FastAPI
from db.db import Base, engine
from controllers import user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}