from database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'admin'
        )
    ''')

    # Volunteers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            skills TEXT,
            availability TEXT,
            status TEXT DEFAULT 'Active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Events table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            event_date TEXT,
            location TEXT,
            required_volunteers INTEGER,
            status TEXT DEFAULT 'Upcoming'
        )
    ''')

    # Attendance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            volunteer_id INTEGER,
            event_id INTEGER,
            attendance_status TEXT DEFAULT 'Absent',
            check_in_time TEXT,
            FOREIGN KEY (volunteer_id) REFERENCES volunteers(id),
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database tables created successfully.")

if __name__ == "__main__":
    create_tables()
