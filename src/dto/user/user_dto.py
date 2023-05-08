import json
class User:
    def __init__(self, id, user_email, user_password, project_id, role):
        self.id = id
        self.user_email = user_email
        self.user_password = user_password
        self.project_id = project_id
        self.role = role

    def __repr__(self):
        return f"User({self.id}, {self.user_email}, {self.user_password}, {self.project_id})"

    def to_dict(self):
        print(self)
        return {
            "id": self.id,
            "user_email": self.user_email,
            "user_password": self.user_password,
            "project_id": self.project_id,
            "role": self.role
        }

    @staticmethod
    def from_dict(user_dict):
        return User(
            id=user_dict["id"],
            user_email=user_dict["user_email"],
            user_password=user_dict["user_password"],
            project_id=user_dict["project_id"],
            role=user_dict["role"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(user_json):
        return User.from_dict(json.loads(user_json))