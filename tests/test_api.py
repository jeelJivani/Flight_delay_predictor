from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200



def test_predict_unknown_weather():
    response = client.post("/predict", json={
        "flight_hour": 23,
        # "weather": "Snow",
        "weather": "Tornado",
        "airline": "EasyJet"
    })
    assert response.status_code == 422