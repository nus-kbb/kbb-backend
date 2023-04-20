from flask import Flask, request
from src.dto.task.task_dto import Task
from src.controller.task_controller.task_controller import TaskController
from src.enum.http_status_code import HttpStatusCode

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
        
        err = task.Parse(request.json)
        if err != None:
            return err, HttpStatusCode.BadRequest
        
        err = taskController.CreateTask(task)
        if err != None:
            return err, HttpStatusCode.BadRequest
        
        return "create task successful", HttpStatusCode.SuccessCode
    
    return 'Content-Type not supported!', HttpStatusCode.BadRequest

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)