from flask import Flask, request
from .controller.task_controller.task_dto.task_dto import Task
from .controller.task_controller.task_controller import TaskController
from .http_status_code_enum import HttpCode
import json

app = Flask(__name__)
taskController = TaskController()


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

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)