from flask import request, jsonify
from src.dao.user_dao.user_dao import UserDAO
from src.dto.user.user_dto import User
from src.http_status_code_enum import HttpCode
class UserController:

    userDAO = UserDAO()

    def __init__(self) -> None:
        pass

    def create_user(self,json):
        user_email = json["user_email"]
        user_password = json["user_password"]
        # project_id = json["project_id"]
        # fake id to init User object
        user = User(None,user_email, user_password, None)

        if result != None:
            return "user already exist", HttpCode.BadRequest.value
        try:
            user = self.userDAO.create_user(user)
            print(user)
            return jsonify(user)
        except Exception as e:
            return "Fail to create", HttpCode.BadRequest.value
    
    def get_all_users(self):
        users = self.userDAO.get_all_user()
        return jsonify(users)
    
    def get_all_users_by_projectId(self, projectId):
        if projectId == None or projectId == "":
            return "Project id is undefined"
        else:
            users = self.userDAO.get_all_users_by_projectId(projectId)
            return jsonify(users)
    
    def get_user_by_userEmail(self, userEmail):
        user = self.userDAO.get_user_by_userEmail(userEmail)
        return jsonify(user)
    
    def delete_user_by_userEmail(self, userEmail):
        result = self.userDAO.delete_user_by_userEmail(userEmail)
        return jsonify(result)
    
    def update_user_by_userEmail(self, json):
        id = json["id"]
        user_email = json["user_email"]
        user_password = json["user_password"]
        project_id = json["project_id"]
        user = User(id, user_email, user_password, project_id)
        result = self.userDAO.update_user_by_userEmail(user_email, user)
        if result == None:
            return "Fail to update", HttpCode.BadRequest.value
        else:
            return jsonify(result)