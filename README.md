# ApisDe-mo
##### 1_. La Raiz
| No | Propiedad             | Detalle                                       |
| -- | --------------------- | --------------------------------------------- |
| 1  | Description           | Endpoint                                      |
| 2  | Summary               | Endpoint                                      |
| 3  | Method                | GET                                           |
| 4  | Endpoint              | `/`                                           |
| 5  | Authentication        | NA                                            |
| 6  | Query param           | NA                                            |
| 7  | Path param            | NA                                            |
| 8  | Data                  | NA                                            |
| 9  | Status code           | 202                                           |
| 10 | Response              | `{ "mensaje": "agenda", "time": "11/09/26" }` |
| 11 | Response type         | application/json                              |
| 12 | Status code (error)   | NA                                            |
| 13 | Response type (error) | NA                                            |
| 14 | Response (error)      | NA                                            |
| 15 | CURL                  | `curl -X GET http://127.0.0.1:8000/`          |

#### 2_. Contactos
| No | Propiedad             | Detalle                                                 |
| -- | --------------------- | --------------------------------------------------------|
| 1  | Description           | Obtiene la lista completa de contactos de la agenda     |
| 2  | Summary               | Endpoint para consultar todos los contactos registrados |
| 3  | Method                | GET                                                     |
| 4  | Endpoint              | `/v1/contactos`                                         |
| 5  | Authentication        | NA                                                      |
| 6  | Query param           | limit:int & skip:int                                    |
| 7  | Path param            | NA                                                      |
| 8  | Data                  | NA                                                      |
| 9  | Status code           | 200                                                     |
| 10 | Response              | {"table": "contactos", "items": [{"id_contacto": int, "nombre": str, "email": str, "telefono": str}], "count": int, "datetime": timestamp, "message": "Datos cargados exitosamente"}                                              |
| 11 | Response type         | application/json                                        |
| 12 | Status code (error)   | 500                                                     |
| 13 | Response type (error) | application/json                                        |
| 14 | Response (error)      | {"table": None, "items": [], "count": int, "datetime": timestamp, "message": "Ocurrio un error al cargar los datos"}|
| 15 | CURL                  | `curl -X GET http://127.0.0.1:8000/contactos`           |

#### 3_. Buscar Contactos
| No | Propiedad             | Detalle                                                 |
| -- | --------------------- | --------------------------------------------------------|
| 1  | Description           | /?id.contacto = 3|
| 2  | Summary               |  |
| 3  | Vercion               | v1                                                      |
| 3  | Method                | GET                                                     |
| 4  | Endpoint              | `/v1/contactos`                                         |
| 5  | Authentication        | NA                                                      |
| 6  | Query param           | limit:int & skip:int                                    |
| 7  | Path param            | NA                                                      |
| 8  | Data                  | NA                                                      |
| 9  | Status code           | 200                                                     |
| 10 | Response              | {"table": "contactos", "items": [{"id_contacto": int, "nombre": str, "email": str, "telefono": str}], "count": int, "datetime": timestamp, "message": "Datos cargados exitosamente"}                                              |
| 11 | Response type         | application/json                                        |
| 12 | Status code (error)   | 500                                                     |
| 13 | Response type (error) | application/json                                        |
| 14 | Response (error)      | {"table": None, "items": [], "count": int, "datetime": timestamp, "message": "Ocurrio un error al cargar los datos"}|
| 15 | CURL                  | `curl -X GET http://127.0.0.1:8000/contactos`           |