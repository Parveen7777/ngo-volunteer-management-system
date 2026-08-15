from models.volunteer import Volunteer
from models.event import Event
from models.attendance import Attendance

class ReportService:

    @staticmethod
    def generate_summary():
        volunteers = Volunteer.get_all_volunteers()
        events = Event.get_all_events()
        attendance = Attendance.get_attendance_records()

        return {
            'total_volunteers': len(volunteers),
            'total_events': len(events),
            'total_attendance': len(attendance),
            'volunteers': volunteers,
            'events': events,
            'attendance': attendance
        }

    @staticmethod
    def volunteer_report():
        return Volunteer.get_all_volunteers()

    @staticmethod
    def event_report():
        return Event.get_all_events()

    @staticmethod
    def attendance_report():
        return Attendance.get_attendance_records()
