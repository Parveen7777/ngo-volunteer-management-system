import unittest
from services.event_service import EventService

class TestEvent(unittest.TestCase):

    def test_get_all_events(self):
        events = EventService.get_all()
        self.assertIsInstance(events, list)

    def test_count_events(self):
        count = EventService.count()
        self.assertGreaterEqual(count, 0)

if __name__ == "__main__":
    unittest.main()
