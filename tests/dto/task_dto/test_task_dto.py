from src.dto.task_dto.task_dto import Task
import unittest
import unittest.mock as mock
from src.app import app

class TestTask(unittest.TestCase):
    
    task_json = None
    
    def setUp(self) -> None:
         self.app_context = app.app_context()
         self.app_context.push()
         self.task_json = None

    def tearDown(self) -> None:
        self.app_context.pop()
        pass
    
    def testTaskValidate_Success(self):
        self.task_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "task"
        }
        
        _task = Task(**self.task_json)
        assert _task.Validate() == None
        assert _task.ValidateWithID() == None
        
    def testTaskValidate_Fail(self):
        self.task_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "story_points": 1,
            "version": "1.0",
            "type": "story"
        }
        
        _task = Task(**self.task_json)
        assert _task.Validate() == "version is not required"
        assert _task.ValidateWithID() == "version is not required"
        
    def testTaskValidate_Fail_Storypoints(self):
        self.task_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "story_points": 1,
            "type": "story"
        }
        
        _task = Task(**self.task_json)
        assert _task.Validate() == "story_points is not required"
        assert _task.ValidateWithID() == "story_points is not required"
        
        
    def testTaskValidateId_Success(self):
        self.task_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "task"
        }
        
        _task = Task(**self.task_json)
        assert _task.ValidateWithID() == None

    def testTaskValidateId_Fail_project_id(self):
        self.task_json = {
            "id": "1",
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "story"
        }
        
        _task = Task(**self.task_json)
        assert _task.ValidateWithID() == "project_id is not specified"
        
    def testTaskValidateId_Fail_user_id(self):
        self.task_json = {
            "id": "1",
            "project_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "story"
        }
        
        _task = Task(**self.task_json)
        assert _task.ValidateWithID() == "user_id is not specified"