from flask import request, jsonify
from src.dao.user_dao.user_dao import UserDAO
from src.dto.user.user_dto import User
from src.http_status_code_enum import HttpCode
class UserController:

    userDAO = UserDAO()

    def __init__(self) -> None:
        pass

    def create_user(self,request):
        user_email = request.json["user_email"]
        user_password = request.json["user_password"]
        project_id = request.json["project_id"]
        user = User(user_email, user_password, project_id)
        try:
            user = self.userDAO.create_user(user)
            return jsonify(user)
        except Exception as e:
            return "Fail to create. User_email must be unique", HttpCode.BadRequest.value
    
    def get_all_users(self):
        users = self.userDAO.get_all_user()
        return jsonify(users)
    
    def get_user_by_userEmail(self, userEmail):
        user = self.userDAO.get_user_by_userEmail(userEmail)
        return jsonify(user)