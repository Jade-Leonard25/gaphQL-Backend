from fastapi import *
from db.db import Base, engine
from controllers import user, chat, content
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(chat.router)
app.include_router(content.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}