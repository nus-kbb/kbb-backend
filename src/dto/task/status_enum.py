import enum
class Status(enum.Enum):
    WAITING="waiting"
    DEVELOPING="developing"
    REVIEWING="reviewing"
    TESTING="testing"
    DONE="done"