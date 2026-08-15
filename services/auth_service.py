from models.user import User

class AuthService:

    @staticmethod
    def login(email, password):
        user = User.get_user_by_email(email)

        if user and user['password'] == password:
            return user

        return None

    @staticmethod
    def register(name, email, password):
        User.create_user(name, email, password)
        return True
