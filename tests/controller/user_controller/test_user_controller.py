import pytest
import json
from src.controller.user_controller.user_controller import UserController
from src.dto.user.user_dto import User
import unittest.mock as mock
from flask import jsonify, request
from src.app import app
import unittest

class TestUserController(unittest.TestCase):

    def setUp(self) -> None:
         self.app_context = app.app_context()
         self.app_context.push()
         self.userController = UserController()

    def tearDown(self) -> None:
        self.app_context.pop()
        pass

    def testUserControllerDAONotEmpty(self):
        result = self.userController.userDAO
        assert result != None

    def testGetAllUsers(self):
        users = [User("useremail1", "userpassword1", "projectid1").to_dict(), User("useremail2", "userpassword2", "projectid2").to_dict()]
        self.userController.userDAO.get_all_user = mock.Mock(return_value = users)
        result = self.userController.get_all_users()
        assert result.json == users

    def testGetUserByUserEmail(self):
        user = User("useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.get_user_by_userEmail = mock.Mock(return_value = user)
        result = self.userController.get_user_by_userEmail("useremail1")
        assert result.json == user

    # def testCreateUser(self):
    #     user = User("useremail1", "userpassword1", "projectid1").to_dict()
    #     self.userController.userDAO.create_user = mock.Mock(return_value = user)
    #     r = request.post('localhost', json=User.from_dict(user).to_json())
    #     result = self.userController.create_user(r)
    #     assert result.json == user
        

    def deleteUserByUserEmail(self):
        user = User("useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.delete_user_by_userEmail = mock.Mock(return_value = 'Success')
        result = self.userController.delete_user_by_userEmail("useremail1")
        assert result.json == user

    def updateUserByUserEmail(self):
        return 

if __name__=='__main__':
    unittest.main()


# def testCreateUser():
#     userController = UserController()
#     result = userController.create_user()
#     print(result)
#     assert result

