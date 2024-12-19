# Import from trirdparty
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import uvicorn

# Import from stl
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import from src
from src.models.model import ModelHandler

# Init a FastAPI container
app: FastAPI = FastAPI()

# Resolve the model path
current_dir: str = os.path.dirname(os.path.abspath(__file__))
model_path: str = os.path.join(current_dir, "..", "models", "artifacts", "sentimentAnalysis_model.h5")

# Load the model
print(f"Loading model from {model_path}")
modelHandler: ModelHandler = ModelHandler(model_path=model_path)

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/predict/")
async def predict(data: dict):
    """
    Endpoint to make predictions using the loaded model.
    """
    try:
        input_data = data.get("features", [])
        prediction = model.predict([input_data])
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Start the Uvicorn server to serve the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
model = ModelLoader.load_model()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction"}

@app.post("/predict/")
def predict(data: dict):
    input_data = data.get("features", [])
    prediction = model.predict([input_data])
    return {"prediction": prediction.tolist()}
"""
