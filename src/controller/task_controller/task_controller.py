from .task_dao.task_dao import TaskDao

class TaskController:
    taskDao = TaskDao()
    def __init__(self) -> None:
        pass

    def CreateTask(self, task):
        self.taskDao.CreateTaskEntry(task)
        # call dao to create task
        print("calling dao to create task")
        return None

    def UpdateTask(self, task):
        self.taskDao.UpdateTaskEntry(task)
        # call dao to update task
        print("calling dao to update task")
        return None

    def DeleteTask(self, task):
        self.taskDao.DeleteTaskEntry(task)
        # call dao to delete task
        print("calling dao to delete task")
        return None

    def GetAllTask(self):
        print("calling dao to get task")
        taskList = []
        return taskList, None