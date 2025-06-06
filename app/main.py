
from fastapi import FastAPI
from .routers import users, tasks
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(tasks.router, prefix="/tareas", tags=["Tareas"])
