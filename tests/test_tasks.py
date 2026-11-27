def test_create_task_returns_201(client):
    response = client.post("/tasks", json={"title": "Write report"})
    
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == "Write report"
    assert body["status"] == "todo"


def test_invalid_status_is_rejected(client):
    response = client.post("/tasks", json={"title": "Write report", "status": "invalid"})
    
    assert response.status_code == 422


def test_blank_title_is_rejected(client):
    response = client.post("/tasks", json={"title": " "})

    assert response.status_code == 422


def test_unknown_task_id_returns_404_on_get(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_unknown_task_id_returns_404_on_patch(client):
    response = client.patch("/tasks/999", json={"status": "done"})

    assert response.status_code == 404


def test_unknown_task_id_returns_404_on_delete(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404


def test_non_positive_task_id_is_rejected(client):
    response = client.get("/tasks/0")

    assert response.status_code == 422


def test_create_rejects_explicit_id(client):
    response = client.post("/tasks", json={"id": 999, "title": "Write report"})

    assert response.status_code == 422


def test_patch_changes_only_status(client):
    created = client.post("/tasks", json={"title": "Write report"})
    task_id = created.json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"status": "done"})

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == task_id
    assert body["title"] == "Write report"
    assert body["status"] == "done"


def test_patch_rejects_null_title(client):
    created = client.post("/tasks", json={"title": "Write report"})
    task_id = created.json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"title": None})

    assert response.status_code == 422


def test_delete_returns_204_then_get_returns_404(client):
    created = client.post("/tasks", json={"title": "Write report"})
    task_id = created.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    get_response = client.get(f"/tasks/{task_id}")

    assert delete_response.status_code == 204
    assert get_response.status_code == 404

