import unittest.mock as mock
from flask import jsonify, request
from src.app import app
import unittest
import json

from src.controller.task_controller.task_controller import TaskController
from src.dto.task_dto.task_dto import Task
from src.dto.task_dto.task_dto import Status
from src.controller.task_controller.item_factory_method import ItemFactoryMethod


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
        
    
    def testCreateBug(self):
        bugDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "type": "bug",
            "content": "test",
            "version": "1.0.0"
        }
        
        bug = ItemFactoryMethod().create_Item(**bugDict)
        
        expectedMessage = "create bug successful"
        
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(bug)
        assert result == expectedMessage
        
    def testCreateBug_InvalidVersion(self):
        bugDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "type": "bug",
            "content": "test",
        }
        
        bug = ItemFactoryMethod().create_Item(**bugDict)
        
        expectedMessage = "version is not specified"
        
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(bug)
        assert result == expectedMessage
    
    def testCreateStory(self):
        storyDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "type": "story",
            "content": "test",
            "story_points": 1
        }
        
        story = ItemFactoryMethod().create_Item(**storyDict)
        
        expectedMessage = "create bug successful"
        
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(story)
        assert result == expectedMessage
        
    def testCreateStory_Invalid(self):
        storyDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "type": "story",
            "content": "test",
            "story_points": 1
        }
        
        story = ItemFactoryMethod().create_Item(**storyDict)
        
        expectedMessage = "create bug successful"
        
        self.taskController.taskDao.CreateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.CreateTask(story)
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

    # Get Task By Project Id
    def testGetTaskByProjectId(self):
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
        self.taskController.taskDao.GetTaskByProjectId = mock.Mock(return_value=taskList)
        result = self.taskController.GetTaskByProjectId("1")
        assert json.dumps(result, default=str) == json.dumps(taskList)

    def testGetTaskByProjectIdWhereProjectIdDidNotExist(self):
        taskList = []
        self.taskController.taskDao.GetTaskByProjectId = mock.Mock(return_value=taskList)
        result = self.taskController.GetTaskByProjectId("0")
        assert json.dumps(result, default=str) == json.dumps(taskList)

    def testGetTaskByProjectIdWhereProjectIdIsNotSpecified(self):
        expectedResul="project id not defined"
        result = self.taskController.GetTaskByProjectId("")
        assert json.dumps(result, default=str) == json.dumps(expectedResul)
    
    # Update Task unit test
    def testUpdateTask(self):
        taskDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test",
            "type": "task"
        }
        task = ItemFactoryMethod().create_Item(**taskDict)
        expectedMessage = "update task successful"
        expectedTaskList = [
            {
                "id": 1,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test",
                "type": "task"
            }
        ] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        self.taskController.taskDao.UpdateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.UpdateTask(task)
        assert result == expectedMessage

    
    def testUpdateStory(self):
        storyDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test",
            "story_points": 1,
            "type": "story"
        }
        story = ItemFactoryMethod().create_Item(**storyDict)
        expectedMessage = "update task successful"
        expectedTaskList = [
            {
                "id": 1,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test",
                "story_points": 1,
                "type": "story"
            }
        ] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        self.taskController.taskDao.UpdateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.UpdateTask(story)
        assert result == expectedMessage
        
    def testUpdateBug(self):
        bugDict = {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "status": Status.WAITING.value,
            "content": "test",
            "version": "1.0",
            "type": "bug"
        }
        bug = ItemFactoryMethod().create_Item(**bugDict)
        expectedMessage = "update task successful"
        expectedTaskList = [
            {
                "id": 1,
                "project_id": 1,
                "user_id": 1,
                "status": Status.WAITING.value,
                "content": "test",
                "version": "1.0",
                "type": "bug"
            }
        ] 
        self.taskController.taskDao.GetTaskById = mock.Mock(return_value=expectedTaskList)
        self.taskController.taskDao.UpdateTaskEntry = mock.Mock(return_value=expectedMessage)
        result = self.taskController.UpdateTask(bug)
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
