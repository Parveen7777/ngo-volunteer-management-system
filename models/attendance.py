from database.db import get_connection

class Attendance:

    @staticmethod
    def mark_attendance(
        volunteer_id,
        event_id,
        attendance_status,
        check_in_time
    ):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO attendance
            (volunteer_id, event_id, attendance_status, check_in_time)
            VALUES (?, ?, ?, ?)
            """,
            (
                volunteer_id,
                event_id,
                attendance_status,
                check_in_time,
            )
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_attendance_records():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT attendance.id,
                   volunteers.name AS volunteer_name,
                   events.title AS event_title,
                   attendance.attendance_status,
                   attendance.check_in_time
            FROM attendance
            JOIN volunteers
              ON attendance.volunteer_id = volunteers.id
            JOIN events
              ON attendance.event_id = events.id
            ORDER BY attendance.id DESC
            """
        )
        records = cursor.fetchall()
        conn.close()
        return records

    @staticmethod
    def get_attendance_by_event(event_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM attendance WHERE event_id=?",
            (event_id,)
        )
        records = cursor.fetchall()
        conn.close()
        return records

    @staticmethod
    def delete_attendance(record_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM attendance WHERE id=?",
            (record_id,)
        )
        conn.commit()
        conn.close()
