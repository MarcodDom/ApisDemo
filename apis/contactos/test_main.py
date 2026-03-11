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
     
def test_1():
    response = requests.get(f"{URL}/v2/contactos/0/10")
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

def test_2():
  response = requests.get(f"{URL}/v2/contactos/0/-10")
  data = response.json()
  assert response.status_code == 422
  assert data == {"ERROR":"El limite no debe de ser inferior a 0"}
    
def test_3():
  response = requests.get(f"{URL}/v2/contactos/-10/0")
  data = response.json()
  assert response.status_code == 422
  assert data == {"ERROR":"El salto no debe de ser inferior a 0"}

def test_4():
  response = requests.get(f"{URL}/v2/contactos/90/10")
  data = response.json()
  assert response.status_code == 200
  assert data == [
  {
    "id_contacto": 91,
    "nombre": "Noelia Bustos",
    "telefono": "5512340091",
    "email": "noelia.bustos@gmail.com"
  },
  {
    "id_contacto": 92,
    "nombre": "Héctor Villaseñor",
    "telefono": "5512340092",
    "email": "hector.villasenor@gmail.com"
  },
  {
    "id_contacto": 93,
    "nombre": "Lourdes Aparicio",
    "telefono": "5512340093",
    "email": "lourdes.aparicio@gmail.com"
  },
  {
    "id_contacto": 94,
    "nombre": "Axel Valenzuela",
    "telefono": "5512340094",
    "email": "axel.valenzuela@gmail.com"
  },
  {
    "id_contacto": 95,
    "nombre": "Cinthia Padilla",
    "telefono": "5512340095",
    "email": "cinthia.padilla@gmail.com"
  },
  {
    "id_contacto": 96,
    "nombre": "Rafael Paredes",
    "telefono": "5512340096",
    "email": "rafael.paredes@gmail.com"
  },
  {
    "id_contacto": 97,
    "nombre": "Maritza Belmonte",
    "telefono": "5512340097",
    "email": "maritza.belmonte@gmail.com"
  },
  {
    "id_contacto": 98,
    "nombre": "Óliver Serrano",
    "telefono": "5512340098",
    "email": "oliver.serrano@gmail.com"
  },
  {
    "id_contacto": 99,
    "nombre": "Beatriz Coronado",
    "telefono": "5512340099",
    "email": "beatriz.coronado@gmail.com"
  },
  {
    "id_contacto": 100,
    "nombre": "Tomás Alcántara",
    "telefono": "5512340100",
    "email": "tomas.alcantara@gmail.com"
  }
]

def test_5():
   response = requests.get(f"{URL}/v2/contactos/0/0")
   data = response.json()
   assert response.status_code == 200
   assert data == []

