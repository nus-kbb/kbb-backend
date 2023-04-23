import json
class User:
    def __init__(self, user_email, user_password, project_id):
        self.user_email = user_email
        self.user_password = user_password
        self.project_id = project_id

    def __repr__(self):
        return f"User({self.user_email}, {self.user_password}, {self.project_id})"

    def to_dict(self):
        return {
            "user_email": self.user_email,
            "user_password": self.user_password,
            "project_id": self.project_id
        }

    @staticmethod
    def from_dict(user_dict):
        return User(
            id=user_dict["id"],
            name=user_dict["user_email"],
            email=user_dict["user_password"],
            password=user_dict["project_id"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(user_json):
        return User.from_dict(json.loads(user_json))