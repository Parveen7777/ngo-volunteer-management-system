from flask import Blueprint, render_template, request, redirect, url_for
from models.event import Event

event_bp = Blueprint('event', __name__)

@event_bp.route('/events')
def events():
    event_list = Event.get_all_events()
    return render_template('events.html', events=event_list)

@event_bp.route('/events/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        Event.add_event(
            request.form['title'],
            request.form['description'],
            request.form['event_date'],
            request.form['location'],
            request.form['required_volunteers']
        )
        return redirect(url_for('event.events'))

    return render_template('add_event.html')

@event_bp.route('/events/delete/<int:event_id>')
def delete_event(event_id):
    Event.delete_event(event_id)
    return redirect(url_for('event.events'))
