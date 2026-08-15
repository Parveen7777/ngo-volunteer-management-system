from models.attendance import Attendance
from datetime import datetime

class AttendanceService:

    @staticmethod
    def get_all():
        return Attendance.get_attendance_records()

    @staticmethod
    def mark(volunteer_id, event_id, status):
        Attendance.mark_attendance(
            volunteer_id,
            event_id,
            status,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

    @staticmethod
    def get_by_event(event_id):
        return Attendance.get_attendance_by_event(event_id)

    @staticmethod
    def delete(record_id):
        Attendance.delete_attendance(record_id)
