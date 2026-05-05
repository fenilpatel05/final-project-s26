from app import app

def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"My Notes App" in response.data

def test_add_note():
    client = app.test_client()
    response = client.post("/add", data={"note": "Test note"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test note" in response.data
