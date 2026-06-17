from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Factura
from schemas import FacturaCreate

router = APIRouter(tags=["Factura"])

@router.get("/factura")
def listar(db: Session = Depends(get_db)):
    return db.query(Factura).all()

@router.post("/factura")
def crear(data: FacturaCreate, db: Session = Depends(get_db)):
    f = Factura(**data.dict())
    db.add(f)
    db.commit()
    db.refresh(f)
    return f

@router.get("/factura/{id}")
def obtener(id:int, db: Session = Depends(get_db)):
    return db.query(Factura).filter(Factura.id==id).first()

@router.put("/factura/{id}")
def editar(id:int, data: FacturaCreate, db: Session = Depends(get_db)):
    f = db.query(Factura).filter(Factura.id==id).first()
    if not f:
        raise HTTPException(404,"Factura no encontrada")
    for k,v in data.dict().items():
        setattr(f,k,v)
    db.commit()
    return f

@router.delete("/factura/{id}")
def eliminar(id:int, db: Session = Depends(get_db)):
    f = db.query(Factura).filter(Factura.id==id).first()
    if not f:
        raise HTTPException(404,"Factura no encontrada")
    db.delete(f)
    db.commit()
    return {"mensaje":"Factura eliminada"}
