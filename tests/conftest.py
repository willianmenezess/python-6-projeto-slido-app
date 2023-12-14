import pytest
from slido_app.models import Visitor
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def allow_db(db):
    pass


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(client):
    User.objects.create_user(username="testuser", password="testpassword")
    response = client.post(
        "/api/token/",
        {
            "username": "testuser",
            "password": "testpassword",
        },
    )
    assert response.status_code == 200
    token = response.json()["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client


@pytest.fixture
def seed_visitor():
    return Visitor.objects.create(
        name="Test Visitor", email="test_visitor@example.com"
    )
