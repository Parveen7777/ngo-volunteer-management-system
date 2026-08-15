from flask import Blueprint, render_template
from models.volunteer import Volunteer
from models.event import Event
from models.attendance import Attendance

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    volunteer_count = Volunteer.count_volunteers()
    event_count = Event.count_events()
    attendance_records = Attendance.get_attendance_records()

    return render_template(
        'dashboard.html',
        volunteer_count=volunteer_count,
        event_count=event_count,
        attendance_records=attendance_records
    )
