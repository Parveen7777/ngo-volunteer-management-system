import unittest
from services.auth_service import AuthService

class TestAuth(unittest.TestCase):

    def test_login_invalid_user(self):
        user = AuthService.login(
            "invalid@example.com",
            "wrongpassword"
        )
        self.assertIsNone(user)

    def test_register(self):
        result = AuthService.register(
            "Test User",
            "test@example.com",
            "password123"
        )
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
