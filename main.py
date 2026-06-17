from fastapi import FastAPI
from database import Base, engine
from routers import clientes, factura, transacciones

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Facturación")

app.include_router(clientes.router)
app.include_router(factura.router)
app.include_router(transacciones.router)

