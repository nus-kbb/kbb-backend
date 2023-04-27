import unittest.mock as mock
from flask import jsonify, request
from src.app import app
import unittest
import json

from src.controller.task_controller.task_controller import TaskController
from src.dto.task_dto.task_dto import Task
from src.dto.task_dto.task_dto import Status



class TestUserController(unittest.TestCase):

    def setUp(self) -> None:
         self.app_context = app.app_context()
         self.app_context.push()
         self.taskController = TaskController()

    def tearDown(self) -> None:
        self.app_context.pop()
        pass

    # Create Task Unit Test
    def testCreateTask(self):
        taskDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)

        expectedMessage = "create task successful"
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(task)
        assert result == expectedMessage
    
    def testCreateTaskWithNoProjectId(self):
        taskDict = {
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)
        
        expectedMessage = "project_id is not specified"
        result = self.taskController.CreateTask(task)
        assert result == expectedMessage
    
    def testCreateTaskWithNoUserId(self):
        taskDict = {
            "project_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)

        expectedMessage = "user_id is not specified"
        result = self.taskController.CreateTask(task)
        assert result == expectedMessage
    
    def testCreateTaskWithNoStatus(self):
        taskDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "content": "test"
        }
        task = Task(**taskDict)

        expectedMessage = "create task successful"
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(task)
        assert result == expectedMessage
    
    # Get All Users unit test
    def testGetAllUsers(self):
        taskList = []    
        for index in range(5):    
            taskDict = {
                "id": index,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test"
            }
            taskList.append(taskDict)
        self.taskController.taskDao.GetAllTask = mock.Mock(return_value=taskList)
        result = self.taskController.GetAllTask()
        assert json.dumps(result, default=str) == json.dumps(taskList)
        
        

