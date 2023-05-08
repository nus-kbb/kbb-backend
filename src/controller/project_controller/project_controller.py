from flask import request, jsonify
from src.dao.project_dao.project_dao import ProjectDAO
from src.dao.user_dao.user_dao import UserDAO
from src.dto.project_dto.project_dto import Project
from src.dto.user.user_dto import User
from src.dto.user.user_role_enum import Role
from src.http_status_code_enum import HttpCode
class ProjectController:

    projectDAO = ProjectDAO()
    userDAO = UserDAO()

    def __init__(self) -> None:
        pass

    def create_project(self,json, userEmail):
        if userEmail == "":
            return "user email is undefined", HttpCode.BadRequest.value
        project_name = json["project_name"]
        content = json["content"]
        # fake id to init project object
        # Add default status
        project = Project(1,project_name, "ACTIVE", content)
        
        try:
            project = self.projectDAO.create_project(project)
            print("project creation: ", project)
        except Exception as e:
            return "Fail to create project", HttpCode.BadRequest.value
        finally:
            try:
                user = self.userDAO.get_user_by_userEmail(userEmail)
                if type(user) == str:
                    return "failed to get user by user email: " + user, HttpCode.BadRequest.value
                print("update user project id")
                user["project_id"] = project["id"]
                # project creator is always the admin
                user["role"] = Role.ADMIN.value
                userObj = User.from_dict(user)
                updatedUser = self.userDAO.update_user_by_userEmail(userEmail, userObj)
                if type(updatedUser) == str:
                    return "failed to update user by user email: " + updatedUser, HttpCode.BadRequest.value
                return jsonify(project)
            except Exception as e:
                return "failed to update user: " + str(e), HttpCode.BadRequest.value

    
    # def get_all_users(self):
    #     users = self.userDAO.get_all_user()
    #     return jsonify(users)
    
    def get_all_project(self):
        return jsonify(self.projectDAO.get_all_project())
    
    def get_all_project_names_only(self):
        projectList = self.projectDAO.get_all_project()
        projectNameList = []
        for p in projectList:
            projectNameList.append(p["project_name"])
        return jsonify(projectNameList)

    def get_project_by_userID(self, userID):
        project = self.projectDAO.get_project_by_userID(userID)
        return jsonify(project)
    
    def delete_project_by_projectID(self, projectID):
        result = self.projectDAO.delete_project_by_projectID(projectID)
        return jsonify(result)
    
    def update_project_by_projectID(self, json):
        id = json["id"]
        project_name = json["project_name"]
        status = json["status"]
        content = json["content"]
        project = Project(id, project_name, status, content)
        result = self.projectDAO.update_project_by_projectID(id, project)
        print(result)
        if result == None:
            return "Fail to update the project", HttpCode.BadRequest.value
        else:
            return jsonify(result)
    
    def join_project(self, userEmail, projectName):
        user = self.userDAO.get_user_by_userEmail(userEmail)
        if type(user) == str:
            return user
        if user["project_id"] is not None:
            return "user already has project"
        projectId = self.projectDAO.get_project_id_by_name(projectName)
        user["project_id"] = projectId
        userObj = User.from_dict(user)
        resultantUser = self.userDAO.update_user_by_userEmail(userEmail, userObj)
        return jsonify(resultantUser)