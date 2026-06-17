# Sistema de Facturación FastAPI

## 1. Crear entorno virtual
python -m venv venv

## 2. Activar entorno
Windows:
venv\Scripts\activate

## 3. Instalar dependencias
pip install -r requirements.txt

## 4. Ejecutar
uvicorn main:app --reload

## 5. Abrir Swagger
http://127.0.0.1:8000/docs

## Rutas
Clientes:
GET /clientes
POST /clientes
GET /clientes/{id}
PATCH /clientes/{id}
DELETE /clientes/{id}

Facturas:
GET /factura
POST /factura
GET /factura/{id}
PUT /factura/{id}
DELETE /factura/{id}

Transacciones:
GET /factura/{id}/transacciones
POST /factura/{id}/transacciones
GET /factura/{id}/transacciones/{transacciones_id}
PUT /factura/{id}/transacciones/{transacciones_id}
DELETE /factura/{id}/transacciones/{transacciones_id}
