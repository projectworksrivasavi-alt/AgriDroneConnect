import sqlite3

conn = sqlite3.connect("agri.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS operators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT,
    email TEXT,
    license_no TEXT,
    drone_no TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_name TEXT,
    mobile TEXT,
    village TEXT,
    crop TEXT,
    area TEXT,
    booking_date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")