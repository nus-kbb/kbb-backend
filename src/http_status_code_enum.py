import enum
class HttpCode(enum.Enum):
    Success=200
    BadRequest=400

class HTTPContentType(enum.Enum):
    JSON='application/json'
    TEXT='text/plain'