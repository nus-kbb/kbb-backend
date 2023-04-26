from src.dao.task_dao.task_dao import TaskDao

class TaskController:
    taskDao = TaskDao()
    def __init__(self) -> None:
        pass

    def CreateTask(self, task):
        return self.taskDao.CreateTaskEntry(task)

    def GetAllTask(self):
        taskDictList = self.taskDao.GetAllTask()
        return taskDictList