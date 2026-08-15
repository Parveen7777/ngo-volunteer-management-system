from flask import Blueprint, render_template
from models.volunteer import Volunteer
from models.event import Event
from models.attendance import Attendance

report_bp = Blueprint('report', __name__)

@report_bp.route('/reports')
def reports():
    volunteers = Volunteer.get_all_volunteers()
    events = Event.get_all_events()
    attendance = Attendance.get_attendance_records()

    return render_template(
        'reports.html',
        volunteers=volunteers,
        events=events,
        attendance=attendance
    )
