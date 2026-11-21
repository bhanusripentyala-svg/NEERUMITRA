import sqlite3

def connect_db():
    return sqlite3.connect("neerumitra.db")

def create_tables():
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            village TEXT,
            mobile TEXT,
            crop TEXT,
            soil TEXT,
            field_size REAL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farmer_id INTEGER,
            soil_condition TEXT,
            rainfall TEXT,
            suggestion TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    con.commit()
    con.close()

def add_farmer(name, village, mobile, crop, soil, field_size):
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO farmers
        (name, village, mobile, crop, soil, field_size)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, village, mobile, crop, soil, field_size))

    farmer_id = cur.lastrowid
    con.commit()
    con.close()

    return farmer_id

def save_history(farmer_id, condition, rainfall, suggestion):
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO history
        (farmer_id, soil_condition, rainfall, suggestion)
        VALUES (?, ?, ?, ?)
    """, (farmer_id, condition, rainfall, suggestion))

    con.commit()
    con.close()

def get_history(farmer_id):
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        SELECT soil_condition, rainfall, suggestion, date
        FROM history WHERE farmer_id = ?
        ORDER BY id DESC
    """, (farmer_id,))

    records = cur.fetchall()
    con.close()

    return records