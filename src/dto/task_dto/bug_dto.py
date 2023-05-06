from src.dto.task_dto.item import Item

class Bug(Item):
    
    story_points = None
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        pass
    
    def __repr__(self) -> str:
        return f"Bug({self.project_id}, {self.user_id}, {self.status}, {self.content}, {self.type} ,{self.version})"
    
    def ValidateWithID(self):
        if not hasattr(self, "version") or self.version == None:
            return "version is not specified"
        elif self.story_points != None:
            return "story_points is not required"
        return super().ValidateWithID()
    
    def Validate(self):
        if not hasattr(self, "version") or self.version == None:
            return "version is not specified"
        elif self.story_points != None:
            return "story_points is not required"
        return super().Validate()