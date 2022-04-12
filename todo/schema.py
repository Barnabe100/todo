from ninja import Schema

class ProjectIn(Schema):
    name: str
    description: str = None

class ProjectUpdate(Schema):
    name: str = None
    description: str = None

class ProjectOut(Schema):
    id: int
    name: str
    description: str

class UserIn(Schema):
    username: str
    password: str
    email : str


class UserOut(Schema):
    id: int
    username: str
    email: str