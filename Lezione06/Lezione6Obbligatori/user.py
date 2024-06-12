class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
