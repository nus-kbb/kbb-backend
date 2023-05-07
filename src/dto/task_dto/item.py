from src.dto.task_dto.status_enum import Status
from src.controller.task_controller.item_category import ItemCategory

class Item: 
    defaultStatus = Status.WAITING.value
    defaultType = ItemCategory.Task.value
    
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            self.__dict__[key] = value
        pass
    
    def __repr__(self) -> str:
        return f"Task({self.project_id}, {self.user_id}, {self.status}, {self.content}, {self.type})"
    
    def Validate(self):
        if not hasattr(self, "project_id"):
            return "project_id is not specified"
        elif not hasattr(self, "user_id"):
            return "user_id is not specified"
        elif not hasattr(self, "status"):
            self.status = self.defaultStatus
        elif not hasattr(self, "type"):
            self.type = self.defaultType
    
    def ValidateWithID(self):
        if not hasattr(self, "project_id"):
            return "project_id is not specified"
        elif not hasattr(self, "user_id"):
            return "user_id is not specified"
        elif not hasattr(self, "id"):
            return "id is not specified"
        elif not hasattr(self, "status"):
            self.status = self.defaultStatus
        elif not hasattr(self, "type"):
            self.type = self.defaultType