
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(database.SessionLocal)):
    return crud.crear_usuario(db, usuario)

@router.get("/", response_model=list[schemas.Usuario])
def listar_usuarios(db: Session = Depends(database.SessionLocal)):
    return crud.obtener_usuarios(db)
