from src.dto.task_dto.status_enum import Status

class Task:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            self.__dict__[key] = value
        pass
    
    def SetAssignee(self, assigneeId) -> None:
        self.assignee = assigneeId

    def Parse(self, jsonObj):
        jsonObj, err = self.Validate(jsonObj)
        if err != None:
            return err
        # set attributes
        self.project_id = jsonObj["project_id"]
        self.user_id = jsonObj["user_id"]
        self.content = jsonObj["content"]
        if "status" not in jsonObj:
            self.status = Status.WAITING
        else:
            self.status = jsonObj["status"]
        return None
    
    def Validate(self, jsonObj):
        if "project_id" not in jsonObj:
            return None, "project_id is not specified"
        elif "user_id" not in jsonObj:
            return None, "user_id is not specified"
        elif "content" not in jsonObj:
            return None, "content cannot be blank"
        elif "status" in jsonObj:
            if jsonObj["status"] != Status.WAITING.value or jsonObj["status"] != Status.DEVELOPING.value  or jsonObj["status"] != Status.TESTING.value or jsonObj["status"] != Status.DONE.value:
                return None, "invalid status"
        else:
            return jsonObj, None

    def ParseDict(self, dictObj):
        self.id = dictObj["id"]
        self.project_id = dictObj["project_id"]
        self.user_id = dictObj["user_id"]
        self.content = dictObj["content"]
        self.status = dictObj["status"]


