class Task:
    def __init__(self, id, name, assigneeId):
        self.id = id
        self.name = name
        self.assignee =  assigneeId
        pass

    def SetAssignee(self, assigneeId):
        self.assignee = assigneeId
