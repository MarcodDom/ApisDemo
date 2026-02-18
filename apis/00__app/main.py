from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Word"}

@app.get("/clientes/{client}")
def get_clientes(client:str):
    data = [
        {"nombre":"marco"},
        {"nombre":"jhon"}
    ]
    
    for a in data:
        if a["nombre"] == client:
            return a
    raise HTTPException(
        status_code = 404,
        detail = "No se encontro"
    )
