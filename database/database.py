"""
BettaHub
Database Manager
"""

import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        db_path = Path(__file__).parent / "bettahub.db"

        self.connection = sqlite3.connect(db_path)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()

    def fetchall(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchall()

    def executemany(self, query, data):

        self.cursor.executemany(query, data)

        self.connection.commit()

    def close(self):

        self.connection.close()