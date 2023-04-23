from flask import Flask, request
from src.controller.task_controller.task_dto.task_dto import Task
from src.controller.task_controller.task_controller import TaskController
from src.controller.user_controller.user_controller import UserController
from src.http_status_code_enum import HttpCode
import json

app = Flask(__name__)
taskController = TaskController()
userController = UserController()

@app.route('/home')
def hello_world():
    return 'Serving Hello world!'

@app.route('/task/create_task', methods=['POST'])
def create_task_handler():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        task = Task()
        print(request.json)
        err = task.Parse(request.json)
        if err != None:
            return err, HttpCode.BadRequest.value
        
        err = taskController.CreateTask(task)
        if err != None:
            return err, HttpCode.BadRequest.value
        
        return "create task successful", HttpCode.Success.value
    
    return 'Content-Type not supported!', HttpCode.BadRequest.value

@app.route('/task/get_all_task', methods=['GET'])
def get_all_task_handler():
    taskList = taskController.GetAllTask()
    jsonTaskList = json.dumps(taskList, indent = 8)
    return jsonTaskList, HttpCode.Success.value, {'Content-Type': 'application/json'}

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
        if request.headers.get('Content-Type') == 'application/json':
            return userController.create_user(request)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'PUT':
        if request.headers.get('Content-Type') == 'application/json':
            return userController.update_user_by_userEmail(request)
        else:
            return "Invalid Content-Type", HttpCode.BadRequest.value
    elif request.method == 'DELETE':
        userEmail = request.args.get('userEmail',default='',type=str)
        return userController.delete_user_by_userEmail(userEmail)
    else:
        return "Invalid User Request", HttpCode.BadRequest.value


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)