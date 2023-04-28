import pytest
from src.app import app
from src.controller.user_controller.user_controller import UserController
from src.dto.user.user_dto import User


def test_index_route():
    response = app.test_client().get('/home')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Serving Hello world!'