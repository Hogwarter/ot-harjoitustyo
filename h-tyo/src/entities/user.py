import uuid

class User:
    def __init__(self, username, password, user_id=None):  # profile pic?
        self.username = username
        self.password = password
        self.user_id = user_id or str(uuid.uuid4())
