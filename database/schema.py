"""
==========================================
BettaHub Database Schema
==========================================

Bu dosya veritabanındaki tabloları oluşturur.
"""

from database.database import DatabaseManager


db = DatabaseManager()


def create_tables():
    """
    BettaHub veritabanı tablolarını oluşturur.
    """

    print("Veritabanı hazırlanıyor...")
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
if __name__ == "__main__":

    create_tables()

    print("BettaHub veritabanı başarıyla oluşturuldu.")