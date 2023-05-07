from src.dto.task_dto.bug_dto import Bug
import unittest
import unittest.mock as mock
from src.app import app

class Testbug(unittest.TestCase):
    
    bug_json = None
    
    def setUp(self) -> None:
         self.app_context = app.app_context()
         self.app_context.push()
         self.bug_json = None

    def tearDown(self) -> None:
        self.app_context.pop()
        pass
    
    def testbugValidate_Success(self):
        self.bug_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "bug",
            "version": "1.0"
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.Validate() == None
        assert _bug.ValidateWithID() == None
        
    def testbugValidate_Fail(self):
        self.bug_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "story_points": 1,
            "version": "1.0",
            "type": "story"
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.Validate() == "story_points is not required"
        assert _bug.ValidateWithID() == "story_points is not required"
        
    def testbugValidate_Fail_Storypoints(self):
        self.bug_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "story_points": 1,
            "type": "story",
            "version": "1.0"
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.Validate() == "story_points is not required"
        assert _bug.ValidateWithID() == "story_points is not required"
        
        
    def testbugValidateId_Success(self):
        self.bug_json = {
            "id": "1",
            "project_id": 1,
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "bug",
            "version": "1.0"
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.ValidateWithID() == None

    def testbugValidateId_Fail_version(self):
        self.bug_json = {
            "id": "1",
            "user_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "story",
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.ValidateWithID() == "version is not specified"
        
    def testbugValidateId_Fail_user_id(self):
        self.bug_json = {
            "id": "1",
            "project_id": 1,
            "status": "developing",
            "content": "Content comes here",
            "type": "story",
            "version": "1.0"
        }
        
        _bug = Bug(**self.bug_json)
        assert _bug.ValidateWithID() == "user_id is not specified"