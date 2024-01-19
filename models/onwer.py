from models.user import User
from models.developer import Developer

class Onwer(Developer):
    def __init__(self, username, email):
       super().__init__(username, email)