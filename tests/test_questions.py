def test_list_questions(client):
    response = client.get("/api/questions/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_question_unauthenticated(client, seed_visitor):
    response = client.post(
        "/api/questions/",
        {
            "question": "How are you?",
            "visitor": seed_visitor.id,
        },
    )
    assert response.status_code == 401


def test_create_question_authenticated(auth_client, seed_visitor):
    response = auth_client.post(
        "/api/questions/",
        {
            "question": "How are you?",
            "visitor": seed_visitor.id,
        },
    )
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["question"] == "How are you?"
    assert response.json()["visitor"] == seed_visitor.id
    assert response.json()["votes"] == 0
