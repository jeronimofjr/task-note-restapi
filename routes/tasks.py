from fastapi import APIRouter, Body, File, UploadFile, status, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.task import Task
from database.database import db
from datetime import datetime
from sqlalchemy import func
from schemas.task import TaskCreate
import pandas
from collections import defaultdict
import os

router = APIRouter()

@router.get("/tasks")
async def get_tasks():
    try:
        tasks = db.query(Task).all()
        if tasks:
            return JSONResponse(content=jsonable_encoder(tasks), 
                                status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message" :"Não há tasks cadastradas"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao recuperar tasks"},
                            status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/tasks/save")
async def save_tasks(file_path: str = Query(...)):
    try:
        tasks = db.query(Task).filter(Task.completed_at == False).all()
        if tasks:
            incomplete_tasks = defaultdict(list)
            for task in tasks:
                incomplete_tasks["title"].append(task.title)
                incomplete_tasks["description"].append(task.description)
                incomplete_tasks["created_at"].append(task.created_at)
            incomplete_tasks = pandas.DataFrame(incomplete_tasks)
            
            incomplete_tasks.to_csv(file_path)
            if os.path.exists(file_path):
                return JSONResponse(content={"message" : "Arquivo salvo com sucesso"},
                                    status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message" :"Não há tasks incompletas cadastradas"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao salvar arquivo"},
                                status_code=status.HTTP_404_NOT_FOUND)


@router.get("/tasks/{id}")
async def get_task(id: int = Path(..., ge=1)):
    try:
        task = db.query(Task).filter(Task.id == id).scalar()
        if task:
            return JSONResponse(content={"message" : jsonable_encoder(task)}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message" : "Task inexistente"}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao recuperar task"},
                            status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/tasks")
async def delete_all_tasks():
    try:
        response = db.query(Task).delete()
        db.commit()
        return JSONResponse(content={"message" : f"{response} tasks deletadas"}, status_code=status.HTTP_200_OK)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={"message" : "Erro ao deletar tasks"},
                            status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/tasks/complete")
async def delete_all_tasks_completed():
    try:
        response = db.query(Task).filter(Task.completed_at == True).delete()
        db.commit()
        if response:
            return JSONResponse(content={"message" : "Tasks deletadas com sucesso"},
                            status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message" : "Não há tasks para serem deletadas"},
                      status_code=status.HTTP_200_OK)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={"message" : "Erro ao deletar tasks"},
                            status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/tasks/{id}")
async def delete_task(id: int = Path(..., ge=1)):
    try:
        task = db.query(Task).filter(Task.id == id).scalar()
        if task:
            db.delete(task)
            db.commit()
            return JSONResponse(content={"message" : f"Task - {task.title} - removida com sucesso"}, status_code=status.HTTP_200_OK)
        
        return JSONResponse(content={"message" : f"Task com inexistente"}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={"message" : "Erro ao deletar task"}, status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/tasks/date/{date}")
async def get_tasks_by_date(date: str):
    try:
        tasks = db.query(Task).filter(Task.created_at == date).all()
        if tasks:
            return JSONResponse(content={"message" : jsonable_encoder(tasks)}, status_code=status.HTTP_200_OK)
        
        return JSONResponse(content={"message" :f"Não há tasks cadastradas para a data {date}"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao buscar tasks"}, status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/tasks/qtd/")
async def get_qtd_tasks():
    try:
        qtd_tasks = db.query(func.count(Task.id)).scalar()
        compl_tasks = db.query(func.count(Task.id)).filter(Task.completed_at == True).scalar()
        uncompl_tasks = qtd_tasks - compl_tasks

        data = {"Tasks Criadas" : qtd_tasks,
                "Tasks completas" : compl_tasks, 
                "Tasks Incompletas" : uncompl_tasks}
        
        return JSONResponse(content=data,
                                 status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content={
            "Erro" : "Não foi possível obter os dados solicitados"
        },
        status_code=status.HTTP_400_BAD_REQUEST)


@router.patch("/tasks/{id}/complete")
def mark_task(id: int = Path(..., ge=1)):
    try:
        task = db.query(Task).filter(Task.id == id).scalar()

        if task:
            task.completed_at = not task.completed_at
            db.commit()
            return JSONResponse(content={"message" : f"Task {task.title} completada com sucesso"}, status_code=status.HTTP_200_OK)
        
        return JSONResponse(content={"message" : f"Task inexistente"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao atualizar task"},
                            status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/tasks/upload")
async def create_many_tasks(file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode()
    content = content.split("\n")

    tasks = []
    for row in content[1:]:
        title, desc = row.split(',')
        
        task = Task(description = desc,
                    title = title,
                    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                    updated_at = None,
                    completed_at = False)
        tasks.append(task)
    try:
        db.add_all(tasks)
        db.commit()
        return JSONResponse(content={"message" : f"{len(tasks)} Tasks criadas com sucesso"}, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content={"message" : "Erro ao criar tasks a partir de arquivo csv"},
                            status_code=status.HTTP_400_BAD_REQUEST)
    
    
@router.post("/tasks")
async def create_task(task: TaskCreate):
    try:
        task = Task(**task.model_dump())
        db.add(task) 
        db.commit()
        return JSONResponse(content={"message" : f"Task - {task.title} - criada com sucesso"}, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={
            "message" : "Erro ao inserir task"},
            status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/tasks/{id}")
async def update_task(id: int = Path(..., ge=1), title: str = Body(None), description: str = Body(None)):
    print(title)
    print(description)
    try:
        task = db.query(Task).filter(Task.id == id).scalar()
        
        print(task)
        if task:
            task.title = title if title else task.title
            task.description = description if description else task.description
            task.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            db.commit()
            return JSONResponse(content={"message" : f"Task - {task.title} - atualizada com sucesso"}, status_code=status.HTTP_200_OK)

        return JSONResponse(content={"message" : f"Task inexistente"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={
            "message" : "Erro ao atualizar task"},
            status_code=status.HTTP_400_BAD_REQUEST)

