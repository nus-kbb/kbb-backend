from flask import request, jsonify
from src.dao.user_dao.user_dao import UserDAO
from src.dto.user.user_dto import User
class UserController:

    userDAO = UserDAO()

    def __init__(self) -> None:
        pass

    def create_user(self,):
        user_email = request.json["user_email"]
        user_password = request.json["user_password"]
        project_id = request.json["project_id"]
        user = User(user_email, user_password, project_id)
        user = self.userDAO.create_user(user)
        return jsonify(user)
    
    def get_all_users(self):
        users = self.userDAO.get_all_user()
        print("get all users")
        return jsonify(users)

        
