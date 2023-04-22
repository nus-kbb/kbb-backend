import pytest
import json
from src.controller.user_controller.user_controller import UserController

def testUserController():
    userController = UserController()
    assert userController != None

# def testGetAllUsers():
#     userController = UserController()
#     result = userController.get_all_users()
#     print(result)
#     assert result

# def testCreateUser():
#     userController = UserController()
#     result = userController.create_user()
#     print(result)
#     assert result

