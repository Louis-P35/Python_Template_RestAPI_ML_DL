from fastapi import FastAPI
from src.models.model_loader import load_model

app = FastAPI()

model = load_model()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction"}

@app.post("/predict/")
def predict(data: dict):
    input_data = data.get("features", [])
    prediction = model.predict([input_data])
    return {"prediction": prediction.tolist()}
