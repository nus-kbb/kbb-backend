from flask import Flask, request, jsonify
from flask_cors import CORS
from src.dto.task_dto.task_dto import Task
from src.controller.task_controller.task_controller import TaskController
from src.controller.user_controller.user_controller import UserController
from src.controller.project_controller.project_controller import ProjectController
from src.http_status_code_enum import HttpCode, HTTPContentType
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
taskController = TaskController()
userController = UserController()

@app.route('/home')
def hello_world():
    return 'Serving Hello world!'

@app.route('/task/create_task', methods=['POST'])
def create_task_handler():
    content_type = request.headers.get('Content-Type')
    if (content_type == HTTPContentType.JSON.value):
        task = Task(**request.json)
        
        err = taskController.CreateTask(task)
        if err != None:
            return err, HttpCode.BadRequest.value
        
        return "create task successful", HttpCode.Success.value
    
    return 'Content-Type not supported!', HttpCode.BadRequest.value

@app.route('/task/update_task', methods=['POST'])
def update_task_handler():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        task = Task(**request.json)
        
        err = taskController.UpdateTask(task)
        if err != None:
            return err, HttpCode.BadRequest.value
        
        return "update task successful", HttpCode.Success.value
    
    return 'Content-Type not supported!', HttpCode.BadRequest.value

@app.route('/task/delete_task', methods=['POST'])
def delete_task_handler():
    taskId = request.args.get('id',default='',type=str)
    err = taskController.DeleteTask(taskId)
    if err != None:
        return err, HttpCode.BadRequest.value
        
    return "delete task successful", HttpCode.Success.value

@app.route('/task/get_all_task', methods=['GET'])
def get_all_task_handler():
    taskList = taskController.GetAllTask()
    return json.dumps(taskList, indent=4, default=str), HttpCode.Success.value, {'Content-Type': HTTPContentType.JSON.value}

@app.route('/task/get_task', methods=['GET'])
def get_task_by_project_id():
    projectId = request.args.get('project_id',default='',type=str)
    taskList = taskController.GetTaskByProjectId(projectId)
    return json.dumps(taskList, indent=4, default=str), HttpCode.Success.value, {'Content-Type': HTTPContentType.JSON.value}

@app.route('/user', methods=['GET'])
def user_handler_Get():
    userEmail = request.args.get('userEmail',default='',type=str)
    if len(userEmail) == 0:
        return userController.get_all_users()
    elif len(userEmail) > 0:
        return userController.get_user_by_userEmail(userEmail)
    else:
        return "Invalid Get User", HttpCode.BadRequest.value
    
@app.route('/user/get_user_by_project_id', methods=['GET'])
def user_handler_Get_by_project_id():
    projectId = request.args.get('projectId',default='',type=str)
    if len(projectId) > 0:
        return userController.get_all_users_by_projectId(projectId)
    else:
        return "Invalid Get User", HttpCode.BadRequest.value


@app.route('/user', methods=['POST', 'PUT', 'DELETE'])
def user_handler():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            return userController.create_user(request.json)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'PUT':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            return userController.update_user_by_userEmail(request.json)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'DELETE':
        userEmail = request.args.get('userEmail',default='',type=str)
        return userController.delete_user_by_userEmail(userEmail)
    else:
        return "Invalid User Request", HttpCode.BadRequest.value



@app.route('/project', methods=['POST','GET','DELETE','PUT'])
def project_handler():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            userEmail = request.args.get('user_email',default='',type=str)
            return ProjectController().create_project(request.json, userEmail)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'DELETE':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            #print(request.json)
            projectID = request.json['project_id']
            #print(projectID)
            return ProjectController().delete_project_by_projectID(projectID)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'GET':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            print(request.json)
            userID = request.json['user_id']
            print(userID)
            return ProjectController().get_project_by_userID(userID)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'PUT':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            print(request.json)
            return ProjectController().update_project_by_projectID(request.json)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    else:
        return "Invalid User Request", HttpCode.BadRequest.value

@app.route('/project/all', methods=['GET'])
def get_all_project_handler():
    return ProjectController().get_all_project()

@app.route('/project/all_names', methods=['GET'])
def get_all_project_handler_names_only():
    return ProjectController().get_all_project_names_only()

@app.route('/project/join_project', methods=['POST'])
def join_project_handler():
    if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
        userEmail = request.json['user_email']
        projectName = request.json['project_name']
        return ProjectController().join_project(userEmail, projectName)
    else:
        return "Invalid Content-Type", HttpCode.BadRequest.value


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)