import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert "Bienvenue sur mon premier projet CI/CD" in response.get_data(as_text=True)

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0

def test_about():
    client = app.test_client()
    response = client.get("/About")

    assert response.status_code == 200
    assert "À propos de mon projet CI/CD" in response.get_data(as_text=True)