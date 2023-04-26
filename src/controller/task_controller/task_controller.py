from src.dao.task_dao.task_dao import TaskDao

class TaskController:
    taskDao = TaskDao()
    def __init__(self) -> None:
        pass

    def CreateTask(self, task):
        self.taskDao.CreateTaskEntry(task)
        # call dao to create task
        print("calling dao to create task")
        return None

    def GetAllTask(self):
        taskDictList = self.taskDao.GetAllTask()
        return taskDictList