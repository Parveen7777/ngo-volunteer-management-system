from models.volunteer import Volunteer

class VolunteerService:

    @staticmethod
    def get_all():
        return Volunteer.get_all_volunteers()

    @staticmethod
    def add(data):
        Volunteer.add_volunteer(
            data['name'],
            data['email'],
            data['phone'],
            data['address'],
            data['skills'],
            data['availability']
        )

    @staticmethod
    def update(volunteer_id, data):
        Volunteer.update_volunteer(
            volunteer_id,
            data['name'],
            data['email'],
            data['phone'],
            data['address'],
            data['skills'],
            data['availability'],
            data['status']
        )

    @staticmethod
    def delete(volunteer_id):
        Volunteer.delete_volunteer(volunteer_id)

    @staticmethod
    def count():
        return Volunteer.count_volunteers()
