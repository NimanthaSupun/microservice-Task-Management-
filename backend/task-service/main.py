import os
from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import redis
import json


app = FastAPI(title="Task service")

# todo: connectd to mongoDB
MONGO_URL = os.getenv("MONGO_URL","mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.task_db

# todo: connect to redis
REDIS_URL = os.getenv("REDIS_URL","redis://localhost:6379")
r = redis.from_url(REDIS_URL)


# todo: 2 define the task model
class Task(BaseModel):
    title:str
    description:str
    status:str = "pending"

@app.get("/")
async def root():
    return {"message":"Task service is connected to MongoDB"}

# 3. create a Task (saves to DB AND sends to redis)
@app.post("/tasks")
async def create_task(task:Task):
    # 1. save mongoDB
    task_dict = task.model_dump()
    new_task = await db.tasks.insert_one(task_dict)

    # 2. push to redis for the notification service
    notification_data = {"title":task.title,"id":str(new_task.inserted_id)}
    r.lpush("task_notifications",json.dumps(notification_data))

    return {"id":str(new_task.inserted_id),"msg":"Task created & Notification Queud!"}
    print(f"Task created & Notification Queud!")

# todo: 4 Get all Tasks
@app.get("/tasks")
async def get_tasks():
    tasks = []
    async for task in db.tasks.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks
