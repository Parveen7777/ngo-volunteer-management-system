from database.db import get_connection

class Volunteer:

    @staticmethod
    def add_volunteer(name, email, phone, address, skills, availability):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO volunteers
            (name, email, phone, address, skills, availability)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (name, email, phone, address, skills, availability)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_volunteers():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM volunteers ORDER BY id DESC")
        volunteers = cursor.fetchall()
        conn.close()
        return volunteers

    @staticmethod
    def get_volunteer(volunteer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM volunteers WHERE id=?",
            (volunteer_id,)
        )
        volunteer = cursor.fetchone()
        conn.close()
        return volunteer

    @staticmethod
    def update_volunteer(
        volunteer_id,
        name,
        email,
        phone,
        address,
        skills,
        availability,
        status
    ):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE volunteers
            SET name=?, email=?, phone=?, address=?, skills=?,
                availability=?, status=?
            WHERE id=?
            """,
            (
                name,
                email,
                phone,
                address,
                skills,
                availability,
                status,
                volunteer_id,
            )
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_volunteer(volunteer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM volunteers WHERE id=?",
            (volunteer_id,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def count_volunteers():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        count = cursor.fetchone()[0]
        conn.close()
        return count
