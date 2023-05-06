from src.dto.task_dto.item import Item

class Story(Item):
    
    version = None
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        pass
    
    def __repr__(self) -> str:
        return f"Story({self.project_id}, {self.user_id}, {self.status}, {self.content}, {self.type}, {self.story_points})"
    
    def Validate(self):
        if not hasattr(self, "story_points") or self.story_points == None:
            return "story_points is not specified"
        elif self.version != None:
            return "version is not required"
        return super().Validate()
    
    def ValidateWithID(self):
        if not hasattr(self, "story_points") or self.story_points == None:
            return "story_points is not specified"
        elif self.version != None:
            return "version is not required"
        return super().ValidateWithID()