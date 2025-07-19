from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel



router = APIRouter()


tasks = []

class Task(BaseModel):
    id : int
    title : str
    description : str

# get all
@router.get("/tasks")
def get_tasks():
    if not tasks:
        raise HTTPException(status_code = 404, detail=' Your tasks were not found ')
    return tasks

#get by id
@router.get("/tasks/{task_id}")
def get_tasks_by_id(task_id:int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code = 404, detail=' the task you entered is not found ')

# create
@router.post("/tasks")
def create_task(task:Task):
    tasks.append(task)
    return task


# delete
@router.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for index, task in enumerate (tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"Message" : "Task Deleted Successfully"}
        
    raise HTTPException(status_code = 404, detail=' the task you entered is not found ')



#Put
@router.put("/tasks/{task_id}")
def update_task(task_id:int,new_task:Task):
    for index, task in enumerate (tasks):
        if task.id == task_id:
            tasks[index]=new_task

            return {'Message' : 'New Task is Upadted'}
        
    raise HTTPException(status_code = 404, detail=' the task you entered is not found ')