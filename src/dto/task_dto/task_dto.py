from src.dto.task_dto.status_enum import Status
from src.dto.task_dto.item import Item

class Task(Item):
    
    story_points = None
    version = None
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        pass
    
    def Validate(self):
        if self.version != None:
            return "version is not required"
        elif self.story_points != None:
            return "story_points is not required"
        return super().Validate()
    
    def ValidateWithID(self):
        if self.version != None:
            return "version is not required"
        elif self.story_points != None:
            return "story_points is not required"
        return super().ValidateWithID()
