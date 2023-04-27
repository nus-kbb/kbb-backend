from flask import Flask, request, jsonify
from src.dto.task_dto.task_dto import Task
from src.controller.task_controller.task_controller import TaskController
from src.controller.user_controller.user_controller import UserController
from src.controller.project_controller.project_controller import ProjectController
from src.http_status_code_enum import HttpCode, HTTPContentType
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
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

@app.route('/task/get_all_task', methods=['GET'])
def get_all_task_handler():
    taskList = taskController.GetAllTask()
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



@app.route('/project', methods=['POST'])
def project_handler():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == HTTPContentType.JSON.value:
            return ProjectController.create_project(request.json)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    else:
        return "Invalid User Request", HttpCode.BadRequest.value



if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)