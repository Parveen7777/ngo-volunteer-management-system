from flask import Blueprint, render_template, request, redirect, url_for
from models.attendance import Attendance
from models.volunteer import Volunteer
from models.event import Event
from datetime import datetime

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance')
def attendance():
    records = Attendance.get_attendance_records()
    volunteers = Volunteer.get_all_volunteers()
    events = Event.get_all_events()

    return render_template(
        'attendance.html',
        records=records,
        volunteers=volunteers,
        events=events
    )

@attendance_bp.route('/attendance/mark', methods=['POST'])
def mark_attendance():
    Attendance.mark_attendance(
        request.form['volunteer_id'],
        request.form['event_id'],
        request.form['attendance_status'],
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    return redirect(url_for('attendance.attendance'))

@attendance_bp.route('/attendance/delete/<int:record_id>')
def delete_attendance(record_id):
    Attendance.delete_attendance(record_id)
    return redirect(url_for('attendance.attendance'))
