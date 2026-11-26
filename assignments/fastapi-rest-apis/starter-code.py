from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Study FastAPI", "completed": False},
]


@app.get("/")
def read_root():
    # TODO: Return a welcome message.
    return {}


@app.get("/tasks")
def read_tasks():
    # TODO: Return the list of tasks.
    return []


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # TODO: Find and return the matching task or raise an HTTPException.
    return {}


@app.post("/tasks")
def create_task(task: TaskInput):
    # TODO: Create a task with a new ID and add it to the list.
    return {}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskInput):
    # TODO: Replace the matching task or raise an HTTPException.
    return {}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Remove and return the matching task or raise an HTTPException.
    return {}
