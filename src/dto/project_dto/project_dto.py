import json
class Project:
    def __init__(self, id, project_name, status, content):
        self.id = id
        self.project_name = project_name
        self.status = status
        self.content = content

    def __repr__(self):
        return f"Project({self.id}, {self.project_name}, {self.status}, {self.content})"

    def to_dict(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "status": self.status,
            "content": self.content
        }

    @staticmethod
    def from_dict(project_dict):
        return Project(
            id=project_dict["id"],
            project_name=project_dict["project_name"],
            content=project_dict["status"],
            project_id=project_dict["content"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(project_json):
        return Project.from_dict(json.loads(project_json))