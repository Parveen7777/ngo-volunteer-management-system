from database.db import get_connection
from database.schema import create_tables

def seed_data():
    create_tables()

    conn = get_connection()
    cursor = conn.cursor()

    # Admin user
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
    ''', (
        "Admin",
        "admin@ngo.org",
        "admin123",
        "admin"
    ))

    # Sample volunteers
    volunteers = [
        ("Rahul Sharma", "rahul@example.com", "9876543210", "Hyderabad", "Teaching", "Weekends", "Active"),
        ("Priya Reddy", "priya@example.com", "9123456780", "Bangalore", "Medical", "Full Time", "Active"),
        ("Arjun Kumar", "arjun@example.com", "9988776655", "Chennai", "Fundraising", "Evenings", "Inactive")
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO volunteers
        (name, email, phone, address, skills, availability, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', volunteers)

    # Sample events
    events = [
        ("Food Distribution Drive", "Distribute food packets to needy families", "2026-09-15", "Hyderabad", 20, "Upcoming"),
        ("Blood Donation Camp", "Organize blood donation awareness and collection", "2026-09-20", "Bangalore", 15, "Upcoming"),
        ("Tree Plantation", "Plant 500 saplings in public parks", "2026-09-25", "Chennai", 30, "Upcoming")
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO events
        (title, description, event_date, location, required_volunteers, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', events)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully.")

if __name__ == "__main__":
    seed_data()
