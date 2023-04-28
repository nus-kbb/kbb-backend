from src.dto.task_dto.status_enum import Status

defaultStatus = Status.WAITING.value

class Task:

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            self.__dict__[key] = value
        pass
    
    def __repr__(self) -> str:
        return f"Task({self.project_id}, {self.user_id}, {self.status}, {self.content})"
    
    def SetAssignee(self, assigneeId) -> None:
        self.assignee = assigneeId
    
    def Validate(self):
        if not hasattr(self, "project_id"):
            return "project_id is not specified"
        elif not hasattr(self, "user_id"):
            return "user_id is not specified"
        elif not hasattr(self, "status"):
            self.status = defaultStatus
    
    def ValidateWithID(self):
        err = self.Validate()
        if not hasattr(self, "id"):
            return "task id is not specified"
        return err
    
