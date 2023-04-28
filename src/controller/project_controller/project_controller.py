from flask import request, jsonify
from src.dao.project_dao.project_dao import ProjectDAO
from src.dto.project_dto.project_dto import Project
from src.http_status_code_enum import HttpCode
class ProjectController:

    projectDAO = ProjectDAO()

    def __init__(self) -> None:
        pass

    def create_project(self,json):
        project_name = json["project_name"]
        status = json["status"]
        content = json["content"]
        # fake id to init project object
        project = Project(1,project_name, status, content)
        try:
            project = self.projectDAO.create_project(project)
            print(project)
            return jsonify(project)
        except Exception as e:
            return "Fail to create project", HttpCode.BadRequest.value
    
    # def get_all_users(self):
    #     users = self.userDAO.get_all_user()
    #     return jsonify(users)
    
    # def get_user_by_userEmail(self, userEmail):
    #     user = self.userDAO.get_user_by_userEmail(userEmail)
    #     return jsonify(user)
    
    # def delete_user_by_userEmail(self, userEmail):
    #     result = self.userDAO.delete_user_by_userEmail(userEmail)
    #     return jsonify(result)
    
    # def update_user_by_userEmail(self, json):
    #     id = json["id"]
    #     user_email = json["user_email"]
    #     user_password = json["user_password"]
    #     project_id = json["project_id"]
    #     user = User(id, user_email, user_password, project_id)
    #     result = self.userDAO.update_user_by_userEmail(user_email, user)
    #     if result == None:
    #         return "Fail to update", HttpCode.BadRequest.value
    #     else:
    #         return jsonify(result)