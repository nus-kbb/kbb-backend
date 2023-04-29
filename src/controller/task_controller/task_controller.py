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
        err = task.ValidateWithID()
        if err != None:
            return err
        
        taskList = self.taskDao.GetTaskById(task.id)
        if len(taskList) == 0:
            return "task does not exist in database"
        return self.taskDao.UpdateTaskEntry(task)

    def DeleteTask(self, taskId):
        if taskId == "":
            return "task id not defined"

        taskList = self.taskDao.GetTaskById(taskId)
        if len(taskList) == 0:
            return "task does not exist in database"
        
        return self.taskDao.DeleteTaskEntry(taskId)

    def GetAllTask(self):
        taskDictList = self.taskDao.GetAllTask()
        return taskDictList
    
    def GetTaskByProjectId(self, projectId):
        if projectId == "":
            return "project id not defined"
        return self.taskDao.GetTaskByProjectId(projectId)