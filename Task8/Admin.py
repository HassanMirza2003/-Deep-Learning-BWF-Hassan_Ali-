class User:
    def __init__(self , first , last) -> None:
        self.firstname= first
        self.lastname = last
        self.login_attempts = 0

    def describe_user(self) :
        print(f"first name is {self.firstname} and last name is {self.lastname}")

    def greetUser(self):
        print(f"Hi {self.firstname} {self.lastname}")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts=0
        
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")