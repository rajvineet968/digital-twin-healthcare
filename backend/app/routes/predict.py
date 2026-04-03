from fastapi import APIRouter
from ai_engine.inference.predict_all import predict_all
from digital_twin.twin_engine import DigitalTwin

router = APIRouter()

twin = DigitalTwin()

@router.post("/predict")
def predict(data: dict):
    twin.update(data)

    prediction = predict_all(data)
    simulation = twin.simulate_future()

    return {
        "prediction": prediction,
        "simulation": simulation
    }