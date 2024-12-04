from fastapi import FastAPI
from routers import task, user
from app.models.task import Task
from app.models.user import User

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}
app.include_router(task.router)
app.include_router(user.router)