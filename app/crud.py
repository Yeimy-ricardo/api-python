
from sqlalchemy.orm import Session
from . import models, schemas

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()

def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    db_tarea = models.Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def obtener_tareas(db: Session):
    return db.query(models.Tarea).all()

def obtener_tareas_por_usuario(db: Session, usuario_id: int):
    return db.query(models.Tarea).filter(models.Tarea.usuario_id == usuario_id).all()

def obtener_tareas_completadas(db: Session):
    return db.query(models.Tarea).filter(models.Tarea.completada == True).all()

def usuario_con_mas_tareas(db: Session):
    from sqlalchemy import func
    return db.query(models.Usuario).join(models.Tarea).group_by(models.Usuario.id).order_by(
        func.count(models.Tarea.id).desc()).first()
