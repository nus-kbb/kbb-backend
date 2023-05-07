import enum

class ItemCategory(enum.Enum):
    """
    ItemCategory is an enum class that represents the category of an item.
    """
    Story = "story"
    Bug = "bug"
    Task = "task"

    def __str__(self):
        return self.name.lower()