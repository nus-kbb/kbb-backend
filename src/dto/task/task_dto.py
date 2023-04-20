class Task:
    def __init__(self, projectId, userId, jsonContent):
        self.project_id=projectId
        self.user_id = userId
        self.content = jsonContent

    def SetAssignee(self, assigneeId):
        self.assignee = assigneeId
