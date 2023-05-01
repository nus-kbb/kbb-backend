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
    
    def get_project_by_userID(self, userID):
        project = self.projectDAO.get_project_by_userID(userID)
        return jsonify(project)
    
    def delete_project_by_projectID(self, projectID):
        result = self.projectDAO.delete_project_by_projectID(projectID)
        return jsonify(result)
    
    def update_project_by_userEmail(self, json):
        id = json["id"]
        project_name = json["project_name"]
        status = json["status"]
        content = json["content"]
        project = Project(id, project_name, status, content)
        result = self.userDAO.update_user_by_userEmail(id, project)
        if result == None:
            return "Fail to update the project", HttpCode.BadRequest.value
        else:
            return jsonify(result)