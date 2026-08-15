from database.db import get_connection

class Event:

    @staticmethod
    def add_event(
        title,
        description,
        event_date,
        location,
        required_volunteers
    ):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO events
            (title, description, event_date, location, required_volunteers)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                event_date,
                location,
                required_volunteers,
            )
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_events():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM events ORDER BY event_date ASC")
        events = cursor.fetchall()
        conn.close()
        return events

    @staticmethod
    def get_event(event_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM events WHERE id=?",
            (event_id,)
        )
        event = cursor.fetchone()
        conn.close()
        return event

    @staticmethod
    def update_event(
        event_id,
        title,
        description,
        event_date,
        location,
        required_volunteers,
        status
    ):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE events
            SET title=?, description=?, event_date=?, location=?,
                required_volunteers=?, status=?
            WHERE id=?
            """,
            (
                title,
                description,
                event_date,
                location,
                required_volunteers,
                status,
                event_id,
            )
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_event(event_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM events WHERE id=?",
            (event_id,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def count_events():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM events")
        count = cursor.fetchone()[0]
        conn.close()
        return count
