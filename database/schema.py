"""
BettaHub
Database Schema
"""

from database.database import DatabaseManager

db = DatabaseManager()


def create_users_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,

        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        phone TEXT,

        country TEXT,

        language TEXT DEFAULT 'tr',

        membership TEXT DEFAULT 'FREE',

        is_admin INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


def create_fish_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS fish (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fish_code TEXT UNIQUE NOT NULL,

        name TEXT NOT NULL,

        species TEXT,

        variety TEXT,

        gender TEXT,

        color TEXT,

        birth_date TEXT,

        aquarium TEXT,

        section TEXT,

        status TEXT DEFAULT 'Aktif',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


def create_tables():

    print("Veritabanı hazırlanıyor...")

    create_users_table()

    create_fish_table()

    print("Tablolar hazır.")


if __name__ == "__main__":

    create_tables()

    db.close()

    print("BettaHub veritabanı başarıyla oluşturuldu.")