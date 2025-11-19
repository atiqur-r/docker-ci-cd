# test_app.py

def test_hello():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from CI/CD Docker Project" in response.data

