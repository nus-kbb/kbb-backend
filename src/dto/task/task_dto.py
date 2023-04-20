import json
from src.enum.status import Status

class Task:
    def __init__(self) -> None:
        pass

    def SetAssignee(self, assigneeId) -> None:
        self.assignee = assigneeId

    def Parse(self, jsonString):
        data, err = self.Validate(jsonString)
        if err != None:
            return err
        # set attributes
        self.project_id = data["project_id"]
        self.user_id = data["user_id"]
        self.content = data["content"]
        if data["status"] != None:
            self.status = Status.WAITING
        else:
            self.status = data["status"]
        return None
    
    def Validate(jsonString):
        try:
            data = json.loads(jsonString)
        except ValueError as err:
            return None, err
        finally:
            if data["project_id"] != None:
                return None, "project_id is not specified"
            elif data["user_id"] != None:
                return None, "user_id is not specified"
            elif data["content"] != None:
                return None, "content cannot be blank"
            elif data["status"] != None:
                if data["status"] != Status.WAITING or data["status"] != Status.DEVELOPING  or data["status"] != Status.TESTING or data["status"] != Status.DONE:
                    return None, "invalid status"
            else:
                return data, None


