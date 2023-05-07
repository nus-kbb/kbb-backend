from src.controller.task_controller.item_category import ItemCategory
from src.dto.task_dto.story_dto import Story
from src.dto.task_dto.bug_dto import Bug
from src.dto.task_dto.task_dto import Task

class ItemFactoryMethod:
    def __init__(self) -> None:
        pass
    
    def create_Item(self, **kwargs):
        try:
            item_type = self.validate_Type_Exists(kwargs["type"])
        except:
            return None
        if item_type == ItemCategory.Story:
            return Story(**kwargs)
        elif item_type == ItemCategory.Bug:
            return Bug(**kwargs)
        elif item_type == ItemCategory.Task:
            return Task(**kwargs)
        else:
            return None

    def validate_Type_Exists(self, type):
        if type == "story":
            return ItemCategory.Story
        elif type == "bug":
            return ItemCategory.Bug
        elif type == "task":
            return ItemCategory.Task
        else:
            return None