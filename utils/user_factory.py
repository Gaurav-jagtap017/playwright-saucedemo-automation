from models.user import User

class UserFactory:
    @staticmethod
    def standard_user():
        return User("User1", "Automation", "411001")