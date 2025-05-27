
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Tarea)
def crear_tarea(tarea: schemas.TareaCreate, db: Session = Depends(database.SessionLocal)):
    return crud.crear_tarea(db, tarea)

@router.get("/", response_model=list[schemas.Tarea])
def listar_tareas(db: Session = Depends(database.SessionLocal)):
    return crud.obtener_tareas(db)

@router.get("/usuario/{usuario_id}")
def tareas_por_usuario(usuario_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.obtener_tareas_por_usuario(db, usuario_id)

@router.get("/completadas")
def tareas_completadas(db: Session = Depends(database.SessionLocal)):
    return crud.obtener_tareas_completadas(db)

@router.get("/usuario-top")
def usuario_con_mas_tareas(db: Session = Depends(database.SessionLocal)):
    return crud.usuario_con_mas_tareas(db)
