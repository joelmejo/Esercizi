from user import User
from privileges import Privileges
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: Privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges
    
    # def show_privileges(self):
    #     print(self.privileges)
