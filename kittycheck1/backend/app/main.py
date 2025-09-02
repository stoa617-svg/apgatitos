from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI()

class Control(BaseModel):
    cat_name: str
    age_months: int
    weight_g: int
    sex: str
    stage: str
    dewormer: str
    base_dose_mg_per_kg: float | None = None
    date: str
    notes: str | None = None

@app.get("/saludo/{name}")
def saludo(name: str):
    return {"message": f"Hola {name}, KittyCheck está funcionando 🐾"}

@app.post("/api/controls")
def add_control(control: Control):
    # Calcular dosis
    dose_mg = (control.weight_g / 1000) * (control.base_dose_mg_per_kg or 5.0)
    
    # Predecir próximo control
    if control.age_months < 3:
        next_date = datetime.fromisoformat(control.date) + timedelta(days=15)
    elif control.age_months < 6:
        next_date = datetime.fromisoformat(control.date) + timedelta(days=30)
    else:
        next_date = datetime.fromisoformat(control.date) + timedelta(days=90)

    return {
        "cat": control.cat_name,
        "dose_mg": round(dose_mg, 2),
        "next_control": next_date.date().isoformat()
    }
