
from pydantic import BaseModel
from typing import List, Optional

class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    completada: Optional[bool] = False

class TareaCreate(TareaBase):
    usuario_id: int

class Tarea(TareaBase):
    id: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    tareas: List[Tarea] = []
    class Config:
        orm_mode = True
