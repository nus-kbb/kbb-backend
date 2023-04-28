from src.dao.task_dao.task_dao import TaskDao

class TaskController:
    taskDao = TaskDao()
    def __init__(self) -> None:
        pass

    def CreateTask(self, task):
        err = task.Validate()
        if err != None:
            return err
        return self.taskDao.CreateTaskEntry(task)

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
        taskDictList = self.taskDao.GetAllTask()
        return taskDictList