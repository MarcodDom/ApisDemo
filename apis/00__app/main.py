from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Word"}

@app.get("/clientes")
def get_clientes():
    data = [
        {
            "nombre":"marco"
        },
        {
            "nombre":"jhon"
        }
    ]
    return data