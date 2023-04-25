from src.controller.user_controller.user_controller import UserController
from src.dto.user.user_dto import User
import unittest.mock as mock
from flask import jsonify, request
from src.app import app
from src.http_status_code_enum import HttpCode
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
        users = [User(1, "useremail1", "userpassword1", "projectid1").to_dict(), User(2, "useremail2", "userpassword2", "projectid2").to_dict()]
        self.userController.userDAO.get_all_user = mock.Mock(return_value = users)
        result = self.userController.get_all_users()
        assert result.json == users

    def testGetAllUsersEmpty(self):
        users = []
        self.userController.userDAO.get_all_user = mock.Mock(return_value = users)
        result = self.userController.get_all_users()
        assert result.json == users

    def testGetUserByUserEmail(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.get_user_by_userEmail = mock.Mock(return_value = user)
        result = self.userController.get_user_by_userEmail("useremail1")
        assert result.json == user

    def testCreateUser(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.create_user = mock.Mock(return_value = user)
        result = self.userController.create_user(user)
        assert result.json == user

    def testCreateUser_DBError(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.create_user = mock.Mock(return_value = Exception)
        result = self.userController.create_user(user)
        assert result == ("Fail to create", HttpCode.BadRequest.value)

    def testUpdateUserByUserEmail(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.update_user_by_userEmail = mock.Mock(return_value = user)
        result = self.userController.update_user_by_userEmail(user)
        assert result.json == user

    def testDeleteUserByUserEmail(self):
        self.userController.userDAO.delete_user_by_userEmail = mock.Mock(return_value = 'Success')
        result = self.userController.delete_user_by_userEmail("useremail1")
        assert result.json == 'Success'

    def testUpdateUserByUserEmail(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.update_user_by_userEmail = mock.Mock(return_value = user)
        result = self.userController.update_user_by_userEmail(user)
        assert result.json == user
    
    def testUpdateUserByUserEmailUser_NotFound(self):
        user = User(1, "useremail1", "userpassword1", "projectid1").to_dict()
        self.userController.userDAO.update_user_by_userEmail = mock.Mock(return_value = None)
        result = self.userController.update_user_by_userEmail(user)
        assert result == ("Fail to update", HttpCode.BadRequest.value)


if __name__=='__main__':
    unittest.main()


