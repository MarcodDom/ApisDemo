from fastapi import FastAPI,HTTPException
import sqlite3

app = FastAPI()

@app.get(
    "/",
    status_code= 202,
    summary= "Endpoint raiz", 
    description= "Bienvenido a la agenda")
def read_root():
    return {
        "message": "Api de la agenda",
        "datatime": "12/02/2026"
        }


@app.get(
    "/v1/contactos",
    status_code = 202,
    summary = """
    description = endpoint que regresa los contactos paginados,
    utiliza los sig query params:
    limit:int -> Indica el numero de resgistros a regresar
    skip: int: -> Indica el numero de registros a omitir"""
)
async def get_contactos(skip: int = 0, limit: int = 10):
    connection = sqlite3.connect("agenda.db")
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute("select * from contactos")
    rows = c.fetchall()
    response = [dict(r) for r in rows]
    ordenados = response[skip: skip + limit]    
    return ordenados


@app.get(
    "/v1/contactos/{id}",
    status_code = 202,
    summary = """
    description = Endpoint dinamico para buscar mediante el ID"""
)
async def get_buscar_contactos(id:int):
    connection = sqlite3.connect("agenda.db")
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute(f"select * from contactos where id_contacto = {id}")
    rows = c.fetchone()
    if not rows:
        raise HTTPException(
            status_code = 404,
            detail = "No se encontrop el archivo"
        )
    return dict(rows)