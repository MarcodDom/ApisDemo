import requests
import pytest
from fastapi.testclient import TestClient
from main import app

URL = "http://localhost:8000"
client = TestClient(app)

def test_contactos():
    response = client.get("v1/contactos", params = {"skip": 0})
    data = response.json()
    assert response.request.url == "http://testserver/v1/contactos?skip=0"
    
def test_contacto1():
    url = f"{URL}/v1/contactos"
    salt = 0
    lim = 10
    PARAMETRO = {
        "skip": salt,
        "limit":lim
    }
    response = requests.get(url, params = PARAMETRO)
    data = response.json()
    assert response.status_code == 200
    assert data == [
    {
        "id_contacto": 1,
        "nombre": "Juan Pérez",
        "telefono": "5512340001",
        "email": "juan.perez@gmail.com"
    },
    {
        "id_contacto": 2,
        "nombre": "María López",
        "telefono": "5512340002",
        "email": "maria.lopez@gmail.com"
    },
    {
        "id_contacto": 3,
        "nombre": "Carlos Sánchez",
        "telefono": "5512340003",
        "email": "carlos.sanchez@gmail.com"
    },
    {
        "id_contacto": 4,
        "nombre": "Ana Martínez",
        "telefono": "5512340004",
        "email": "ana.martinez@gmail.com"
    },
    {
        "id_contacto": 5,
        "nombre": "Luis Hernández",
        "telefono": "5512340005",
        "email": "luis.hernandez@gmail.com"
    },
    {
        "id_contacto": 6,
        "nombre": "Sofía Ramírez",
        "telefono": "5512340006",
        "email": "sofia.ramirez@gmail.com"
    },
    {
        "id_contacto": 7,
        "nombre": "Diego Torres",
        "telefono": "5512340007",
        "email": "diego.torres@gmail.com"
    },
    {
        "id_contacto": 8,
        "nombre": "Valeria Flores",
        "telefono": "5512340008",
        "email": "valeria.flores@gmail.com"
    },
    {
        "id_contacto": 9,
        "nombre": "Jorge Castillo",
        "telefono": "5512340009",
        "email": "jorge.castillo@gmail.com"
    },
    {
        "id_contacto": 10,
        "nombre": "Fernanda Gómez",
        "telefono": "5512340010",
        "email": "fernanda.gomez@gmail.com"
    }
    ]
    
def test_1():
    url = f"{URL}/v2/contactos/0/0"
    response = requests.get(url)
    data = response.json()
    assert data == []

    
    