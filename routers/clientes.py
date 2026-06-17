from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Cliente
from schemas import ClienteCreate

router = APIRouter(tags=["Clientes"])

@router.get("/clientes")
def listar(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@router.post("/clientes")
def crear(cliente: ClienteCreate, db: Session = Depends(get_db)):
    nuevo = Cliente(**cliente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/clientes/{id}")
def obtener(id:int, db: Session = Depends(get_db)):
    c = db.query(Cliente).filter(Cliente.id == id).first()
    if not c:
        raise HTTPException(404,"Cliente no encontrado")
    return c

@router.patch("/clientes/{id}")
def editar(id:int, datos: ClienteCreate, db: Session = Depends(get_db)):
    c = db.query(Cliente).filter(Cliente.id == id).first()
    if not c:
        raise HTTPException(404,"Cliente no encontrado")
    for k,v in datos.dict().items():
        setattr(c,k,v)
    db.commit()
    return c

@router.delete("/clientes/{id}")
def eliminar(id:int, db: Session = Depends(get_db)):
    c = db.query(Cliente).filter(Cliente.id == id).first()
    if not c:
        raise HTTPException(404,"Cliente no encontrado")
    db.delete(c)
    db.commit()
    return {"mensaje":"Cliente eliminado"}
