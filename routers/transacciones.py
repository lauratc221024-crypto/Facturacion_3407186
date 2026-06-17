from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Transaccion
from schemas import TransaccionCreate

router = APIRouter(tags=["Transacciones"])

@router.get("/factura/{id}/transacciones")
def listar(id:int, db: Session = Depends(get_db)):
    return db.query(Transaccion).filter(Transaccion.factura_id==id).all()

@router.post("/factura/{id}/transacciones")
def crear(id:int, data: TransaccionCreate, db: Session = Depends(get_db)):
    t = Transaccion(**data.dict(), factura_id=id)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

@router.get("/factura/{id}/transacciones/{transacciones_id}")
def obtener(id:int, transacciones_id:int, db: Session = Depends(get_db)):
    return db.query(Transaccion).filter(Transaccion.id==transacciones_id, Transaccion.factura_id==id).first()

@router.put("/factura/{id}/transacciones/{transacciones_id}")
def editar(id:int, transacciones_id:int, data: TransaccionCreate, db: Session = Depends(get_db)):
    t = db.query(Transaccion).filter(Transaccion.id==transacciones_id).first()
    if not t:
        raise HTTPException(404,"No encontrada")
    for k,v in data.dict().items():
        setattr(t,k,v)
    db.commit()
    return t

@router.delete("/factura/{id}/transacciones/{transacciones_id}")
def eliminar(id:int, transacciones_id:int, db: Session = Depends(get_db)):
    t = db.query(Transaccion).filter(Transaccion.id==transacciones_id).first()
    if not t:
        raise HTTPException(404,"No encontrada")
    db.delete(t)
    db.commit()
    return {"mensaje":"Transacción eliminada"}
