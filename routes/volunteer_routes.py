from flask import Blueprint, render_template, request, redirect, url_for
from models.volunteer import Volunteer

volunteer_bp = Blueprint('volunteer', __name__)

@volunteer_bp.route('/volunteers')
def volunteers():
    volunteer_list = Volunteer.get_all_volunteers()
    return render_template('volunteers.html', volunteers=volunteer_list)

@volunteer_bp.route('/volunteers/add', methods=['GET', 'POST'])
def add_volunteer():
    if request.method == 'POST':
        Volunteer.add_volunteer(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['address'],
            request.form['skills'],
            request.form['availability']
        )
        return redirect(url_for('volunteer.volunteers'))

    return render_template('add_volunteer.html')

@volunteer_bp.route('/volunteers/delete/<int:volunteer_id>')
def delete_volunteer(volunteer_id):
    Volunteer.delete_volunteer(volunteer_id)
    return redirect(url_for('volunteer.volunteers'))
