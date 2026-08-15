from models.event import Event

class EventService:

    @staticmethod
    def get_all():
        return Event.get_all_events()

    @staticmethod
    def add(data):
        Event.add_event(
            data['title'],
            data['description'],
            data['event_date'],
            data['location'],
            data['required_volunteers']
        )

    @staticmethod
    def update(event_id, data):
        Event.update_event(
            event_id,
            data['title'],
            data['description'],
            data['event_date'],
            data['location'],
            data['required_volunteers'],
            data['status']
        )

    @staticmethod
    def delete(event_id):
        Event.delete_event(event_id)

    @staticmethod
    def count():
        return Event.count_events()
