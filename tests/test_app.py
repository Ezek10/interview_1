from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_returns_ok_with_winner():
    input = {
        "player1":
            {
                "movimientos": ["SDD", "DSD", "SA", "DSD"],
                "golpes":["K", "P", "K", "P"]
            }, 
        "player2":
            {
                "movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],
                "golpes":["P", "K", "K", "K", "P", "k"]
            }
    }
    response = client.post(
        "/fight",
        json=input
    )

    assert response.status_code == 200

def test_returns_ok_with_draw():

    input = {
        "player1":
            {
                "movimientos": [""],
                "golpes":[""]
            }, 
        "player2":
            {
                "movimientos":[""],
                "golpes":[""]
            }
    }
    response = client.post(
        "/fight",
        json=input
    )

    assert response.status_code == 200

def test_response_text():
    input = {
        "player1":
            {
                "movimientos": ["SDa", "DSD", "SA", "DSD"],
                "golpes":["K", "P", "K", "P"]
            }, 
        "player2":
            {
                "movimientos":["DSD", "WSA", "ASA", "", "ASA", "SA"],
                "golpes":["P", "K", "K", "K", "P", "k"]
            }
    } 
    expected_response = [
        "¡El combate comenzo! Tonyn Stallone dara el primer golpe",
        "Tonyn Stallone dio una gran patada",
        "Arnaldor Shuatseneguer dio un puñetazo",
        "Tonyn Stallone lo revento con un Taladoken",
        "Arnaldor Shuatseneguer lo revento con un Remuyuken",
        "Tonyn Stallone dio una gran patada",
        "Arnaldor Shuatseneguer lo revento con un Remuyuken",
        "Tonyn Stallone murio, sus familiares van a llorarlo toda su vida",
        "Arnaldor Shuatseneguer sobrevivio, y le quedo 1 energia"
    ]

    response = client.post(
        "/fight",
        json=input
    )

    assert response.status_code == 200
    assert response.json() == expected_response
