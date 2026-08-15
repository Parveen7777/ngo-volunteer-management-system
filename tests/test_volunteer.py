import unittest
from services.volunteer_service import VolunteerService

class TestVolunteer(unittest.TestCase):

    def test_get_all_volunteers(self):
        volunteers = VolunteerService.get_all()
        self.assertIsInstance(volunteers, list)

    def test_count_volunteers(self):
        count = VolunteerService.count()
        self.assertGreaterEqual(count, 0)

if __name__ == "__main__":
    unittest.main()
