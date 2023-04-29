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
    
    # Get All Task unit test
    def testGetAllTask(self):
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
    
    # Update Task unit test
    def testUpdateTask(self):
        taskDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)
        expectedMessage = "update task successful"
        expectedTaskList = [
            {
                "id": 1,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test"
            }
        ] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        self.taskController.taskDao.UpdateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.UpdateTask(task)
        assert result == expectedMessage

    def testUpdateTaskWhereIdIsNotSpecified(self):
        taskDict = {
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)
        expectedMessage = "id is not specified"
        result = self.taskController.UpdateTask(task)
        assert result == expectedMessage

    def testUpdateTaskWhereTaskDoesNotExist(self):
        taskDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test"
        }
        task = Task(**taskDict)
        expectedMessage = "task does not exist in database"
        expectedTaskList = [] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        result = self.taskController.UpdateTask(task)
        assert result == expectedMessage

    # delete task unit test 
    def testDeleteTask(self):
        taskId = "1"
        expectedMessage = "delete task successful"
        expectedTaskList = [
            {
                "id": 1,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test"
            }
        ] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        self.taskController.taskDao.DeleteTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.DeleteTask(taskId)
        assert result == expectedMessage
    
    def testDeleteTaskWhereIDIsNotSpecified(self):
        taskId = ""
        expectedMessage = "task id not defined"
        result = self.taskController.DeleteTask(taskId)
        assert result == expectedMessage

    def testDeleteTaskWhereTaskDoesNotExist(self):
        taskId = "1"
        expectedMessage = "task does not exist in database"
        expectedTaskList = [] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        result = self.taskController.DeleteTask(taskId)
        assert result == expectedMessage
