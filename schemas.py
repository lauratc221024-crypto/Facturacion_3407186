from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre:str
    correo:str
    telefono:str

class FacturaCreate(BaseModel):
    numero:str
    fecha:str
    total:float
    cliente_id:int

class TransaccionCreate(BaseModel):
    tipo:str
    valor:float
    fecha:str
