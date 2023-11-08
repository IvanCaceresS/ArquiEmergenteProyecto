from fastapi import FastAPI
from typing import List

# Define un modelo Pydantic para tus escenarios
from pydantic import BaseModel

class Scenario(BaseModel):
    id: int
    name: str
    author: str = "Carlos Garcia"
    descripcion: str

app = FastAPI()

# Datos simulados
scenarios_data = [
    {"id": 1, "name": "Escenario Santiago", "descripcion": "Escenario base Santiago v1"},
    {"id": 2, "name": "Escenario Temuco", "descripcion": "Escenario base Temuco v1"}
]

@app.get("/scenarios", response_model=List[Scenario])
async def get_scenarios():
    return scenarios_data
