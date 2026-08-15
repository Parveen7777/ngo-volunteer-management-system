import unittest
from services.attendance_service import AttendanceService

class TestAttendance(unittest.TestCase):

    def test_get_attendance(self):
        records = AttendanceService.get_all()
        self.assertIsInstance(records, list)

    def test_get_by_event(self):
        records = AttendanceService.get_by_event(1)
        self.assertIsInstance(records, list)

if __name__ == "__main__":
    unittest.main()
